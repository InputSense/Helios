from vg_helper import *
from buttons import *


__title__ = 'Config Example'
__author__ = 'jaj'
__version__ = 1.0


def config():
    label('CONFIGURATION EXAMPLE', 'This is an example of how to use the configuration widgets to assign values to global variables in user scripts.')

    mem.face_buttons = checkbox('My Checkboxes',
                                "Use 'checkbox' for features that can be enabled or disabled inclusively to each other.",
                                ['inclusive feature 1', 'inclusive feature 2', 'inclusive feature 3', 'inclusive feature 4'],
                                default_selection=[0, 1, 2])  # You can set the default selected checkboxes as an int, list, or tuple

    mem.dpad_buttons = radiobox(title='My Radio Button',
                                description="Use 'checkbox' for features that can be enabled or disabled exclusively to each other.",
                                items=['exclusive feature 1', 'exclusive feature 2', 'exclusive feature 3', 'exclusive feature 4'],
                                default_selection=1)

    mem.combo_box_value = combobox('My Combo Box',
                                   "Use 'comboBox' for features with many different exclusive options.",
                                   ['combobox feature 1', 'combobox feature 2', 'combobox feature 3', 'combobox feature 4', 'combobox feature 5', 'combobox feature 6'])

    mem.spinbox_value = spinbox('My Spinbox',
                                description="Use 'spinBox' when it is desired the user type a numeric value. The value can be positive or negative within a predetermined range."
                                            "Numerical features all allow min, max, step, and default parameters",
                                minimum=10,
                                maximum=50,
                                default_value=36,
                                step=2)

    mem.double_spinbox_value = floatspinbox('My Float Spinbox',
                                            description="The 'floatSpinBox' is the same as the 'spinbox', but for numeric values with decimal portion."
                                                        "The float spinbox also allows a decimal parameter",
                                            minimum=-1.0,
                                            maximum=1.0,
                                            default_value=0.0,
                                            step=0.01,
                                            decimals=2)

    mem.slider_value = slider('My Slider',
                              description="Use 'slider' to configure numeric parameters. The numeric value can be positive or negative within a predetermined range.")

    mem.vslider_value = slider('My V Slider',
                               description="The slider can also have a vertical orientation, set with the 'orientation' parameter",
                               orientation='vertical',
                               minimum=100,
                               maximum=500)

    mem.dial_value = dial('My Dial', "The 'dial' is similar to 'slider', but in a circular knob shape.")

    mem.catalog_values = catalog("My Catalog",
                                 description="Use 'catalog' for features which can be enabled inclusively or exclusively of each other. Multi or single select of features can be set using the 'multi' parameter. Catalog has no default selection",
                                 items=['list item 1', 'list item 2', 'list item 3', 'list item 4', 'list item 5'])


def init():
    print("Config Example Started")


def main():

    if event_active(BUTTON_5):  # On RT press event, the faces combo is run to test the checkbox/button feature
        combo_run(faces)

    if get_actual(BUTTON_8):  # Press or hold LT to test the radiobox/dpad feature
        set_val(mem.dpad_buttons+9, 100)


    set_val(STICK_1_X, mem.spinbox_value)
    set_val(STICK_1_Y, mem.double_spinbox_value)


def faces():

    # set_val_for takes a tuple or an array of tuples
    # Therefore we will create the array of tuples based on selected buttons

    buttons = []

    for i, button in enumerate(mem.face_buttons):
        # for each button we need to see if it is true, and if so append a tuple of (button, 100) to the list or array
        if button:
            buttons.append((i + 13, 100))

    set_val_for(buttons, duration=200)  # all selected face buttons are now set for 200ms





