# haversine formula

球面上任意两点的中心角求解公式：  

$$
 hav(\frac{d}{r}) = hav(\phi_2 - \phi_1) + \cos(\phi_1)\cos(\phi_2)hav(\lambda_2 - \lambda_1) 
$$


# 问题讨论
现在想象一下这种情况：
1. 给定一个点 $$p$$ $$[lontitude, latitude]$$
2. 一个平面 $$P$$ 经过该点和地球球心
3. 经过点 $$p$$ 和平面 $$P$$ 与地球球面相切的直线 $$L_p$$ 
4. 经过点 $$p$$ 与 纬度 $$latitude$$ 所在圆相切的直线 $$L_lat$$
5. $$L_p$$ 与 $$L_lat$$ 夹角（锐角）为 $$theta$$
6. $$P$$ 与地球球面所切圆为 $$C$$
7. 从 $$p$$ 点出发，沿 $$C$$ 走 $$D$$ 之后，到达点 $$q$$

求 $$q$$ 的经纬度。

# 图例

* 中心角
  AOB 被称作中心角
  ![AOB](https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Sector_central_angle_arc.svg/320px-Sector_central_angle_arc.svg.png)



