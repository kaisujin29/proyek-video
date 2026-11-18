"""Komponen gaya khas untuk lapisan gambar (kanvas 2000x2000, disimpan 1000x1000).

Pakai di skrip lapisan:
    import sys; sys.path.insert(0, "<folder skill>")
    from komponen import *
    img, d = kanvas(); kartu(img, (150, 300, 1850, 1300), tab="CLAUDE.md"); simpan(img, "a1_kartu.png")

Semua lapisan satu adegan memakai kanvas yang sama (2000x2000), jadi posisi antar-lapisan selalu cocok.
"""
import math, os
from PIL import Image, ImageDraw, ImageFont

DIR = os.path.dirname(os.path.abspath(__file__))
HITAM, KARTU, TEPI = (18, 18, 18), (40, 40, 40, 225), (78, 78, 78)
OREN, KUNING, PUTIH, ABU = (255, 122, 0), (255, 212, 0), (255, 255, 255), (150, 150, 150)
HIJAU, MERAH, COKLAT = (88, 200, 96), (226, 58, 52), (92, 52, 18)


def _f(nama, px):
    return ImageFont.truetype(os.path.join(DIR, "fonts", nama), px)
def judul(px): return _f("Montserrat-ExtraBold.ttf", px)
def tebal(px): return _f("Montserrat-Bold.ttf", px)
def isi(px): return _f("Inter-SemiBold.otf", px)
def mono(px): return _f("JetBrainsMono-Regular.ttf", px)


def kanvas():
    img = Image.new("RGBA", (2000, 2000), (0, 0, 0, 0))
    return img, ImageDraw.Draw(img)


def simpan(img, path):
    img.resize((1000, 1000), Image.LANCZOS).save(path)


def kartu(img, box, tab=None):
    """Kartu kaca gelap semi-transparan, sudut membulat, tepi tipis. tab = chip nama file di kiri atas."""
    lap = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(lap)
    d.rounded_rectangle(box, 40, fill=KARTU, outline=TEPI, width=4)
    if tab:
        f = mono(40)
        w = f.getlength(tab)
        d.rounded_rectangle([box[0] + 40, box[1] + 36, box[0] + 40 + w + 60, box[1] + 106], 14,
                            fill=COKLAT, outline=OREN, width=4)
        d.text((box[0] + 70, box[1] + 46), tab, font=f, fill=PUTIH)
    img.alpha_composite(lap)


def kode(d, box, baris, sorot=None, px=52):
    """Isi editor: nomor baris abu, baris '## ...' kuning, baris lain putih. sorot = indeks baris yang diberi pita coklat."""
    f = mono(px)
    x, y = box[0] + 50, box[1] + 150
    for i, teks in enumerate(baris):
        if sorot == i:
            d.rounded_rectangle([box[0] + 30, y - 16, box[2] - 30, y + px + 22], 12, fill=COKLAT + (230,))
        d.text((x, y), str(i + 1), font=mono(int(px * 0.7)), fill=(100, 100, 100))
        d.text((x + 70, y), teks, font=f, fill=KUNING if teks.startswith("#") else PUTIH)
        y += int(px * 1.9)


def ikon_folder(d, x, y, s=1.0, warna=OREN):
    d.rounded_rectangle([x, y, x + 60 * s, y + 18 * s], 5 * s, fill=warna)
    d.rounded_rectangle([x, y + 10 * s, x + 90 * s, y + 70 * s], 8 * s, fill=warna)


def folder(d, box, item, px=46):
    """Pohon folder. item = [(nama, level, keterangan, status)], status: None / "salah" (merah) / "sorot" (coklat)."""
    y = box[1] + 70
    for nama, level, ket, status in item:
        if status:
            d.rounded_rectangle([box[0] + 30, y - 14, box[2] - 30, y + px + 18], 12,
                                fill=(110, 30, 26, 230) if status == "salah" else COKLAT + (230,))
        x = box[0] + 60 + level * 70
        ikon_folder(d, x, y + 4, 0.55, MERAH if status == "salah" else OREN)
        d.text((x + 70, y), nama, font=mono(px), fill=PUTIH)
        if ket:
            f = isi(int(px * 0.62))
            d.text((box[2] - 60 - f.getlength(ket), y + 10), ket, font=f, fill=MERAH if status == "salah" else ABU)
        y += int(px * 1.75)


