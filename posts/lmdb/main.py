# -*- coding: utf-8 -*-
# learning lmdb
import numpy as np
import lmdb

import glob

img_path = './image'

img_list = glob.glob('./image/*.jpg')
label_list = []

def readText(path):
    with open(path) as f:
        return f.read().strip()

for i in img_list:
    print i
    label = readText(i.replace('.jpg', '.txt'))
    label_list.append(label)
    print label

print len(img_list)
