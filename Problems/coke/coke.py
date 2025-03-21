x = int(input('Insert coin: '))

def main():
    amount_due = 50 - x
    while amount_due > 0:
        if x == 30:
            return print('Amount Due: '+str(50))
        print('Amount Due: '+str(amount_due))

        amount_due = amount_due - int(input('Insert coin: '))

    else:
        return print('Change Owed: '+str(abs(amount_due)))

main()
