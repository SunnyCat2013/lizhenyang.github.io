# Synthetic Data for Text Localisation in Natural Images

http://www.robots.ox.ac.uk/~vgg/data/scenetext/
http://www.robots.ox.ac.uk/~vgg/data/scenetext/gupta16.pdf

1. 将文字通过图片深度信息，把文字印在图片中
2. 文字检测


## 文字合成 pipeline
1. 选择合适背景图片和文字。
    - 文字分成，字、句子和段落三个层次。
    - 图片本身不包含文字
2. 使用[contour detector](https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/papers/amfm_pami2010.pdf) 把图片分成一系列连续的区域。
    - 背景：In real images, text tends to be contained in well defined regions.
    - 策略：使用颜色和背景比较一致的图片区域
    - 过滤：区域太小不要；背景纹理过复杂不要；与视觉正交的不要；宽高比例不同的不要。
3. 获取像素点的深度信息[a dense pixel-wise depth map](https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Liu_Deep_Convolutional_Neural_2015_CVPR_paper.pdf)
4. Then, for each contiguous region a local surface normal is estimated.
5. 使用 [Poisson image editing](https://www.cs.virginia.edu/~connelly/class/2014/comp_photo/proj2/poisson.pdf) 根据 local surface orientation 把文字融合到背景中。
    - 颜色选择：使用 K-means 从 IIT5K 中学习出一系列 <background color, text color> 数据对。知道待插入文字的背景的颜色之后，就可以知道文字颜色了。
