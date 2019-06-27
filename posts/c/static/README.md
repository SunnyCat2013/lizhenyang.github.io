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


# Reference
> https://www.geeksforgeeks.org/static-variables-in-c/
