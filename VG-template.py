# not a necessary import
# used for auto complete in IDEs
from vg_helper import *

# set script metadata
__title__ = 'Template'
__author__ = 'jaj'
__version__ = '1.0'


def init():  # called first/once at runtime
    return


def main():  # loops indefinitely

    if cv_ready():
        # evaluates True once per cv frame
        # receive cv_data from running cv script
        # always False if no cv script is running
        pass

    return



