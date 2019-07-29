# include<stdio.h>

int runner()
{
    static int count = 0;
    count++;
    return count;
}
int runner_no_static()
{
    int count = 0;
    count++;
    return count;
}

int main(void) {
    printf("Hello key word static in c!\n");

    printf("Runner: %d \n", runner());
    printf("Runner: %d \n", runner());
    printf("runner_no_static: %d \n", runner_no_static());
    printf("runner_no_static: %d \n", runner_no_static());
    static int x;
    int y;
    printf("default static int: %d, normal int:%d", x, y);
    return 0;
}
