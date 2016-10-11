#!/usr/bin/env python
   
black_pixel = [0, 0, 0]
white_pixel = [255, 255, 255]
green_pixel = [0, 255, 0]
red_pixel = [255, 0, 0]
blue_pixel = [0, 0, 255]

def color_ratio(color, ratio):
    if ratio < 0:
        ratio = 0
    elif ratio > 1:
        ratio = 1

    r = color[0] * ratio
    g = color[1] * ratio
    b = color[2] * ratio
    return [r, g, b]