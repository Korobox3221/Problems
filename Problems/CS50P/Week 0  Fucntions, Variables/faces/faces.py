def convert():
    Hi = input(': ')
    Hi = Hi.replace(':)','🙂')
    Hi = Hi.replace(':(', '🙁')
    return Hi

def main():
    print(convert())
main()
