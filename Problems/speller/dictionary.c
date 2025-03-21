// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <cs50.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"
int words = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = sizeof(node);

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int i = hash(word);
    node * current = table[i];
    while(current != NULL)
    {
      if  (strcasecmp(current->word, word)==0)
        {
            return true;


        }
        current = current->next;



    }
    return false;


}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int hash = 0;
    for (int i = 0; i<strlen(word); i++)
    {
        hash =(hash*31) + toupper(word[i]);

    }
    return hash % N;

}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
     for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }
    // Open the dictionary file
    char buffer[LENGTH + 1];
    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
    {
        printf("Could not open file.\n");
        return false;

    }

    // Read each word in the file

    while(fscanf(source, "%s", buffer ) != EOF)
    {
        // Add each word to the hash table
        node*n = malloc(sizeof(node));
        if (n==NULL)
        {
            printf("Memory allocation failed.\n");
            return false;
        }
        strcpy(n->word, buffer);

        int index = hash(n->word);
        n->next = table[index];
        table[index] = n;
        words++;

    }




    // Close the dictionary file
    fclose(source);
    printf("Total words loaded: %i\n", words);;

    return true;


}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{


    return words;
}


// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for( int i = 0; i<N;i++)
    {
        node * current = table[i];
        while(current != NULL)
        {
        node * tmp = current;
        current = current->next;
        free(tmp);


        }

    }

    return true;
}

