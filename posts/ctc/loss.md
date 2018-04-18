# loss of ctc

# 待解释

1. Lambda
2. ctc_lambda_func
# [tf.keras.backend.ctc_batch_cost](https://www.tensorflow.org/api_docs/python/tf/keras/backend/ctc_batch_cost)
先来看一下 tf 对这个函数的定义：
```
tf.keras.backend.ctc_batch_cost(
    y_true,
    y_pred,
    input_length,
    label_length
)
```
## 参数
```
y_true: tensor (样本数量, 最大字符长度) 样本标签。
y_pred: tensor (samples, 时间序列的长度, 字符的类别的数量) 时间序列的预测结果，或者是 softmax 结果。
input_length: tensor (samples, 1) 时间序列长度，和 y_pred 长度一致（毕竟一个时序输入，就有一个时序输出）。
label_length: tensor (samples, 1) 和 y_true 长度一致。

```




# 参考
[tf.keras.backend.ctc_batch_cost](https://www.tensorflow.org/api_docs/python/tf/keras/backend/ctc_batch_cost)
