#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
bool only_digits(string s);
int main(void)

{
    int i = 0;
    string hello = get_string("Text: ");
    char c = hello[i];
    int len = strlen(hello);
    printf("%i",isdigit(atoi(hello)));

}

