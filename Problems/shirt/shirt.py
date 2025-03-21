from PIL import  Image, ImageOps
import sys
import PIL
def main():
    if sys.argv[3:]:
        print('Too many command-line arguments')
        sys.exit(1)
    name1, extention1 = sys.argv[1].split('.')
    name2, extention2 = sys.argv[2].split('.')
    try:
        elist = ['jpg','png','jpeg']
        if extention1 not in elist:
            sys.exit('Invalid input')
    except IndexError:
        print('Too few command-line arguments')
        sys.exit(1)
    if extention1 != extention2:
        sys.exit('Input and output have different extensions')
    try:
        image = Image.open(sys.argv[1])
        shirt = Image.open('shirt.png')
        imagef = ImageOps.fit(image,shirt.size)
        imagef.paste(shirt,(0,0),shirt)
        imagef.save(sys.argv[2])
    except FileNotFoundError:
        print('Could not read', sys.argv[1])
        sys.exit(1)






if __name__ == "__main__":
    main()
