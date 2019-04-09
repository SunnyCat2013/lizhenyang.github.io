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
1. 通过计算的不可逆性，防止诈骗，保护商家（也就是说，计算能力一旦突破，就得重新更新算法）
2. routine escrow mechanisms（不知道怎么翻译）保护消费者
> Transactions that are computationally impractical to reverse would protect sellers
from fraud, and routine escrow mechanisms could easily be implemented to protect buyers. 


这个文章的方案：
为了解决传统的两方都要付出代价的交易模式，作者提出了一种 p2p 的解决方案。
这种方案使用一种 p2p 的带有时间戳的分布式服务器，产生一种验证交易先后顺序的计算出来的证明。

> In this paper, we propose a solution to the double-spending problem using a peer-to-peer distributed timestamp server to generate computational proof of the chronological order of transactions. 


保证这种系统安全的条件：
可信任的计算机结点控制的 CPU 计算能力大于不可信任的计算机结点的计算能力。

## 2. Transactions
区块链电子货币的本质：数字签名的数据链

> 拥有公钥的一方，是被拥有私钥的一方信任的。而拥有私钥的一方，其实是不被信任的。
```
我来思考一下这个通信过程，以 github 为例：
github 每天都会接收非常多信息，如果是我的用户名发过去的信息，github 会用我的公钥进行解密。如果能正确解密一个信息（比如，开头是“发给 github 的信”）说明，确实是我发的。
如果解密不对，那就说明受到了攻击。

此处要注意了，关键的点来了：
公钥虽然谁都可以拿到，但是，反推私钥的过程是当前计算能力无法在指定时间内完成的。这点由算法来保证！

另外一方面，我从 github 上 pull/clone 数据的时候，我作为一个人是相信 github 的。所以说，验证过程，是由我这个人来做的。因此，我不需要 github 的公钥。

```

double-spend 是一钱两花的意思？

目前对第二段的理解是，它给出了两个保证数字货币权限认证及交易合法性的点。
1. 对前面的交易区块进行数字加密(验证是谁的)
2. 用大多数结点，保证同一个区块的最旱的交易是合法的（验证谁是最早的，保证不会让前面的区块花给几个人。）。
3. mint 会给交易加一个时间戳，时间戳最早的交易被认为是合法的。同时整个系统的信任基础就是，我们相信 mint。我们信任 mint ，是因为它代表了大多数结点。这个前提如果都不可信的话，这个体系自然也就不可信了。

## 3. Timestamp Server
介绍了一下时间戳。
时间戳的存在，保证了数据的存在。
前面区块的 Hash 值与当前的区块，又可以给下次区块的交易提供新的 Hash 值。这样便形成了区块链。

## 4. Proof-of-Work
实现一个结点之间平等的时间戳服务系统。
> To implement a distributed timestamp server on a peer-to-peer basis,

## 5. Network

## 6. Incentive
区块的第一个交易都获得一个新的货币。那么，一个区块多大呢？
> The first transaction in a block is a special transaction that starts a new coin owned by the creator of the block.

奖励机制可以让有更多 CPU 的一方在为系统服务时，获利更多。
如果拥有更多的 CPU 去伪造前面的交易记录所获得的 bitcoin 要小于它为系统服务所获得的新的 bitcoin，那么它主动去攻击系统的意愿就不大。

## 7. Reclaiming Disk Space

## 8. Simplified Payment Verification
