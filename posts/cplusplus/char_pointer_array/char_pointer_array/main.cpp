//
//  main.cpp
//  char_pointer_array
//
//  Created by 李振洋 on 2018/10/8.
//  Copyright © 2018年 李振洋. All rights reserved.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    char *p = "Hello C Plus Plus";
    cout << p << endl;
    
    const char *q = "Hello const char pointer";
    cout << q << endl;
    
    char r[] = "Hello char array";
    cout << r << endl;
    return 0;
}
