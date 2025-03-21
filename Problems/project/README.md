# Important dates
### [Video Demo](https://www.youtube.com/watch?v=q2NBCCHFJbk)
## Description:
This program prompts the user to select one of the  given dates. After that, the program will prompt the user with one of 3 "styles". Each "style" is a different format in which the amount of days left before the given date will be printed.
### How does the Program Work?
The Program utilizes the python built-in library `Datetime` and imports `date` objects.
To acquire the current local date, `.today()` class method from `date` was used which has `.days` instance attribute.
The calculations of the amount of days left before the given date are based on subtracting the `.today()` object from the given `date` object and with the help of `.days` instance attribute we can see the number that we need to be printed.


The user is asked to choose from three "styles": "Regular","FIGlet" and "Numbers to words"
The Program also utilizes libraries `pyfiglet` and `inflect` to be used in two of the given print "styles".


`pyfiglet` library is utilized to print the  amount of days left in the FIGlet ASCII art style. `inflect` library is utilized for the `.number_to_words` method to print the number of days left in the form of words.


Besides that, the program utilizes the `tabulate` library to print given dates and style 'variants' in table format.

### Installation
It's recommended to first create a python virtual environment and then install the requirements with the following command:
```
$ pip install -r requirements.txt
```
Then run the command:
```
python project.py
```
### Tech used

Python 3.12

### Main files
- project.py - main file with the program

- test_project.py - three tests of the main program's functions
