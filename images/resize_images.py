from pathlib import Path
from PIL import Image, ImageChops

IN  = Path("/Users/shane/Desktop/Team23_Media/").expanduser()
OUT = Path("~/Desktop/resized_images_cover").expanduser()
OUT.mkdir(parents=True, exist_ok=True)

TARGET_W, TARGET_H = 808, 716          # final real size

def auto_trim(im, tol=3):
    """Remove a solid-colour border (white, black, etc.)."""
    bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -tol)  # drop near-bg pixels
    box = diff.getbbox()               # bounding box of real content
    return im if box is None else im.crop(box)

def cover_crop(im):
    w, h = im.size
    scale = max(TARGET_W / w, TARGET_H / h)
    im = im.resize((round(w*scale), round(h*scale)), Image.LANCZOS)
    left   = (im.width  - TARGET_W) // 2
    top    = (im.height - TARGET_H) // 2
    return im.crop((left, top, left+TARGET_W, top+TARGET_H))

for f in IN.glob("*.[jp][pn]g"):       # jpg / jpeg / png
    with Image.open(f) as img:
        img = auto_trim(img)           # ① strip padding
        img = cover_crop(img)          # ② true uniform size
        img.save(OUT / f.name, quality=95)

print("✓ Done: all images are exactly 808 × 716 px, no inner borders.")
