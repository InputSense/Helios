# not a necessary import
# used for auto complete in IDEs
from vg_helper import *


def init():  # called first/once at runtime
    return


def main():  # loops indefinitely

    if cv_ready():
        # will evaluate True once per cv frame
        # to receive cv_data from running cv script
        # always False if no cv script is running
        pass

    return


