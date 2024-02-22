# Importing the Tkinter module to design a calculator

from tkinter import *

# Creating a Calculator class that inherits from Tk

class Calculator(Tk):
    
    # Defining the __init__ method
    
    def __init__(self):
        
        # Calling the __init__ method of the parent class
        
        super().__init__()
        
        # Setting the title and geometry of the main window of the calculator
        
        self.title("PhoenixBird Calculator")
        self.geometry("260x150")
        
        # Creating a StringVar object to store the expression
        
        self.expression = StringVar()
        
        # Creating an Entry widget to display the expression
        
        self.entry = Entry(self, textvariable=self.expression)
        
        # Using the grid method to place the entry widget on the main window
        
        self.entry.grid(columnspan=4, ipadx=70)
        
        # Creating Button widgets for each digit and operation provided in the calculator
        
        self.button1 = Button(self, text="1", command=lambda: self.press(1))
        self.button2 = Button(self, text="2", command=lambda: self.press(2))
        self.button3 = Button(self, text="3", command=lambda: self.press(3))
        self.button4 = Button(self, text="4", command=lambda: self.press(4))
        self.button5 = Button(self, text="5", command=lambda: self.press(5))
        self.button6 = Button(self, text="6", command=lambda: self.press(6))
        self.button7 = Button(self, text="7", command=lambda: self.press(7))
        self.button8 = Button(self, text="8", command=lambda: self.press(8))
        self.button9 = Button(self, text="9", command=lambda: self.press(9))
        self.button0 = Button(self, text="0", command=lambda: self.press(0))
        self.button_plus = Button(self, text="+", command=lambda: self.press("+"))
        self.button_minus = Button(self, text="-", command=lambda: self.press("-"))
        self.button_multiply = Button(self, text="*", command=lambda: self.press("*"))
        self.button_divide = Button(self, text="/", command=lambda: self.press("/"))
        self.button_modulo = Button(self, text="%", command=lambda: self.press("%"))
        self.button_exponent = Button(self, text="^", command=lambda: self.press("**"))
        self.button_equal = Button(self, text="=", command=self.equalpress)
        self.button_clear = Button(self, text="C", command=self.clear)
        
        # Using the grid method to place the button widgets on the main window of the calculator
        
        self.button1.grid(row=2, column=0)
        self.button2.grid(row=2, column=1)
        self.button3.grid(row=2, column=2)
        self.button_plus.grid(row=2, column=3)
        self.button4.grid(row=3, column=0)
        self.button5.grid(row=3, column=1)
        self.button6.grid(row=3, column=2)
        self.button_minus.grid(row=3, column=3)
        self.button7.grid(row=4, column=0)
        self.button8.grid(row=4, column=1)
        self.button9.grid(row=4, column=2)
        self.button_multiply.grid(row=4, column=3)
        self.button0.grid(row=5, column=0)
        self.button_modulo.grid(row=5, column=1)
        self.button_exponent.grid(row=5, column=2)
        self.button_divide.grid(row=5, column=3)
        self.button_equal.grid(row=6, column=0, columnspan=2)
        self.button_clear.grid(row=6, column=2, columnspan=2)

    # Defining the press function, which updates the expression with the pressed button
    
    def press(self, num):
        
        # Getting the current value of the expression
        
        current = self.expression.get()
        
        # Appending the pressed button to the expression
        
        new = current + str(num)
        
        # Setting the new value of the expression
        
        self.expression.set(new)

    # Defining the equalpress function, which evaluates the expression and displays the result
    
    def equalpress(self):
        
        # Trying to evaluate the expression
        
        try:
            
            # Getting the current value of the expression
            
            current = self.expression.get()
            
            # Evaluating the expression using the eval function
            
            result = eval(current)
            
            # Setting the result as the new value of the expression
            
            self.expression.set(result)
            
        # Handling any possible errors
        
        except:
            
            # Set the expression value as "error"
            
            self.expression.set("Wrong Move!")
            

    # Defining the clear function, which clears the expression
    
    def clear(self):
        
        # Setting the expression value as an empty string
        
        self.expression.set("")

# Creating an instance of the Calculator class

calc = Calculator()

# Calling the mainloop method to run the application

calc.mainloop()
