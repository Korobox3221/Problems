while True:
    try:
        n = int(input("Height: "))
        if n<1 or n>8:
            raise ValueError
    except ValueError:
        print("Not integer")
    else:
        break
x = n
for i in range(n):
    x = x-1
    print(" "*x+"#"*(i+1)+"  "+"#"*(i+1))






