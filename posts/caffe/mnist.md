# 学习使用 caffe 训练 mnist 手写字体识别
http://caffe.berkeleyvision.org/gathered/examples/mnist.html

# 想要测试的点
- sigmoid 与 recitified linear unit 的分类效果的区别


# lenet 结构
a convolutional layer 
followed by a pooling layer
another convolution layer followed by a pooling layer
and then two fully connected layers 

caffe 中的模型在 $CAFFE_ROOT/examples/mnist/lenet_train_test.prototxt.
