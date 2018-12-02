# `y = { 'ctc': lambda y_true, yy: 'hh' }` 这是个什么？

我一直以为中间那个 ", " 把这个 dict 分成了两个元素，但其实，它是 lambda 的一个参数的分隔。

```
    # the loss calc occurs elsewhere, so use a dummy lambda func for the loss
    model.compile(loss={'ctc': lambda y_true, y_pred: y_pred}, optimizer=sgd)
```
因为在 ctc 中计算了损失函数，所以，就使用了一个 lambda 函数来表示损失了。

# list




