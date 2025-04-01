def main():
    main_text = str(input("Text: "))
    letters = float(count_letters(main_text))
    words = float(count_words(main_text))
    sentences = float(count_sentences(main_text))
    L = float(letters / words * 100)
    S = float(sentences / words * 100)
    index = float(0.0588 * L - 0.296 * S - 15.8)
    grade = round(index)
    print(letters,words,sentences)
    if grade<1:
        print("Before Grade 1")
    elif grade>16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")






def count_letters(text):
    text = list(text)
    score = 0
    for i in range(len(text)):
        if text[i].isalpha():
            score+=1
    return score



def count_words(text):
    text = text.split()
    score =0
    for i in range(len(text)):
        if text[i] in text:
            score+=1
    return score


def count_sentences(text):
    text = list(text)
    score = 0
    for i in range(len(text)):
        if str(text[i])=='?'or str(text[i])=='.'or str(text[i])=='!':
            score += 1
    return score

main()
