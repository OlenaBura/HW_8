from datetime import datetime
import sys


def correct_path():

    try:
        sys.argv[1] == 'print'
    except IndexError:
        sys.exit("You must write the word 'print'")

    if sys.argv[1] != 'print':
        sys.exit("You must write only the word 'print'")


def get_dict_birth(users):

    n_number_week = datetime.now().strftime('%W')

    for i in range(len(users)):

        b_week_day = users[i]['birthday'].weekday()
        b_number_week = users[i]['birthday'].strftime('%W')
        delta_week = int(b_number_week) - int(n_number_week)

        if delta_week == 1 and (str(b_week_day) != 5 and str(b_week_day) != 6):
            for k, v in dict_help.items():
                if b_week_day in v:
                    dict_birth[k].append(users[i]['name'])
        elif delta_week == 0 and (str(b_week_day) == 5 or str(b_week_day) == 6):
            for k, v in dict_help.items():
                if b_week_day in v:
                    dict_birth[k].append(users[i]['name'])
        else:
            continue

    return dict_birth


def result(dict_birth):

    for k, v in dict_birth.items():
        print('' if v == [] else f"{k}: {', '.join(v)}")


def get_birthdays_per_week():

    correct_path()
    dict_birth = get_dict_birth(users)
    result(dict_birth)


if __name__ == '__main__':
    users = [{'name': 'Olena', 'birthday': datetime(year=(datetime.now()).year, month=2, day=8)},
         {'name': 'Dmytro', 'birthday': datetime(year=(datetime.now()).year, month=2, day=3)},
         {'name': 'Julia', 'birthday': datetime(year=(datetime.now()).year, month=2, day=1)},
         {'name': 'Olga', 'birthday': datetime(year=(datetime.now()).year, month=2, day=5)},
         {'name': 'Sergiy', 'birthday': datetime(year=(datetime.now()).year, month=11, day=21)},
         {'name': 'Amanda', 'birthday': datetime(year=(datetime.now()).year, month=1, day=28)},
         {'name': 'Adam', 'birthday': datetime(year=(datetime.now()).year, month=2, day=4)},
         {'name': 'Jane', 'birthday': datetime(year=(datetime.now()).year, month=2, day=3)}]
    dict_birth = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
    dict_help = {'Monday': [5, 6, 0], 'Tuesday': [1], 'Wednesday': [2], 'Thursday': [3], 'Friday': [4]}
    get_birthdays_per_week()
