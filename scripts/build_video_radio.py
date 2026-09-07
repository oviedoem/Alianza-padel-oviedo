# -*- coding: utf-8 -*-
"""Arma el video vertical Oviedo Express: 4 imagenes reales con efecto Ken Burns
+ audio de radio real + subtitulos quemados (transcripcion literal del audio).
No genera ningun contenido sintetico: solo recorta/escala/superpone archivos reales.
"""
import re
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from moviepy import VideoClip, ImageClip, AudioFileClip, CompositeVideoClip, concatenate_videoclips

BASE = r"E:\alianza-padel-oviedo"
OUT = BASE + r"\output\video-radio-oviedo-express.mp4"

W, H = 1080, 1920

IMAGES = [
    BASE + r"\output\flyer-apertura-oviedo-express-9x16.png",
    BASE + r"\output\flyer-logistica-oviedo-express-1x1.png",
    BASE + r"\output\flyer-collage-3fotos-1x1.png",
    BASE + r"\output\cierre-video-vertical.png",
]
AUDIO = BASE + r"\assets\audio\radio-oviedo-express.mp3"
SRT = BASE + r"\assets\audio\radio-oviedo-express.srt"
FONT_PATH = r"C:\Windows\Fonts\arialbd.ttf"
BURN_SUBTITLES = False  # sin subtitulos quemados, a pedido del usuario


def cover_fit(img: Image.Image, w: int, h: int) -> Image.Image:
    src_ratio = img.width / img.height
    dst_ratio = w / h
    if src_ratio > dst_ratio:
        new_h = h
        new_w = int(h * src_ratio)
    else:
        new_w = w
        new_h = int(w / src_ratio)
    resized = img.resize((new_w, new_h), Image.LANCZOS)
    x0 = (new_w - w) // 2
    y0 = (new_h - h) // 2
    return resized.crop((x0, y0, x0 + w, y0 + h))


def ken_burns_clip(path: str, duration: float, zoom_in: bool) -> VideoClip:
    src = Image.open(path).convert("RGB")
    margin = 1.06
    big_w, big_h = int(W * margin), int(H * margin)
    big = cover_fit(src, big_w, big_h)
    big_arr = np.array(big)

    def frame_function(t):
        p = min(max(t / duration, 0.0), 1.0)
        p = p if zoom_in else (1.0 - p)
        cw = int(big_w - (big_w - W) * p)
        ch = int(big_h - (big_h - H) * p)
        cw = max(cw, W)
        ch = max(ch, H)
        x0 = (big_w - cw) // 2
        y0 = (big_h - ch) // 2
        crop = big_arr[y0:y0 + ch, x0:x0 + cw]
        frame = Image.fromarray(crop).resize((W, H), Image.LANCZOS)
        return np.array(frame)

    return VideoClip(frame_function, duration=duration)


