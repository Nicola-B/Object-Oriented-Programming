#Nicola Batty
#17/06/2015
#Farm simulation radio buttons widget

from PyQt4.QtGui import *

class RadioButtonWidget(QWidget):
    #This class creates a group of radio buttons from a  given list of lables
    def __init__(self, label, instruction, button_list):
        super().__init__()

        #create widgets
        self.title_label = QLabel(label)
        self.radio_group_box = QGroupBox(instruction)
        self.radio_button_group = QButtonGroup()

        #Create the radio buttons
        self.radio_button_list = []
        for each in button_list:
            self.radio_button_list.append(QRadioButton(each))

        #set the defult checked item
        self.radio_button_list[0].setChecked(True)

        #create layout fot radio buttons and add them
        self.radio_button_layout = QVBoxLayout()

        #add buttons to the layout and butto group
        counter = 1
        for each in self.radio_button_list:
            self.radio_button_layout.addWidget(each)
            self.radio_button_group.addButton(each)
            self.radio_button_group.setId(each, counter)
            counter += 1

        #add radio butons to the goup box
        self.radio_group_box.setLayout(self.radio_button_layout)

        #create a layout fot whole widget
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.title_label)
        self.main_layout.addWidget(self.radio_group_box)

        #set the layout for this widget
        self.setLayout(self.main_layout)

    #method to find out the selected button
    def selected_button(self):
        return self.radio_button_group.checkedId()
