#include <cs50.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    char buff[50];
    FILE *img = NULL;


    int num_file = 0;
    // Accept a single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open the memory card
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // Create a buffer for a block of data
    uint8_t buffer[512];
    bool first_file = true;

    // While there's still data left to read from the memory card
    while (fread(buffer, 1, 512, card) == 512)
    {



        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {

            if (img != NULL)
            {
                fclose(img);
            }

            sprintf(buff, "%03i.jpg", num_file);
            img = fopen(buff, "w");
            if (img == NULL)
            {
                printf("Could not open file.\n");
                return 1;
            }
            num_file++;
        }
        if (img != NULL)
        {
            fwrite(buffer, 1, 512, img);
        }

        // Create JPEGs from the data
    }
    printf("%i\n", num_file);
}
