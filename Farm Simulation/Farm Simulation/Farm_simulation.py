#Nicola Batty
#30/07/2015
#Farm simulation field simulation

import sys
import random

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Farm_simulation_graphic_field_scene_class import *
from Farm_simulation_graphic_wheat_item_class import *
from Farm_simulation_graphic_potato_item_class import *
from Farm_simulation_graphic_cow_item_class import *
from Farm_simulation_graphic_sheep_item_class import *
from Farm_simulation_graphic_drag_label_class import *
from Farm_simulation_field_manual_grow_dialog_class import *

class FieldWindow(QMainWindow):
    #This class creates a main window to observe the growth of a simulated field

    #constructer
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Field Simulation")

        #create toolbars
        self.crop_tool_bar = QToolBar()
        self.animal_tool_bar = QToolBar()

        #create toolbar labels
        self.wheat_label = WheatDragLabel()
        self.wheat_label.setToolTip("Add wheat")
        
        self.potato_label = PotatoDragLabel()
        self.potato_label.setToolTip("Add potato")

        self.cow_label = CowDragLabel()
        self.cow_label.setToolTip("Add cow")

        self.sheep_label = SheepDragLabel()
        self.sheep_label.setToolTip("Add sheep")

        #add labels to toolbars
        self.crop_tool_bar.addWidget(self.wheat_label)
        self.crop_tool_bar.addWidget(self.potato_label)

        self.animal_tool_bar.addWidget(self.cow_label)
        self.animal_tool_bar.addWidget(self.sheep_label)

        #add toolbars to window
        self.addToolBar(self.crop_tool_bar)
        self.addToolBar(self.animal_tool_bar)

        self.field_graphics_view = QGraphicsView()
        self.field_graphics_view.setScene(FieldGraphicsScene(2,5))

        self.field_graphics_view.setFixedHeight(400)
        self.field_graphics_view.setFixedWidth(400)
        self.field_graphics_view.setSceneRect(0,0,400,400)
        self.field_graphics_view.setHorizontalScrollBarPolicy(1)
        self.field_graphics_view.setVerticalScrollBarPolicy(1)

        self.field_report_button = QPushButton("Field Report")
        self.field_automatic_grow_button = QPushButton("Automatically Grow Field")
        self.field_manual_grow_button = QPushButton("Manually Grow Fiels")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.field_graphics_view)
        self.layout.addWidget(self.field_report_button)
        self.layout.addWidget(self.field_automatic_grow_button)
        self.layout.addWidget(self.field_manual_grow_button)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

        #commections
        self.field_automatic_grow_button.clicked.connect(self.auromatically_grow)
        self.field_manual_grow_button.clicked.connect(self.manually_grow)

    def auromatically_grow (self):
        for days in range(30):
            food = random.randint(1, 100)
            water = random.randint(1, 10)
            light = random.randint(1, 10)
            self.field_graphics_view.scene().field.grow(light, food, water)
        self.field_graphics_view.scene().update_status()

    def manually_grow (self):
        dialog = ManualGrowDialog()
        dialog.exec_()
        light, water, food = dialog.get_values()
        self.field_graphics_view.scene().field.grow(light, food, water)
        self.field_graphics_view.scene().update_status()

def main():
    field_simulation = QApplication(sys.argv)#create new application
    field_window = FieldWindow()#create new instance of main window
    field_window.show()#make instance wisible
    field_window.raise_()#rase instance to top of window sack
    field_simulation.exec_()#monitor application for events

if __name__ == "__main__":
    main()
