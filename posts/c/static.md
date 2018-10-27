# static

1. 一个源文件的 static 变量只能被当前文件中的函数访问。感觉有些像 C++ 中的 private 变量。

```
// static.c
# include<stdio.h>
# include "friend.h"

int main(void) {
    printf("Hello key word static in c!\n");
    printStr();
    printf("I want to print %s in main file.", hello);
    return 0;
}

// friend.c
#include "friend.h"

static char* hello = "Hello static!";

void printStr(){
    printf("%s\n", hello);
}

// shell
gcc -Wall *.c -o out
static.c:7:48: error: use of undeclared identifier 'hello'; did you mean 'ftello'?
    printf("I want to print %s in main file.", hello);
                                               ^~~~~
```
