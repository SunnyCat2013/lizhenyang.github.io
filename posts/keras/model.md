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
