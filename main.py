from tkinter import *

root = Tk()
root.title("Calculator app by #2279")

def AddNumbers():
    def CalculationResult():
        TheFirstNumber = FirstNumber.get()
        TheSecondNumber = SecondNumber.get()
        try:
            if int(TheFirstNumber) and int(TheSecondNumber):
                TextLabel3 = Label(root, text=int(TheFirstNumber) + int(TheSecondNumber))
                TextLabel3.pack()
        except ValueError:
            TextLabel4 = Label(root, text="Type a number not word")
            TextLabel4.pack()
    TextLabel1 = Label(text="Enter first number")
    TextLabel1.pack()
    FirstNumber = Entry(root)
    FirstNumber.pack()
    TextLabel2 = Label(root, text="Enter second number")
    TextLabel2.pack()
    SecondNumber = Entry(root)
    SecondNumber.pack()
    CalculateButton = Button(root, text="Calculate", command=CalculationResult)
    CalculateButton.pack()

def SubtractNumbers():
    def SubtractionResult01():
        TheFirstNumber0 = FirstNumber01.get()
        TheSecondNumber01 = SecondNumber031.get()
        try:
            if int(TheFirstNumber0) and int(TheSecondNumber01):
                TextLabel03 = Label(root, text=int(TheFirstNumber0) - int(TheSecondNumber01))
                TextLabel03.pack()
        except ValueError:
            TextLabel04 = Label(root, text="Type a number not a word")
            TextLabel04.pack()
    TextLabel351 = Label(text="Enter First Number")
    TextLabel351.pack()
    FirstNumber01 = Entry(root)
    FirstNumber01.pack()
    TextLabel352 = Label(text="Enter Second Number")
    TextLabel352.pack()
    SecondNumber031 = Entry(root)
    SecondNumber031.pack()
    TextLabel352.pack()
    CalculateButton03 = Button(text="Calculate", command=SubtractionResult01)
    CalculateButton03.pack()

def MultiplyNumbers():
    def MultiplicationResult():
        TheFirstNumber310 = FirstNumberYes.get()
        TheSecondNumber315 = SecondNumberYes.get()
        try:
            if int(TheFirstNumber310) and int(TheSecondNumber315):
                Result = Label(root, text=int(TheFirstNumber310) * int(TheSecondNumber315))
                Result.pack()
        except ValueError:
            ErrorWidget = Label(root, text="Type a number not a word")
            ErrorWidget.pack()


    TextLabelIdk = Label(text="Enter First Number")
    TextLabelIdk.pack()
    FirstNumberYes = Entry(root)
    FirstNumberYes.pack()
    TextLabelIdk0 = Label(text="Enter Second Number")
    TextLabelIdk0.pack()
    SecondNumberYes = Entry(root)
    SecondNumberYes.pack()
    CalculationButton = Button(root, text="Calculate", command=MultiplicationResult)
    CalculationButton.pack()

def DivideNumbers():
    def DivisionResult():
        DivFirstNumber = FirstNumberYas.get()
        DivSecondNumber = SecondNumberYas.get()
        try:
            if int(DivFirstNumber) and int(DivSecondNumber):
                DivResult = Label(root, text=int(DivFirstNumber) / int(DivSecondNumber))
                DivResult.pack()
        except ValueError:
            ErrorWidget0 = Label(root, text="Type a number not a word")
            ErrorWidget0.pack()
        except ZeroDivisionError:
            YesHi = Label(root, text="You can't divide a number with 0")
            YesHi.pack()
    
    TextLabelIdk10 = Label(text="Enter First Number")
    TextLabelIdk10.pack()
    FirstNumberYas = Entry(root)
    FirstNumberYas.pack()
    TextLabelIdk13 = Label(text="Enter Second Number")
    TextLabelIdk13.pack()
    SecondNumberYas = Entry(root)
    SecondNumberYas.pack()
    CalculateButton6500 = Button(root, text="Calculate", command=DivisionResult)
    CalculateButton6500.pack()




# NOT APART OF ANY FUNCTION - THIS COMMENT WAS TO CLEAR CONFUSION FOR MYSELF
TextLabelWidget0 = Label(root, text="Calculator App", padx=50, pady=50, fg="black", bg="white")
TextLabelWidget0.pack()
TextLabelWidget1 = Label(root, text="Select an Operation")
TextLabelWidget1.pack()
ButtonWidget1 = Button(root, text="+", command=AddNumbers)
ButtonWidget1.pack()
ButtonWidget030 = Button(root, text="-", command=SubtractNumbers)
ButtonWidget030.pack()
MultiplyOperation = Button(root, text="* (Multiply)", command=MultiplyNumbers)
MultiplyOperation.pack()
DivisionOperation = Button(root, text="/ (Divide", command=DivideNumbers)
DivisionOperation.pack()

root.mainloop()