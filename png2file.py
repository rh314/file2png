#!/usr/bin/env python3
import sys

if sys.version_info.major != 3:
    raise Exception('Please run with python3')

from PIL import Image
import struct


def img2data(img):
    data = img.tobytes()
    data_len = struct.unpack('=I', data[:4])[0]
    data = data[4: 4 + data_len]
    return data


def png2file(fname_png):
    assert fname_png.endswith('.png')
    img = Image.open(fname_png)
    tmp = fname_png.split('/')
    tmp[-1] = tmp[-1][:-4].replace('DOT', '.')
    fname = '/'.join(tmp)
    data = img2data(img)
    with open(fname, 'wb') as f:
        f.write(data)
    return fname


fname_png = sys.argv[1]
fname = png2file(fname_png)
print('Created (from PNG):', fname)
