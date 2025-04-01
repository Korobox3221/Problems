import datetime
import sys
from calendar import month
from datetime import date
import  inflect

p = inflect.engine()
class Dates:
    def __init__(self,day):
        self.day = day


    def __str__(self):
        return self.day
    def __sub__(self, other):
        day = self.day - other.day
        return Dates(day)

        #@classmethod
        #def get(cls):
            #year, month, day = input().split('-')
            #return cls(year,month,day)



def main():
    print(wordnumbers(input('Date of Birth: ')))
def wordnumbers(s):
    try:
        today = date.today()
        razdel = s
        year, month, day = razdel.split("-")
    except ValueError:
            sys.exit('Invalid date')
    else:
        #yeart,montht,dayt = today.split('-')
        birthday = date(int(year),int(month),int(day))

        diff = today - birthday
        days = int(diff.days)*24*60
        words = p.number_to_words(days,andword="")
        return f'{words.capitalize()} minutes'
        #print(birthday)
        #print(year)
        #print(date.today().timetuple())
        #print(datetime.time())

if __name__ == "__main__":
    main()










