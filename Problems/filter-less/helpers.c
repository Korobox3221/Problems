#include "helpers.h"
#include <math.h>
// Convert image to grayscale
void swap(BYTE *a, BYTE *b);
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{

    // Loop over all pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Take average of red, green, and blue
            int red = image[i][j].rgbtRed;
            int blue = image[i][j].rgbtBlue;
            int green = image[i][j].rgbtGreen;
            int average = round((red + green + blue) / 3.0);

            // Update pixel values
            image[i][j].rgbtRed = average;
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int originalRed = image[i][j].rgbtRed;
            int originalBlue = image[i][j].rgbtBlue;
            int originalGreen = image[i][j].rgbtGreen;
            int sepiaRed = round(.393 * originalRed + .769 * originalGreen + .189 * originalBlue);
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            int sepiaGreen = round(.349 * originalRed + .686 * originalGreen + .168 * originalBlue);
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            int sepiaBlue = round(.272 * originalRed + .534 * originalGreen + .131 * originalBlue);
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtBlue = sepiaBlue;
            image[i][j].rgbtGreen = sepiaGreen;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            swap(&image[i][j].rgbtRed, &image[i][width - 1 - j].rgbtRed);
            // Swap the green values
            swap(&image[i][j].rgbtGreen, &image[i][width - 1 - j].rgbtGreen);
            // Swap the blue values
            swap(&image[i][j].rgbtBlue, &image[i][width - 1 - j].rgbtBlue);
        }
    }

    return;
}
void swap(BYTE *a, BYTE *b)
{
    BYTE tmp = *a;
    *a = *b;
    *b = tmp;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    // Copy the original image to the copy array
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int pixels = 0;
            int amountr = 0;
            int amountg = 0;
            int amountb = 0;

            for (int m = i - 1; m < i + 2; m++)
            {
                for (int z = j - 1; z < j + 2; z++)
                {
                    if (m >= 0 && m < height && z >= 0 && z < width)
                    {
                        pixels++;
                        amountg += copy[m][z].rgbtGreen;
                        amountr += copy[m][z].rgbtRed;
                        amountb += copy[m][z].rgbtBlue;
                    }
                }
            }
            image[i][j].rgbtRed = round((float)amountr / pixels);
            image[i][j].rgbtGreen = round((float)amountg / pixels);
            image[i][j].rgbtBlue = round((float)amountb / pixels);
        }
    }

    return;
}
