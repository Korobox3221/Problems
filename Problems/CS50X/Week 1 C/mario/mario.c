#include <cs50.h>
#include <stdio.h>
int input(void);
void blocks(int n);
int main(void)
{
    int height = input();
    blocks(height);
}

int input(void)
{
    int x;
    do
        x = get_int("Height: ");
    while (x < 1 || x > 8);
    return x;
}
void blocks(int n)
{
    for (int x = 0; x < n; x++)
    {
        for (int i = n-1; i > x; i--)
        {
            printf(" ");
        }

        for (int y = 0; y <= x; y++)
        {
            printf("#");
        }
        printf("\n");
    }
}
