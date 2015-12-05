# drawingpad.py
# turtle drawing pad

from turtle import *
from tkinter import *

def main():
    pad = TurtlePad()
    pad.run()

class TurtlePad():
    def __init__(self):
        """Constructor that sets up some varaiables."""
        # change these lines to alter the default behaviour of this program.
        self.cols = ['black', 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow']
        self.side = 50
        self.radius = 50
        self.long= 100
        self.short = 10
        self.starLen = 200
        self.starAngle = 170
        self.colNum = len(self.cols)
        self.shortString = str(self.short)
        self.longString = str(self.long)

    def star(self):
        """Draws a star - from http://docs.python.org/3.3/library/turtle.html"""
        temp = self.pen.pos()
        self.pen.color('red', 'yellow')
        self.pen.begin_fill()
        while 1:
            self.pen.fd(self.starLen)
            self.pen.lt(self.starAngle)
            if abs(self.pen.pos() - temp) < 1:
                break
        self.pen.end_fill()

    def penToggle(self):
        """Toggle the shape of the turtle"""
        if self.pen.shape() == 'classic':
            self.pen.shape('turtle')
        else:
            self.pen.shape('classic')

    def penHome(self):
        """Return tutle to origin."""
        self.pen.pu()
        self.pen.home()
        self.pen.seth(90)
        self.pen.pd()

    def polygon(self, sides):
        """Draws a regular polygon with "sides" sides. Change default length in __init__(self)."""
        for i in range (sides):
            self.pen.fd(self.side)
            self.pen.lt(360/sides)

    def filled(self, f,n):
        """Takes a function and wraps it in the fill commands."""
        self.pen.begin_fill()
        f(n)
        self.pen.end_fill()

    def updatePos(self):
        a,b = self.pen.pos()
        self.posL.configure(text=str(int(a)) + ',' + str(int(b)))


    def run(self):
        # Set up the GUI
        root = Tk()
        root.title("Turtle Drawing Pad")
        app=Frame(root)
        app.grid()

        canvas = Canvas(app, width=600, height=600)
        # make the canvas spread across 6 columns in the grid.
        canvas.grid(row=0, columnspan=6)
        self.pen = RawTurtle(canvas)
        # I like to start pointing "North".
        self.pen.seth(90)
        # Choose a decent speed.
        self.pen.speed(10)

        # First row buttons
        upB = Button(app, text="Pen Up", width=8,command=self.pen.pu)
        upB.grid(row=1, column=0, padx=1, pady=1)

        downB = Button(app, text="Pen Down", width=8, command=self.pen.pd)
        downB.grid(row=1, column=1, padx=1, pady=1)

        penColB = Button(app, text="Pen Colour", width=8)
        penColB["command"] = lambda: self.pen.pencolor(self.cols[(self.cols.index(self.pen.pencolor()) + 1) % self.colNum])
        penColB.grid(row=1, column=2, padx=1, pady=1)

        fillColB = Button(app, text="Fill Colour", width=8)
        fillColB["command"] = lambda: self.pen.fillcolor(self.cols[(self.cols.index(self.pen.fillcolor()) + 1) % self.colNum])
        fillColB.grid(row=1, column=3, padx=1, pady=1)

        penToggle = Button(app, text="Change Turtle", width=8,command=self.penToggle)
        penToggle.grid(row=1, column=4, padx=1, pady=1)

        penHome = Button(app, text="Home", width=8,command=self.penHome)
        penHome.grid(row=1, column=5, padx=1, pady=1)

        # Second row buttons
        leftB = Button(app, text="Left45", width=8)
        leftB["command"] = lambda: self.pen.lt(45)
        leftB.grid(row=2, column=0, padx=1, pady=1)

        rightB = Button(app, text="Right45", width=8)
        rightB["command"] = lambda: self.pen.rt(45)
        rightB.grid(row=2, column=1, padx=1, pady=1)

        penThick = Button(app, text="Thicken Pen", width=8)
        penThick["command"] = lambda: self.pen.width(1 + self.pen.width())
        penThick.grid(row=2, column=2, padx=1, pady=1)

        penThin = Button(app, text="Thin Pen", width=8)
        penThin["command"] = lambda: self.pen.width(-1 + self.pen.width())
        penThin.grid(row=2, column=3, padx=1, pady=1)

        penStamp = Button(app, text="Stamp", width=8,command=self.pen.stamp)
        penStamp.grid(row=2, column=4, padx=1, pady=1)

        clearB = Button(app, text="Clear", width=8, command=self.pen.clear)
        clearB.grid(row=2, column=5, padx=1, pady=1)

        # Third Row Buttons
        fwdB = Button(app, text="Fwd " + self.longString, width=8)
        fwdB["command"] = lambda: self.pen.fd(self.long)
        fwdB.grid(row=3, column=0, padx=1, pady=1)

        fwdShortB = Button(app, text="Fwd " + self.shortString, width=8)
        fwdShortB["command"] = lambda: self.pen.fd(self.short)
        fwdShortB.grid(row=3, column=1, padx=1, pady=1)

        circleB = Button(app, text="Circle", width=8)
        circleB["command"] = lambda: self.pen.circle(self.radius)
        circleB.grid(row=3, column=2, padx=1, pady=1)

        discB = Button(app, text="Disc", width=8)
        discB["command"] = lambda: self.filled(self.pen.circle, self.radius)
        discB.grid(row=3, column=3, padx=1, pady=1)

        sqB = Button(app, text="Square", width=8)
        sqB["command"] = lambda: self.polygon(4)
        sqB.grid(row=3, column=4, padx=1, pady=1)

        fillSqB = Button(app, text="Filled Square", width=8)
        fillSqB["command"] = lambda: self.filled(self.polygon,4)
        fillSqB.grid(row=3, column=5, padx=1, pady=1)

        # Fourth Row Buttons
        starB = Button(app, text="Star", width=8, command=self.star)
        starB.grid(row=4, column=0, padx=1, pady=1)

        triB = Button(app, text="Triangle", width=8)
        triB["command"] = lambda: self.polygon(3)
        triB.grid(row=4, column=1, padx=1, pady=1)

        fillTriB= Button(app, text="Fill Triangle", width=8)
        fillTriB["command"] = lambda: self.filled(self.polygon,3)
        fillTriB.grid(row=4, column=2, padx=1, pady=1)

        pentB = Button(app, text="Pentagon", width=8)
        pentB["command"] = lambda: self.polygon(5)
        pentB.grid(row=4, column=3, padx=1, pady=1)

        fillPentB= Button(app, text="Fill Pentagon", width=8)
        fillPentB["command"] = lambda: self.filled(self.polygon, 5)
        fillPentB.grid(row=4, column=4, padx=1, pady=1)

        self.posL = Label(app, text="0,0")
        self.posL.grid(row=4, column=5)

        # start the GUI
        self.updatePos()
        root.mainloop()


if __name__ == "__main__":
    main()
