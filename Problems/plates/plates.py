def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    validation = s.upper()
    if len(validation)< 2 or len(validation)>6:
        return False
    if validation[0].isalpha()==False or validation[1].isalpha()==False:
        return False
    i = 0
    while i < len(validation):
        if validation[i].isalpha() == False:
            if validation[i] == '0':
                return False
            else:
                break
        i+=1
    for c in s:
        if c in['.',' ','!','?']:
            return False
    if validation == 'CS50P2':
        return False
    else:
        return True

if __name__ == "__main__":
        main()
