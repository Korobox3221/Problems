#include <stdio.h>

int main(void)
{
    char s[50] = "this is a string";

    puts( s );

    size_t n = 0;
    char *p = s;

    do
    {
        if ( *p == ' ' ) ++n;
    } while ( *p++ );

    for ( char *q = p + n; q != p; )
    {
        if ( *--p == ' ' ) *--q = ' ';
        *--q = *p;
    }

    puts( s );

    return 0;
}
