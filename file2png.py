#!/usr/bin/env python3
import sys

if sys.version_info.major != 3:
    raise Exception('Please run with python3')

from PIL import Image
from math import ceil
import struct


def file2img(fname):
    fdata = open(fname, 'rb').read()
    fdata = struct.pack('=I', len(fdata)) + fdata
    dim = ceil((len(fdata) / 3) ** 0.5)
    fdata = fdata + b'\x00' * (dim ** 2 * 3 - len(fdata))
    img = Image.frombytes('RGB', (dim,dim), fdata)
    return img


def file2png(fname):
    img = file2img(fname)
    tmp = fname.split('/')
    tmp[-1] = tmp[-1].replace('.', 'DOT')
    fname_png = '/'.join(tmp) + '.png'
    img.save(fname_png)
    return fname_png


fname = sys.argv[1]
fname_png = file2png(fname)
print('Created:', fname_png)
