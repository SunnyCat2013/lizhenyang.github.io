# C 移动指针，C++ 使用 iterator

```
// Runtime: 4 ms
bool judgeCircle(char* moves) {
    int x = 0, y = 0;
    while(*moves != '\0') {
        char c = *moves;
        if(c == 'U')
            y++;
        else if(c == 'L')
            x++;
        else if(c == 'D')
            y--;
        else
            x--;
        moves++;
    }
    return x == 0 && y == 0;
}
```

```
// Runtime: 12 ms
class Solution {
public:
    bool judgeCircle(string moves) {
        int x = 0, y = 0;
        for(char c: moves) {

            if(c == 'U')
                y++;
            else if(c == 'L')
                x++;
            else if(c == 'D')
                y--;
            else
                x--;

        }
        return x == 0 && y == 0;
    }
};
```
