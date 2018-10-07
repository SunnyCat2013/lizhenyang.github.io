//
//  main.cpp
//  polymorphism
//
//  Created by 李振洋 on 2018/10/6.
//  Copyright © 2018年 李振洋. All rights reserved.
//

#include <iostream>
using namespace std;

class Shape {
protected:
    int width, height;
public:
    Shape( int a=0, int b=0)
    {
        width = a;
        height = b;
    }
    virtual int area() = 0;
//    virtual int area()
//    {
//        cout << "Parent class area :" <<endl;
//        return 0;
//    }
};
class Rectangle: public Shape{
public:
    Rectangle( int a=0, int b=0):Shape(a, b) { }
    virtual int area ()
    {
        cout << "Rectangle class area :" <<endl;
        return (width * height);
    }
};
class Triangle: public Shape{
public:
    Triangle( int a=0, int b=0):Shape(a, b) { }
    virtual int area ()
    {
        cout << "Triangle class area :" <<endl;
        return (width * height / 2);
    }
};
class Square: public Rectangle{
public:
    // shape 的儿子类的 area 是虚函数吗？如果是，那么在孙子类 Square 中应该可以覆盖。
    Square(int a, int b): Rectangle(a, b) {}
    int area (int a) {
        cout << "Square class area" << endl;
        return width;
    }
};
// 程序的主函数
int main( )
{
    Shape *shape;
    Rectangle rec(10,7);
    Square squ(10, 7);
    Triangle  tri(10,5);
    
    // 存储矩形的地址
    shape = &rec;
    // 调用矩形的求面积函数 area
    shape->area();
    
    // 存储三角形的地址
    shape = &tri;
    // 调用三角形的求面积函数 area
    shape->area();
    
    shape = &squ;
    shape->area(); // 预测：Square class area
    
    Rectangle * rectangle;
    rectangle = &squ;
    rectangle->area();
    
    return 0;
}
