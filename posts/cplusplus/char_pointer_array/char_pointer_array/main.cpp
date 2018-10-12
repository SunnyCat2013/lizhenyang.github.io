//
//  main.cpp
//  char_pointer_array
//
//  Created by 李振洋 on 2018/10/8.
//  Copyright © 2018年 李振洋. All rights reserved.
//

#include <iostream>
using namespace std;
/*
 
 */
int main(int argc, const char * argv[]) {
    // 该字符串是常量
    char *p = "Hello C Plus Plus";
    cout << p << endl;
    
    // 使用常量声明
    const char *q = "Hello const char pointer";
    cout << q << endl;
    
    // 在内存中分配存储空间
    char r[] = "Hello char array";
    cout << r << endl;
    return 0;
}
