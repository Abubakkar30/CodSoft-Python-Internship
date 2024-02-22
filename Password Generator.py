# import the Tkinter module, the pyperclip module, and the string module
from tkinter import *
import pyperclip
import string
import random

# create a root window for the application
root = Tk()
# set the title of the window
root.title("PhoenixBird Password Generator")
# set the size of the window
root.geometry("600x600")

# create a label widget to display the title of the application
title_label = Label(root, text="Welcome, Soldier!", font="arial 20 bold")
# pack the label widget
title_label.pack(pady=10)

# create a string variable to store the password
passstr = StringVar()
# create an integer variable to store the password length
passlen = IntVar()
# set the default value of the password length to 8
passlen.set(8)

# create a function to generate the password
def generate():
    # create a list of all possible characters, numbers, and symbols
    all_chars = string.ascii_letters + string.digits + string.punctuation
    # use the random.choices function to generate a list of random characters, with the specified length
    password_list = random.choices(all_chars, k=passlen.get())
    # join the password list into a string
    password = "".join(password_list)
    # set the password string to the passstr variable
    passstr.set(password)

# create a function to copy the password to the clipboard
def copytoclipboard():
    # get the password string from the passstr variable
    random_password = passstr.get()
    # copy the password string to the clipboard using the pyperclip module
    pyperclip.copy(random_password)

# create a label widget to prompt the user to enter the password length
length_label = Label(root, text="Please Enter The Desired Length of Your Password, Soldier!", font="arial 12")
# pack the label widget
length_label.pack(pady=10)

# create a spinbox widget to take the password length input from the user
length_spinbox = Spinbox(root, from_=4, to_=32, textvariable=passlen, width=15, font="arial 16")
# pack the spinbox widget
length_spinbox.pack()

# create a button widget to generate the password
generate_button = Button(root, text="Generate Your Security Key", command=generate, font="arial 12")
# pack the button widget
generate_button.pack(pady=10)

# create an entry widget to display the generated password
password_label = Label(root, text="Your Desired Security Key Will Appear Here, Soldier!", font="arial 12")
password_label.pack(pady=10)
password_entry = Entry(root, textvariable=passstr, font="arial 16")
# pack the entry widget
password_entry.pack(pady=10)

# create a button widget to copy the password to the clipboard
copy_label = Label(root, text="Please Copy Your Security Key Into Your Clipboard For Future Use, Soldier!", font="arial 12")
copy_label.pack(pady=10)
copy_button = Button(root, text="Copy Your Security Key", command=copytoclipboard, font="arial 12")
# pack the button widget
copy_button.pack(pady=10)

# start the main loop of the application
root.mainloop()
