# shapes
Python implementation of a graphics window using PyQt5

Harkening back to a screensaver written in Objective C ( see https://github.com/rpural/rpSaver2 ), 
this is basically just a window implementing drawing various shapes using random colors.

rpSaver left off with attempting to draw stars, but I never had time to add that feature,
and I always regretted that. I wanted to have a platform I could implement and draw various shapes
in, so that I could experiment with stars and various other shapes.

THe current program draws random ellipses, rectangles, quadrilaterals... and Stars! This first
attempt uses the Schläfli descriptions and draws each star by connecting the points in the right
order. For instance, a "normal" 5-point star is represented by the Schläfli symbol {5,2}. This 
means that you divide a circle into 5 equi-distant points, and then connect every other point
until you get back to the starting point.

The type(s) of shapes to be drawn are selectable via checkboxes, the process can be stopped and started,
and the window can be cleared so that it is less crowded again.

[TODO] - implement an algorithm for an irregular star using points on two semi-concentric circles.
