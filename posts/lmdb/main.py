# -*- coding: utf-8 -*-
# learning lmdb
import numpy as np
import lmdb

import glob

img_path = './image'

img_list = glob.glob('./image/*.jpg')
for i in img_list:
    print i

