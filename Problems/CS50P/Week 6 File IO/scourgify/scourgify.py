import sys
import csv
names = []
house = []
def main():
    if sys.argv[3:]:
        print('Too many command-line arguments')
        sys.exit(1)
    try:
        if not sys.argv[1].endswith('.csv'):
            print('Not a CSV file')
            sys.exit(1)
    except IndexError:
        print('Too few command-line arguments')
        sys.exit(1)
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                names.append( row[0].replace(' ','').split(','))
                house.append(row[1])
            names.pop(0)
            house.pop(0)
                #house.pop(0)
        fname = [i[1] for i in names]
        lname = [i[0] for i in names]
        with open(sys.argv[2], 'w', newline='') as csvfile:
            fieldnames = ['first', 'last','house']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for length in names:
                writer.writerow({'first':fname[0],'last':lname[0],'house':house[0]})
                fname.pop(0)
                lname.pop(0)
                house.pop(0)
    except FileNotFoundError:
        print('Could not read',sys.argv[1])
        sys.exit(1)
    except Exception:
        print('Too many command-line arguments')
        sys.exit(1)


if __name__ == '__main__':
    main()