def letterbox_clip(path: str, duration: float) -> VideoClip:
    """Para imagenes cuyo aspecto no es 9:16 (ej. piezas cuadradas con texto
    propio pegado al borde): se muestran COMPLETAS sin recortar (contain-fit),
    con un fondo desenfocado de la misma imagen rellenando las franjas, y solo
    el fondo tiene un leve zoom para que no se vea estatico. El primer plano
    nunca se recorta, asi el texto propio de la pieza nunca queda cortado.
    """
    src = Image.open(path).convert("RGB")

    bg_margin = 1.15
    big_w, big_h = int(W * bg_margin), int(H * bg_margin)
    bg = cover_fit(src, big_w, big_h)
    bg = bg.filter(ImageFilter.GaussianBlur(28))
    dark = Image.new("RGB", bg.size, (0, 0, 0))
    bg = Image.blend(bg, dark, 0.35)
    bg_arr = np.array(bg)

    scale = W / src.width
    fg = src.resize((W, int(src.height * scale)), Image.LANCZOS)
    if fg.height > H:
        fg = fg.crop((0, (fg.height - H) // 2, W, (fg.height - H) // 2 + H))
    fg_arr = np.array(fg)
    fg_y0 = (H - fg.height) // 2

    def frame_function(t):
        p = min(max(t / duration, 0.0), 1.0)
        cw = int(big_w - (big_w - W) * p)
        ch = int(big_h - (big_h - H) * p)
        cw = max(cw, W)
        ch = max(ch, H)
        x0 = (big_w - cw) // 2
        y0 = (big_h - ch) // 2
        crop = bg_arr[y0:y0 + ch, x0:x0 + cw]
        frame_img = Image.fromarray(crop).resize((W, H), Image.LANCZOS)
        frame_img.paste(Image.fromarray(fg_arr), (0, fg_y0))
        return np.array(frame_img)

    return VideoClip(frame_function, duration=duration)


def parse_srt(path: str):
    text = open(path, encoding="utf-8").read()
    blocks = re.split(r"\n\s*\n", text.strip())
    entries = []
    time_re = re.compile(r"(\d{2}):(\d{2}):(\d{2}),(\d{3})\s*-->\s*(\d{2}):(\d{2}):(\d{2}),(\d{3})")

    def to_sec(h, m, s, ms):
        return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000.0

    for b in blocks:
        lines = b.strip().splitlines()
        if len(lines) < 2:
            continue
        m = time_re.search(lines[1])
        if not m:
            continue
        start = to_sec(*m.groups()[0:4])
        end = to_sec(*m.groups()[4:8])
        caption = " ".join(lines[2:]).strip()
        caption = re.sub(r"^Speaker\s*\d+:\s*", "", caption)
        entries.append((start, end, caption))
    return entries


def wrap_text(draw, text, font, max_width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# Cada pieza tiene su propio texto en un lugar distinto del diseño; se eligio
# a mano, revisando cada imagen, donde SI hay espacio libre para el subtitulo:
#   0 apertura   -> texto propio abajo (55%-85%)      => subtitulo ARRIBA
#   1 logistica  -> texto propio medio-bajo del cuadro => subtitulo ARRIBA
#   2 collage    -> texto propio ARRIBA                => subtitulo ABAJO
#   3 cierre     -> texto propio al medio              => subtitulo ARRIBA
ANCHOR_MODE = ["top", "top", "bottom", "top"]
TOP_ANCHOR = 430
BOTTOM_MARGIN = 470


def caption_clip(text: str, start: float, end: float, mode: str) -> ImageClip:
    font = ImageFont.truetype(FONT_PATH, 44)
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)
    lines = wrap_text(draw, text.upper(), font, W - 160)

    line_h = 54
    total_h = len(lines) * line_h
    pad_x, pad_y = 30, 18
    box_w = max(draw.textlength(l, font=font) for l in lines) + pad_x * 2
    box_h = total_h + pad_y * 2
    box_x0 = (W - box_w) / 2
    box_y0 = TOP_ANCHOR if mode == "top" else (H - BOTTOM_MARGIN - box_h)

    draw.rounded_rectangle(
        [box_x0, box_y0, box_x0 + box_w, box_y0 + box_h],
        radius=16, fill=(13, 13, 13, 215)
    )
    y = box_y0 + pad_y
    for line in lines:
        lw = draw.textlength(line, font=font)
        x = (W - lw) / 2
        draw.text((x, y), line, font=font, fill=(255, 255, 255, 255))
        y += line_h

    clip = ImageClip(np.array(canvas)).with_start(start).with_duration(end - start)
    return clip


def main():
    audio = AudioFileClip(AUDIO)
    total_dur = audio.duration
    per_img = total_dur / len(IMAGES)

    target_ratio = W / H  # 9:16 = 0.5625

    img_clips = []
    img_bounds = []  # (t_start, t_end) por imagen, para ubicar cada subtitulo
    t_cursor = 0.0
    for i, path in enumerate(IMAGES):
        dur = per_img if i < len(IMAGES) - 1 else (total_dur - t_cursor)
        with Image.open(path) as im:
            src_ratio = im.width / im.height
        if abs(src_ratio - target_ratio) < 0.05:
            # ya es vertical 9:16: recorte+paneo (Ken Burns) sin perder nada relevante
            clip = ken_burns_clip(path, dur, zoom_in=(i % 2 == 0))
        else:
            # aspecto distinto (ej. pieza cuadrada con texto pegado al borde):
            # se muestra completa, sin recortar, con fondo desenfocado
            clip = letterbox_clip(path, dur)
        img_clips.append(clip)
        img_bounds.append((t_cursor, t_cursor + dur))
        t_cursor += dur

    base_video = concatenate_videoclips(img_clips, method="chain")

    layers = [base_video]
    if BURN_SUBTITLES:
        def anchor_for(t):
            for idx, (t0, t1) in enumerate(img_bounds):
                if t0 <= t < t1:
                    return ANCHOR_MODE[idx]
            return ANCHOR_MODE[-1]

        subs = parse_srt(SRT)
        layers += [
            caption_clip(text, start, min(end, total_dur), anchor_for(start))
            for start, end, text in subs
        ]

    final = CompositeVideoClip(layers, size=(W, H))
    final = final.with_audio(audio).with_duration(total_dur)

    final.write_videofile(
        OUT, fps=30, codec="libx264", audio_codec="aac",
        bitrate="6000k", audio_bitrate="192k", threads=4,
        temp_audiofile=BASE + r"\output\_temp_audio.m4a",
        remove_temp=True,
    )


if __name__ == "__main__":
    main()
