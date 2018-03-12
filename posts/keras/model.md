# [model](https://keras.io/models/model/)

# train_on_batch
```
train_on_batch(self, x, y, sample_weight=None, class_weight=None)
```

- x: 训练数据，一个包含 Numpy 数组的列表。或者，在模型需要多种输入的时候，此时的 x 是一组 Numpy 数组。



# [Model visualization](https://keras.io/visualization/)
输出一个模型的结构图片，挺好用的。
```
from keras.utils import plot_model
plot_model(model, to_file='model.png')
```

# output

1. output 是什么？

```
from keras.models import Model
from keras.layers import Input, Dense

a = Input(shape=(32,))
b = Dense(32)(a)
model = Model(inputs=a, outputs=b)
```
在已经输入 a 的条件下，模型会将输出层 b 用到的所有用于计算的层包含进去。

> 如果 a 存在，则这一步会把所有与输入 a 和输出 b 相关和层连接起来。
> 为什么要写再次 `a(input)` 呢？




# 理解

1. keras 用起来不够直观。
