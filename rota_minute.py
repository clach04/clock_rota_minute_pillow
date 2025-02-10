import datetime

from PIL import Image
from PIL import ImageDraw

screen_res = (100, 100)

image = Image.new('RGB', screen_res, 'white')
draw = ImageDraw.Draw(image)


now = datetime.datetime.now()

hours = now.hour
minutes = now.minute

"""
hours = 11
minutes = 15

degree = 90  # for 15 mins, quarter of an hour
degree = 180  # for 30 mins, half of an hour
degree = 270  # for 45 mins, three-quarter of an hour
"""

degree = minutes * 6  # 360 / 60

# https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#PIL.ImageDraw.ImageDraw.ellipse
# ImageDraw.ellipse(xy, fill=None, outline=None, width=1)



# https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#PIL.ImageDraw.ImageDraw.arc
# ImageDraw.arc(xy, start, end, fill=None, width=0)[source]
#  Angles are measured from 3 o'clock, increasing clockwise
# FIXME hard coded coordinates
draw.arc((10, 10, 10+80, 10+80), -90, degree-90, fill='black', width=10)  # draw an arc in black

image.show()
