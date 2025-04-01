#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Prompt the user for some text
    string text = get_string("Text: ");

    // Count the number of letters, words, and sentences in the text
    float letters = count_letters(text);
    float words = count_words(text);
    float sentences = count_sentences(text);
    float L = letters / words * 100;
    float S = sentences / words * 100;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int grade = round(index);
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }

    // Compute the Coleman-Liau index

    // Print the grade level
    // printf("%f\n",sentences);
}
int count_letters(string text)

{
    int score = 0;

    for (int i = 0, len = strlen(text); i < len; i++)
    {

        if (isalpha(text[i]))
        {
            score++;
        }
    }
    return score;
}

int count_words(string text)
{
    // Return the number of words in text
    int score = 0;

    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (isblank(text[i]))
        {
            score++;
        }
    }
    return score + 1;
}

int count_sentences(string text)
{
    int score = 0;

    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] == '?' || text[i] == '.' || text[i] == '!')
        {
            score++;
        }
    }
    return score;
}
