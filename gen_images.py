from PIL import Image, ImageDraw, ImageFilter
import random
random.seed(7)
def make(name, c1, c2, w=3200, h=2000):
    img = Image.new("RGB", (w, h))
    px = img.load()
    for y in range(h):
        for x in range(0, w):
            t = (x/w + y/h)/2
            n = random.randint(-18, 18)
            px[x, y] = tuple(max(0, min(255, int(c1[i]+(c2[i]-c1[i])*t)+n)) for i in range(3))
    d = ImageDraw.Draw(img)
    for _ in range(25):
        x, y, r = random.randint(0,w), random.randint(0,h), random.randint(100,400)
        d.ellipse([x-r,y-r,x+r,y+r], outline=(255,255,255), width=6)
    img.save(f"before/img/{name}.png")
    # optimized variants
    for width in (480, 960):
        s = img.resize((width, int(h*width/w)), Image.LANCZOS)
        s.save(f"after/img/{name}-{width}.webp", "WEBP", quality=72, method=6)
make("hero", (30,60,140), (240,120,60))
make("project1", (20,120,100), (230,220,90))
make("project2", (120,30,120), (60,180,220))
make("project3", (200,50,60), (250,200,120))
