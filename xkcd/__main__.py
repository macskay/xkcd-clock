from PIL import Image
from datetime import datetime

from xkcd.settings import Settings


def main():
    settings = Settings()
    summertime = settings.options.summertime

    inside_img = Image.open("../resources/insidea.png")
    outside_img = Image.open("../resources/outside.png")

    inside_img = inside_img.convert("RGBA")
    outside_img = outside_img.convert("RGBA")

    dt = datetime.utcnow()
    print(dt.hour, dt.minute)

    magnitudes = 24 - dt.hour-1

    if summertime:
        magnitudes -= 1

    angle_h = magnitudes * 15
    angle_m = round(15 / 60 * dt.minute)

    inside_img = inside_img.rotate(angle_h + angle_m)

    Image.alpha_composite(outside_img, inside_img).show()

if __name__ == '__main__':
    main()
