cardi = input("Credit card number: ")
card = list(cardi)
sum = 0
length = len(card)
print(length)
one = 1


for i in range(length):
    try:
        index_length = length - one
        last = int(card[index_length])
        str_last = str(last*2)


        if index_length == length -1:
            sum = sum +last
        elif one % 2 == 0:
            if last*2>9:
                sum = sum +int(str_last[0])+ int(str_last[1])
            else:
                sum = sum + last*2


        else:
            sum = sum+last
        one+=1

    except IndexError:
        on = 0
print(sum)
ssum = str(sum)
fn = int(card[0])
sn = int(card[1])
if ssum[1]=="0":
    if length ==15:
        if fn ==3:
            if sn == 4 or sn == 7:
                print("AMEX")
            else:
                print("INVALID")
        else:
            print("INVALID")
    elif length== 16:
        if fn== 5:
            if sn ==1 or sn ==2 or sn ==3 or  sn ==4 or  sn ==5:
                print("MASTERCARD")
            else:
                print("INVALID")
        elif fn == 4:
            print("VISA")
        else:
            print("INVALID")


    elif length ==13:
        if fn == 4:
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")
else:
    print("INVALID")
