#! /usr/bin/env python3

'''
    Open a window to draw shapes, much like a screen saver.

    The use is to experiment first with the PyTk5 graphics system,
    and second to experiment with some of the mathmatics for
    various shapes, especially stars.
'''

import sys

import random

import math

from PyQt5.QtCore import Qt, QTimer, QPointF
from PyQt5.QtGui import QBrush, QPainter, QPen, QPolygonF
from PyQt5.QtWidgets import (
    QApplication,
    QGraphicsItem,
    QGraphicsRectItem,
    QGraphicsEllipseItem,
    QGraphicsPolygonItem,
    QGraphicsScene,
    QGraphicsView,
    QHBoxLayout,
    QPushButton,
    QSlider,
    QVBoxLayout,
    QWidget,
)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # set the window dimentions
        screen = app.primaryScreen()
        geometry = screen.availableGeometry()
        self.setFixedSize(int(geometry.width() * 0.9), int(geometry.height() * 0.9))

        # Defining a scene rect of the available size, with it's origin at 0,0.
        # If we don't set this on creation, we can set it later with .setSceneRect
        self.scene = QGraphicsScene(0, 0, max_rect.width(), max_rect.height())

        # Define our layout.
        vbox = QVBoxLayout()

        strt = QPushButton("Start")
        strt.clicked.connect(self.strtTimer)
        vbox.addWidget(strt)

        stop = QPushButton("Stop")
        stop.clicked.connect(self.stopTimer)
        vbox.addWidget(stop)

        clear = QPushButton("Clear")
        clear.clicked.connect(self.clearGraphic)
        vbox.addWidget(clear)

        end = QPushButton("Exit")
        end.clicked.connect(self.endprogram)
        vbox.addWidget(end)

        view = QGraphicsView(self.scene)
        view.setRenderHint(QPainter.Antialiasing)

        hbox = QHBoxLayout(self)
        hbox.addLayout(vbox)
        hbox.addWidget(view)

        self.workingWidth = view.geometry().width()
        self.workingHeight = view.geometry().height()
        self.scene.setSceneRect(0, 0, self.workingWidth, self.workingHeight)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.newItem)
        self.strtTimer()

        self.setLayout(hbox)

    def strtTimer(self):
        self.timer.start(1000) # draw shape once per second

    def stopTimer(self):
        self.timer.stop()

    def newItem(self):
        item = random.choice([
            self.ellipse,
            self.rect,
            self.parallelogram,
            self.quadrilateral,
            self.star,
            ])()
        itemloc = (random.randint(0, self.workingWidth),random.randint(0, self.workingHeight))
        item.setPos(*itemloc)
        pen = QPen(random.choice([
            Qt.red,
            Qt.blue,
            Qt.green,
            Qt.white,
            Qt.cyan,
            Qt.magenta,
            Qt.yellow,
            Qt.darkRed,
            Qt.darkGreen,
            Qt.darkBlue,
            Qt.darkCyan,
            ]))
        pen.setWidth(1)
        item.setPen(pen)
        item.setRotation(random.randint(0,360))
        self.scene.addItem(item)

    def ellipse(self):
        itemsize = (random.randint(10, 150),random.randint(10, 150))
        return QGraphicsEllipseItem(0, 0, *itemsize)

    def rect(self):
        itemsize = (random.randint(10, 150),random.randint(10, 150))
        return  QGraphicsRectItem(0, 0, *itemsize)

    def parallelogram(self):
        itemsize = (random.randint(10, 150), random.randint(10, 150))
        shift = random.randint(10, 50)
        polygon = QPolygonF([QPointF(shift, 0), QPointF(shift+itemsize[0], 0),
             QPointF(itemsize[0],itemsize[1]),QPointF(0,itemsize[1])])
        return QGraphicsPolygonItem(polygon)

    def quadrilateral(self):
        itemsize = (random.randint(10, 150), random.randint(10, 150))
        shift = random.randint(10,50)
        polygon = QPolygonF([QPointF(shift, 0), QPointF(itemsize[0]-shift, 0),
             QPointF(itemsize[0],itemsize[1]),QPointF(0,itemsize[1])])
        return QGraphicsPolygonItem(polygon)

    def star(self):
        pattern = random.choice([
            (3,1),
            (5,2),
            (6,2),
            (7,3),
            (8,3),
            (9,3),
            (9,4),
            (10,4),
            (11,4),
            (12,4),
            (11,5),
            (12,5),
        ])
        numpoints = pattern[0]
        space = ((2 * math.pi) / numpoints) * pattern[1]
        radius = random.randint(30, 150)
        # point (0,𝑟) ends up at 𝑥=𝑟cos𝜃, 𝑦=𝑟sin𝜃.
        points = []
        for i in range(numpoints):
            points.append(QPointF(radius * math.cos(i*space), radius * math.sin(i*space)))
        return QGraphicsPolygonItem(QPolygonF(points))

    def clearGraphic(self):
        self.scene.clear()

    def endprogram(self):
        app.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    screen = app.primaryScreen()
    max_rect = screen.availableGeometry()

    w = Window()
    w.show()

    app.exec()
