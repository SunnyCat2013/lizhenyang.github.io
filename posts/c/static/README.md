# static

1. 一个源文件的 static 变量只能被当前文件中的函数访问。感觉有些像 C++ 中的 private 变量。
感觉像是声明了一个全局变量。

```
# include<stdio.h>
# include "friend.h"

int runner()
{
    static int count = 0;
    count++;
    return count;
}

int main(void) {
    printf("Hello key word static in c!\n");
    printStr();

    printf("Runner: %d ", runner());
    printf("Runner: %d ", runner());
    printf("Runner: %d ", runner());
    return 0;
}
```
> Static variables have a property of preserving their value even after they are out of their scope!Hence, static variables preserve their previous value in their previous scope and are not initialized again in the new scope.

static 变量可以跨作用域保存值。并且，在跨域使用时，不会被重新初始化。

2. 静态变量被分配在段里，而不是在栈里
> Static variables are allocated memory in data segment, not stack segment. See memory layout of C programs for details.

3. 静态变量默认初始值是 0
> Static variables (like global variables) are initialized as 0 if not initialized explicitly. For example in the below program, value of x is printed as 0, while value of y is something garbage. See this for more details.

4. 静态变量只能用常量初始化
> In C, static variables can only be initialized using constant literals. For example, following program fails in compilation. See this for more details.

5. 在 C/C++ 里也可以使用静态变量和静态函数
> Static global variables and functions are also possible in C/C++. The purpose of these is to limit scope of a variable or function to a file.

# Q & A
1. 类中的 static 函数啥意思？






# Reference
> https://www.geeksforgeeks.org/static-variables-in-c/
