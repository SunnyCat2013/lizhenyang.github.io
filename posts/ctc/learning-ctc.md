# Connectionist Temporal Classification
> 因为最近做了一些用连续标签做文字识别标签任务的工作，对 ctc 有了一些了解，在此记录一下。

在学习 CTC 的时候，也看了不少博客，但是我觉得讲的最好的还是原论文 [Connectionist Temporal Classification: Labelling Unsegmented Sequence Data with Recurrent Neural Networks](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.75.6306&rep=rep1&type=pdf) 解释的最清楚。
对于没接触过这个概念的人，可能加一些例子会更好理解一些。
我就来加一些例子。

# 背景知识
用实例来说，我们在做 ocr 工作时，我们希望给一行文字的图片让机器识别出来这个图片里面的文字。
语音识别任务中，给了一段语音片段，我们希望能把这段语音识别成可编辑的文字。
但是，在对每个片段进行分类模型训练之前，需要对每个训练样本进行切割标注。
这是项非常繁琐的工作非常不利于模型的训练。

下面是个对文字进行标注的工具，大家可以看一下。如果我们在做文字识别工作时，对每个文字都要明确标出这个字在图片中的位置、高、宽，这将会是一个多么巨大的工作量。

![jtessboxeditor](http://vietocr.sourceforge.net/training.html)
