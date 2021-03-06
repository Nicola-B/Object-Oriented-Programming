#Nicola Batty
#30/07/2015
#Farm simulation graphic field scene class

from PyQt4.QtGui import *

from Farm_simulation_Fields import *
from Farm_simulation_graphic_wheat_item_class import*
from Farm_simulation_graphic_potato_item_class import*
from Farm_simulation_graphic_cow_item_class import*
from Farm_simulation_graphic_sheep_item_class import*

import resources

class FieldGraphicsScene(QGraphicsScene):
    #This class procides a scene to manage items in the field

    #constructor
    def __init__(self, max_crops, max_animals):
        super().__init__()

        self.field = Field(max_crops, max_animals)

        self.background_brush = QBrush()
        self.background_picture = QPixmap(":/field_background.png")
        self.background_brush.setTexture(self.background_picture)
        self.setBackgroundBrush(self.background_brush)

    def harvest_crop(self, crop_to_harvest):
        position = self.field._crops.index(crop_to_harvest)
        self.field.harvest_crop(position) #remove crop from field
        self.removeItem(crop_to_harvest) #remove visual representation

    def remove_animal(self, animal_to_remove):
        position = self.field._animals.index(animal_to_remove)
        self.field.remove_animal(position) #remove crop from field
        self.removeItem(animal_to_remove) #remove visual representation

    def update_status(self):
        for each in self.field._crops:
            each.update_status()
        for each in self.field._animals:
            each.update_status()

    def _drop_position(self, item):
        cursor_position = QCursor.pos() #global cursor position
        current_view = self.views()[0]
        scene_position = current_view.mapFromGlobal(cursor_position)

        width = item.boundingRect().width()
        height = item.boundingRect().height()

        width_offset = width/2
        height_offset = height/2

        drop_x = scene_position.x() - width_offset
        drop_y = scene_position.y() - height_offset

        return drop_x, drop_y

    def _visualise_graphic_item(self, graphic_item_type):
        if graphic_item_type == "crop":
            X, Y = self._drop_position(self.field._crops[-1])
            self.field._crops[-1].setPos(X, Y)
            self.addItem(self.field._crops[-1])
        elif graphic_item_type == "animal":
            X, Y = self._drop_position(self.field._animals[-1])
            self.field._animals[-1].setPos(X, Y)
            self.addItem(self.field._animals[-1])

    def _add_graphic_item( self, result, graphic_item_type):
        if result:
            self._visualise_graphic_item(graphic_item_type)
        else:
            error_message = QMessageBox()
            error_message.setText("No more {0}'s can be added to this field".format(graphic_item_type))
            error_message.exec()

    #This method orrides the parent method
    def dragEnterEvent(self, event):
        #what to do if an object is dragged into the scene
        event.accept()

    def dragMoveEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        event.accept()

        #what to do if an object is dropped on the scene
        if event.mimeData().hasFormat("application/x-wheat"):
            crop_added = self.field.plant_crop(WheatGraphicsPixmapItem())
            self._add_graphic_item(crop_added, "crop")
        elif event.mimeData().hasFormat("application/x-potato"):
            crop_added = self.field.plant_crop(PotatoGraphicsPixmapItem())
            self._add_graphic_item(crop_added, "crop")
        elif event.mimeData().hasFormat("application/x-cow"):
            animal_added = self.field.add_animal(CowGraphicsPixmapItem())
            self._add_graphic_item(animal_added, "animal")
        elif event.mimeData().hasFormat("application/x-sheep"):
            animal_added = self.field.add_animal(SheepGraphicsPixmapItem())
            self._add_graphic_item(animal_added, "animal")
