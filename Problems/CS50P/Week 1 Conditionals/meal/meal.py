def main():
    answer = input('What time is it? ')
    time = convert(answer)
    if 7.00 <= time <= 8.0:
        print('breakfast time')
    elif 12.00 <= time <= 13.0:
        print('lunch time')
    elif 18.00 <= time <= 19.0:
        print('dinner time')


def convert(time):
    hours,minutes = time.split(':')
    return float(hours) + (float(minutes)/60)


if __name__ == "__main__":
    main()
