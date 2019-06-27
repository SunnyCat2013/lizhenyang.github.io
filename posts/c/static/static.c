# include<stdio.h>

int runner()
{
    static int count = 0;
    count++;
    return count;
}

int main(void) {
    printf("Hello key word static in c!\n");

    printf("Runner: %d \n", runner());
    printf("Runner: %d \n", runner());
    printf("Runner: %d \n", runner());
    printf("Runner: %d \n", runner());
    return 0;
}
