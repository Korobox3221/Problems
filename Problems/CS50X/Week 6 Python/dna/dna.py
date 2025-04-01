import csv
import sys


def main():
    # TODO: Check for command-line usage
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

    # TODO: Read database file into a variable
    rows = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(row)

        s_txt = []
        with open(sys.argv[2]) as file:
            txt_reader = file.read()
            s_txt.append(txt_reader)

        sequences = []
        for i in range(len(reader.fieldnames)):
            sequences.append(longest_match(s_txt[0], reader.fieldnames[i]))
        sequences.pop(0)
        # sequences = [{'AGATC': sequences[0], 'TTTTTTCT': sequences[1], 'AATG': sequences[2], 'TCTAG': sequences[3], 'GATA': sequences[4], 'TATC': sequences[5], 'GAAA': sequences[6], 'TCTG': sequences[7]}]
        fieldnames = reader.fieldnames
        fieldnames.pop(0)
        find = 0
        for d in rows:
            seq_score = 0
            for i in range(len(fieldnames)):
                if int(d[fieldnames[i]]) == int(sequences[i]):
                    seq_score += 1
                    if seq_score == len(fieldnames):
                        print(d['name'])
                        find += 1
        if find == 0:
            print("No match")
    except FileNotFoundError:
        print('Could not read', sys.argv[1])
        sys.exit(1)
    except Exception:
        print('Too many command-line arguments')
        sys.exit(1)


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
