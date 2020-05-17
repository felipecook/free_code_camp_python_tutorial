import random

feet_in_mile = 5280
meters_in_kilometer = 1000
members_of_the_beatles = ["John", "Paul", "Ringo", "George"]

def get_ext_name(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(number):
    return random.randint(1, number)