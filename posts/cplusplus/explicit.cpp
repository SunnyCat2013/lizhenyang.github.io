#include <iostream>
using namespace std;

class A
{
public:
    //这里用explicit关键词来修饰类构造函数.
    explicit A(int i = 5, int j = 10)
    {
        m_a = i;
        m_b = j;
    }
//private:
    int m_a;
    int m_b;
};

int main()
{
    A s;
    //这样直接赋值,会被提示错误,因为explicit抑制隐式转换的进行
    // s = 10;//这样会报错!!!
    //当然显示转换还是可以的.
    s = A(20);
    cout << "m_a(20)" << s.m_a << endl;
    cout << "m_b(10)" << s.m_b << endl;

    system("pause");
    return 0;
}
// Reference: https://blog.csdn.net/qq_37233607/article/details/79051075 
