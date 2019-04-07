# A Peer to Peer Electronic Money System

## Abstract
最长链（The longest chian）是关键

1. Proof of the sequence of events witnessed
2. Proof that it came from the largest pool of CPU power

## Introduction

### 第一段
电子商务几乎都要用可信用的第三方作为支付中介。

但是，这种模式有一些缺点。

第一点（其实不太理解）买卖过程中会有纠纷，所以完成一次交易之后，这个交易还是可能被交易的双方拿出来重新更改。我猜这样会增加很多成本，同时在对账、还原交易信息的时候，就会变得极少不容易。（所以才需要做成不可逆的账本？）
> Completely non-reversible transactions are not really possible, since financial institutions cannot
avoid mediating disputes.

纠纷的存在的缺点：
1. 增大了交易成本
2. 使小额交易变得不可能（因为交易成本已经大于交易额了）


交易可逆性的缺点：
在一个提供不可逆的服务中，交易可塑带来的成本更大。
首先是信任成本变高。商家不得不谨慎验证它们的用户，让用户提供更多的证明材料。
同时，一定比例的错误是认为可以被接受的。

现在交易就可以避免上述问题。
想一想也对，如果面对面交易就不用给第三方交易费了，省了一笔钱。
同时，因为没有中介费，小额的交易也可以进行。

> 设想一下，如果小额交易也可以低成本，甚至 0 成本地进行？？！
> 小额交易的需求有哪些？

### 第二段
一个基于密码学的验证系统可以很好地替代信任模式。

保护交易双方的方式如下：
> Transactions that are computationally impractical to reverse would protect sellers
from fraud, and routine escrow mechanisms could easily be implemented to protect buyers. 
