from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey
import PIL.Image


funcs = ft_red, ft_green, ft_blue, ft_invert, ft_grey
image = ft_load('landscape.jpg')


for f in funcs:
    result = f(image)
    if result is not None:
        PIL.Image.fromarray(result).show()
