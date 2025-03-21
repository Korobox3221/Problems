from datetime import date
from pyfiglet import Figlet
import  inflect
from tabulate import  tabulate
# Contains all the  important dates
class Dates:
    def __init__(self,damich=date(2025,11,18),cl = date(2025,5,31),birthday=date(2025,3,13),
                 new_year=date(2025,1,1), vacation=date(2025,1,24)):
        self.damich = damich
        self.cl = cl
        self.birthday = birthday
        self.new_year = new_year
        self.vacation = vacation
        #Figlet font
        self.fig_font='big'
        #Lists of date and style choices for tabulate
        self.date_list = [["1."," Damir comes back from army"],["2."," My birthdate"],
                          ["3."," New Year"],["4."," Champion's league final"], ["5."," Vacation"]]
        self.style_choices_list = [["1."," Regular"],["2."," FIGlet"],["3."," Numbers to words"]]
        self.headers = [['Important dates'],['$tyle$']]
dates = Dates()
# Prints dates choices in table format
def main():
    while True:
        try:
            print(tabulate(dates.date_list,dates.headers[0],tablefmt='grid'))
            date_choice = input('Select a date: ').strip()
            if date_choice == '1'or date_choice == '2' or date_choice == '3' or date_choice == '4'or date_choice == '5':
               break
            else:
                raise ValueError
        except ValueError:
            print('Choose a number from the ones below!')
    days = days_left(date_choice)
    print(style_choice(days))
# Returns the amount of days left
def days_left(n):
    if n == '1':
        days_left_damich = dates.damich - date.today()
        return days_left_damich.days
    if n == '2':
        days_left_birthday = dates.birthday - date.today()
        return days_left_birthday.days
    if n == '3':
        days_left_new_year = dates.new_year - date.today()
        return days_left_new_year.days
    if n == '4':
        days_left_cl = dates.cl - date.today()
        return days_left_cl.days
    if n == '5':
        days_left_vac = dates.vacation - date.today()
        return days_left_vac.days
    else:
        raise ValueError
# Prints style choices in table format and returns a string
def style_choice(s):
    while True:
            try:
                print(tabulate(dates.style_choices_list,dates.headers[1],tablefmt='grid'))
                style_choice = input('Select a style: ').strip()
                if style_choice == '1':
                    return str(s)+' days left'
                elif style_choice == '2':
                    return figlet(s)
                elif style_choice == '3':
                    return num_to_words(s)
                else:
                    raise ValueError
            except ValueError:
                print('Choose a number from the ones below!')
# Returns a string in Figlet format
def figlet(s):
    figlett = Figlet()
    figlett.getFonts()
    figlett.setFont(font=dates.fig_font)
    return figlett.renderText(str(s)+' days left')
# Returns a string in number to words format
def num_to_words(s):
    p = inflect.engine()
    words = p.number_to_words(s,andword='')
    return words.capitalize()+' days left'


if __name__ == "__main__":
    main()
