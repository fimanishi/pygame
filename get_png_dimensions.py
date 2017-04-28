#!/usr/bin/env python3

import struct

def get_image_info(data):

    w, h = struct.unpack('>LL', data[16:24])
    width = int(w)
    height = int(h)

    return width, height



def png_info(FILENAME):
    with open(FILENAME, 'rb') as f:
        data = f.read()
    return get_image_info(data)