def stempel(img, teks, pusat, warna=OREN, sudut=-10, px=150):
    """Stempel miring bergaris tepi: WAJIB (oranye), SALAH (merah), SERAGAM (hijau)."""
    f = judul(px)
    w, h = int(f.getlength(teks)) + 90, int(px * 1.45)
    st = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(st)
    d.rounded_rectangle([6, 6, w - 6, h - 6], 22, outline=warna, width=14)
    d.text((45, h * 0.1), teks, font=f, fill=warna)
    st = st.rotate(sudut, expand=True, resample=Image.BICUBIC)
    img.alpha_composite(st, (int(pusat[0] - st.width / 2), int(pusat[1] - st.height / 2)))


def pil(d, pusat, teks, warna=KUNING, px=48, teks_warna=HITAM):
    f = isi(px)
    w = f.getlength(teks)
    d.rounded_rectangle([pusat[0] - w / 2 - 50, pusat[1] - px, pusat[0] + w / 2 + 50, pusat[1] + px], px, fill=warna)
    d.text((pusat[0] - w / 2, pusat[1] - px * 0.62), teks, font=f, fill=teks_warna)


def berkas_zip(d, x, y, s=1.0):
    w, h = 360 * s, 460 * s
    d.polygon([(x, y), (x + w - 110 * s, y), (x + w, y + 110 * s), (x + w, y + h), (x, y + h)], fill=OREN)
    d.polygon([(x + w - 110 * s, y), (x + w, y + 110 * s), (x + w - 110 * s, y + 110 * s)], fill=(200, 92, 0))
    for k in range(6):
        yy = y + 40 * s + k * 45 * s
        d.rectangle([x + w / 2 - 40 * s + (k % 2) * 40 * s, yy, x + w / 2 + (k % 2) * 40 * s, yy + 30 * s], fill=HITAM)
    d.rounded_rectangle([x + w / 2 - 50 * s, y + 320 * s, x + w / 2 + 50 * s, y + 420 * s], 20 * s, fill=HITAM)


def hp(d, x, y, w=650, h=1250, layar=(26, 26, 26)):
    d.rounded_rectangle([x, y, x + w, y + h], 90, fill=(30, 30, 30), outline=(70, 70, 70), width=8)
    d.rounded_rectangle([x + 30, y + 30, x + w - 30, y + h - 30], 64, fill=layar)
    d.rounded_rectangle([x + w / 2 - 90, y + 55, x + w / 2 + 90, y + 85], 15, fill=(60, 60, 60))


def truk(d, x, y, s=1.0):
    """Dump truck oranye; (x, y) = kiri bawah roda."""
    d.polygon([(x, y - 230 * s), (x + 420 * s, y - 230 * s), (x + 400 * s, y - 90 * s), (x + 20 * s, y - 90 * s)], fill=OREN)
    for k in range(5):
        d.rectangle([x + 40 * s + k * 75 * s, y - 210 * s, x + 70 * s + k * 75 * s, y - 110 * s], fill=(205, 92, 0))
    d.rectangle([x + 430 * s, y - 220 * s, x + 600 * s, y - 90 * s], fill=OREN)
    d.rectangle([x + 470 * s, y - 200 * s, x + 580 * s, y - 140 * s], fill=(60, 74, 85))
    d.rectangle([x, y - 95 * s, x + 600 * s, y - 70 * s], fill=(60, 60, 60))
    for cx in (x + 110 * s, x + 300 * s, x + 500 * s):
        d.ellipse([cx - 70 * s, y - 140 * s, cx + 70 * s, y], fill=(20, 20, 20))
        d.ellipse([cx - 28 * s, y - 98 * s, cx + 28 * s, y - 42 * s], fill=(90, 90, 90))


