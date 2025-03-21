#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
bool only_digits(string s);
int main(int argc, string argv[])
{
    // Make sure program was run with just one command-line argument
    if (argc == 2&&only_digits(argv[1])==true)
    {
        // Convert argv[1] from a `string` to an `int`
        int key = atoi(argv[1]);
        // Prompt user for plaintext
        string plaintext = get_string("plaintext: ");
        printf("ciphertext: ");
        // For each character in the plaintext:
        for (int i = 0, len = strlen(plaintext); i < len; i++)
        {
            char c = plaintext[i];
            // Rotate the character if it's a letter
            if (isupper(plaintext[i]) && isalpha(plaintext[i]))
            {
                int alph = c - 'A';
                int index = (alph + key) % 26;
                c = index + 'A';
                printf("%c", c);
            }
            else if (islower(plaintext[i]) && isalpha(plaintext[i]))
            {
                int alph = c - 'a';
                int index = (alph + key) % 26;
                c = index + 'a';
                printf("%c", c);
            }
            else
            {
                printf("%c", c);
            }
        }
        printf("\n");
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}
// Make sure every character in argv[1] is a digit
bool only_digits(string s)
{
    int score = 0;
    int len = strlen(s);

    for(int i =0; i < len; i++)
    {
        if (isdigit(s[i]))
        {
            score++;
        }
    }
    if (score < len)
    {
        return false;
    }
    else
    {
        return true;
    }

}
