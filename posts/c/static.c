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
