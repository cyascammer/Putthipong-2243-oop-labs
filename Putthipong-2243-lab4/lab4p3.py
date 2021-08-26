'''
Putthipong Phukhansung
633040224-3
Problem 3
'''

from datetime import date


def get_year():
    correct_input = False
    while not correct_input:  # this is a while loop
        try:
            year = int(input(f"Enter the year you were born [1900, 2020]:"))
            if 1900 <= year <= 2020:
                return year
            else:
                print(f"Enter the year in the range [1900, 2020]")
                continue
        except ValueError:
            print("Please enter a valid floating point number")
        finally:
            print("Stay healthy!")


def compute_age(birth_year):
    cur_year = date.today().year
    return cur_year - birth_year


if __name__ == "__main__":
    b_year = get_year()
    print(f"You were born in {b_year}")
    age = compute_age(b_year)
    print(f"You are {age} years old")