def pekerja(d, x, y, s=1.0, apd=True):
    """Pekerja tambang berdiri; (x, y) = tengah bawah kaki. apd=False: tanpa helm & rompi."""
    d.rectangle([x - 55 * s, y - 230 * s, x - 10 * s, y], fill=(50, 60, 80))
    d.rectangle([x + 10 * s, y - 230 * s, x + 55 * s, y], fill=(50, 60, 80))
    d.rounded_rectangle([x - 80 * s, y - 520 * s, x + 80 * s, y - 220 * s], 30 * s, fill=OREN if apd else (90, 110, 140))
    if apd:
        for yy in (y - 430 * s, y - 330 * s):
            d.rectangle([x - 80 * s, yy, x + 80 * s, yy + 22 * s], fill=(220, 220, 220))
    d.ellipse([x - 60 * s, y - 650 * s, x + 60 * s, y - 530 * s], fill=(200, 150, 110))
    if apd:
        d.chord([x - 75 * s, y - 690 * s, x + 75 * s, y - 560 * s], 180, 360, fill=KUNING)
        d.rectangle([x - 90 * s, y - 628 * s, x + 90 * s, y - 612 * s], fill=KUNING)


def hazard(d, box, lebar=60):
    """Pita hazard kuning-hitam diagonal."""
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=KUNING)
    h = y1 - y0
    x = x0 - h
    while x < x1:
        d.polygon([(max(x0, x), y1), (min(x1, x + lebar), y1), (min(x1, x + lebar + h), y0), (max(x0, x + h), y0)][:4],
                  fill=HITAM)
        x += lebar * 2


def screenshot(img, path, y0, tinggi=1000, box=(200, 300, 1800, None)):
    """Potongan screenshot HP (lebar 1080, mulai baris y0) di dalam kartu kaca. Kembalikan fungsi ke(x, y)
    untuk memetakan koordinat screenshot ke kanvas (dipakai sorot())."""
    x0, yb, x1, _ = box
    w = x1 - x0
    s = w / 1080
    h = int(tinggi * s)
    kartu(img, (x0 - 26, yb - 26, x1 + 26, yb + h + 26))
    crop = Image.open(path).convert("RGB").crop((0, y0, 1080, y0 + tinggi)).resize((w, h), Image.LANCZOS)
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, w, h], 30, fill=255)
    img.paste(crop, (x0, yb), m)
    return lambda x, y: (x0 + x * s, yb + (y - y0) * s)


def sorot(d, ke, box, ketuk=True):
    """Kotak kuning di tombol pada screenshot (koordinat asli screenshot) + titik ketukan oranye-putih."""
    x1, y1 = ke(box[0], box[1]); x2, y2 = ke(box[2], box[3])
    d.rounded_rectangle([x1 - 14, y1 - 14, x2 + 14, y2 + 14], 26, outline=KUNING, width=16)
    if ketuk:
        cx, cy = x2 - min(60, (x2 - x1) * 0.3), y2 - (y2 - y1) * 0.3
        d.ellipse([cx - 70, cy - 70, cx + 70, cy + 70], outline=OREN, width=12)
        d.ellipse([cx - 32, cy - 32, cx + 32, cy + 32], fill=PUTIH)


def follow(img, d, nama="Seri belajar edit", sub="pakai Claude", box=(250, 700, 1750, 1100)):
    """Kartu penutup: avatar pekerja + nama + tombol Follow oranye."""
    kartu(img, box)
    cx, cy = box[0] + 150, (box[1] + box[3]) / 2
    d.ellipse([cx - 95, cy - 95, cx + 95, cy + 95], fill=(60, 60, 60))
    pekerja(d, cx, cy + 150, 0.33)
    d.text((cx + 140, cy - 70), nama, font=tebal(60), fill=PUTIH)
    d.text((cx + 140, cy + 10), sub, font=isi(44), fill=ABU)
    d.rounded_rectangle([box[2] - 380, cy - 60, box[2] - 60, cy + 60], 60, fill=OREN)
    f = tebal(52)
    d.text((box[2] - 220 - f.getlength("Follow") / 2, cy - 34), "Follow", font=f, fill=HITAM)
