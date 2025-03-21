x = input('File name: ').upper().replace(' ','')

def files():
    if x.endswith('.JPG') or x.endswith('.JPEG'):
        print('image/jpeg')
    elif x.endswith('.GIF'):
        print('image/gif')
    elif x.endswith('.PNG'):
        print('image/png')
    elif x.endswith('.PDF'):
        print('application/pdf')
    elif x.endswith('.TXT'):
        print('text/plain')
    elif x.endswith('.ZIP'):
        print('application/zip')
    else:
        print('application/octet-stream ')
files()
