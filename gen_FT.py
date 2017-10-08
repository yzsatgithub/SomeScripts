#!/usr/bin/python
#coding=utf-8
import sys
import numpy as np
from EMAN2 import *

print len(sys.argv)
if len(sys.argv) < 3:
    print 'usage: gen_FT.py [input (absolute) path to an image] [output (absolute) path]'
    exit(0)

input_image = sys.argv[1]
output_image = sys.argv[2]

img = EMData(input_image)
img_mat = EMNumPy.em2numpy(img)
ft_img_mat = np.fft.fft2(img_mat)
ft_img_shifted = np.fft.fftshift(ft_img_mat)
ft_img_shifted = EMNumPy.numpy2em(np.abs(ft_img_shifted))

ft_img_shifted.write_image(output_image)



