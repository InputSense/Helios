# Imports are not necessary and not used in a running VG
# They are helpful with writing in the IDE for autocomplete
# You'd need to have the files in your working directory
from vg_helper import *  # Will autocomplete vg functions
from buttons import *    # Will autocomplete buttons


# Set script metadata
__title__ = 'Template'
__author__ = 'jaj'
__version__ = '1.0'


# config is optional, it creates the gui config interface is wanted
def config():
    pass

# init is optional, called first/once at runtime
# can print, create, set variables, etc
def init():
    print("Starting VG Template")


# main is required and runs the main loop
# do not use print statements or wait functions within the main loop
def main():

    if cv_ready():
        # evaluates True once per cv frame
        # receive cv_data from running cv script
        # always False if no cv script is running
        pass

    return


def my_combo():
    # all combos should be defined this way
    # to run them: combo_run(my_combo)
    # notice no parenthesis when calling combo run




