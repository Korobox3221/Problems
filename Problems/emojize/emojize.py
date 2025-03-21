import emoji
x = input()
if  ',' in x:
    hello, emojis = x.split(',')
    print(hello+','+emoji.emojize(emojis,language='alias'))
else:
    print(emoji.emojize(x,language='alias'))
