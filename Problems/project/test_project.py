from project import Dates,days_left,style_choice,figlet,num_to_words
from datetime import date
import pytest
damich_date = date(2025,11,18)- date.today()
cl_date = date(2025,5,31)- date.today()
ny_date = date(2025,1,1)- date.today()
bd_date = date(2025,3,13)- date.today()
vac_date = date(2025,1,24) - date.today()
def test_days_left():
    assert days_left('1') == damich_date.days
    assert days_left('2') == bd_date.days
    assert days_left('3') == ny_date.days
    assert days_left('4') == cl_date.days
    assert days_left('5') == vac_date.days
def test_days_left_error():
    with pytest.raises(ValueError):
        days_left('6')
def test_figlet():
    assert figlet('172') == (' __ ______ ___        _                   _       __ _   \n'
 '/_ |____  |__ \\      | |                 | |     / _| |  \n'
 ' | |   / /   ) |   __| | __ _ _   _ ___  | | ___| |_| |_ \n'
 ' | |  / /   / /   / _` |/ _` | | | / __| | |/ _ \\  _| __|\n'
 ' | | / /   / /_  | (_| | (_| | |_| \\__ \\ | |  __/ | | |_ \n'
 ' |_|/_/   |____|  \\__,_|\\__,_|\\__, |___/ |_|\\___|_|  \\__|\n'
 '                               __/ |                     \n'
 '                              |___/                      \n')
    assert figlet('123') == (' __ ___  ____        _                   _       __ _   \n'
 '/_ |__ \\|___ \\      | |                 | |     / _| |  \n'
 ' | |  ) | __) |   __| | __ _ _   _ ___  | | ___| |_| |_ \n'
 ' | | / / |__ <   / _` |/ _` | | | / __| | |/ _ \\  _| __|\n'
 ' | |/ /_ ___) | | (_| | (_| | |_| \\__ \\ | |  __/ | | |_ \n'
 ' |_|____|____/   \\__,_|\\__,_|\\__, |___/ |_|\\___|_|  \\__|\n'
 '                              __/ |                     \n'
 '                             |___/                      \n')

    assert figlet('38') == (' ____   ___        _                   _       __ _   \n'
 '|___ \\ / _ \\      | |                 | |     / _| |  \n'
 '  __) | (_) |   __| | __ _ _   _ ___  | | ___| |_| |_ \n'
 ' |__ < > _ <   / _` |/ _` | | | / __| | |/ _ \\  _| __|\n'
 ' ___) | (_) | | (_| | (_| | |_| \\__ \\ | |  __/ | | |_ \n'
 '|____/ \\___/   \\__,_|\\__,_|\\__, |___/ |_|\\___|_|  \\__|\n'
 '                            __/ |                     \n'
 '                           |___/                      \n')

def test_num_to_words():
    assert num_to_words('232') == 'Two hundred thirty-two days left'
    assert num_to_words('99') == 'Ninety-nine days left'
    assert num_to_words('11') == 'Eleven days left'

