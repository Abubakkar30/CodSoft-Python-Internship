#To create a To-Do Lists Application, We need to import packages

from  tkinter import * 
import tkinter.messagebox
import tkinter.filedialog
import tkinter.simpledialog
import tkinter.ttk as ttk
import datetime
import pickle

#We use entergoal() function to enter the task in the Listbox

def entergoal():

    #A new window to pop up to take input
    
    input_text=""
    def add():
        input_text=entry_goal.get(1.0, "end-1c")
        if input_text=="":
            tkinter.messagebox.showwarning(title="It's So Empty!",message="Please Enter Your Goal To Achieve, Soldier!")
        else:

            #It asks the user to enter the deadline for the task
            
            deadline = tkinter.simpledialog.askstring("Choose Your Final Day, Soldier!", "Enter The Final Day For Your Goal, Soldier! (YYYY-MM-DD):")
            try:

                #It converts the deadline to a datetime object
                
                deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d")

                #It appends the task and the deadline to the goal_list
                
                goal_list.append((input_text, deadline))
                
                #It updates the listbox with the task and the deadline
                
                listbox_goal.insert(END, input_text + " (" + deadline.strftime("%Y-%m-%d") + ")")

                #It closes the root1 window
                
                root1.destroy()
            except ValueError:

                #It shows an error message if the deadline is not valid
                
                tkinter.messagebox.showerror(title="Wrong Move, Soldier!", message="You Gave An Invalid Format For Your Final Day. Try Again, Soldier!")
            
    root1=Tk()
    root1.title("Set Your Goal To Achieve, Soldier!")
    entry_goal=Text(root1,width=40,height=4)
    entry_goal.pack()
    button_temp=Button(root1,text="Set Your Goal!",command=add)
    button_temp.pack()
    root1.mainloop()
    

#We use deletegoal() function to facilitate the delete task from the Listbox
    
def deletegoal():

    #It selects the selected item and then deletes it
    
    selected=listbox_goal.curselection()
    if selected:

        #It deletes the task from the tasks_list
        
        goal_list.pop(selected[0])
        
        #It deletes the task from the listbox
        
        listbox_goal.delete(selected[0])
    else:
        
        #It shows a warning message if no task is selected
        
        tkinter.messagebox.showwarning(title="It's So Empty!", message="Please Select A Goal That You Don't Need In Your Life, Soldier!")

#We use markcompleted() function to mark the task as completed
        
def markcompleted():
    marked=listbox_goal.curselection()
    if marked:
        temp=marked[0]
        
        #It stores the text of selected item in a string
        
        temp_marked=listbox_goal.get(marked)
        
        #It updates
        
        temp_marked=temp_marked+" (Achieved!) "
        
        #It deletes and then inserts 
        
        listbox_goal.delete(temp)
        listbox_goal.insert(temp,temp_marked)
    else:

        #It shows a warning message if no task is selected
        
        tkinter.messagebox.showwarning(title="Remember, Soldier!", message="Please Select A Goal To Mark As Won, Soldier!")

#We use savegoal() function to save the tasks to a file
        
def savegoal():
    
    #It asks the user to choose a file name and location
    
    file_name = tkinter.filedialog.asksaveasfilename(title="Save Your Goals, Soldier!", defaultextension=".dat")
    if file_name:
        
        #It opens the file in write mode
        
        file = open(file_name, "wb")
        
        #It uses pickle to dump the tasks_list to the file
        
        pickle.dump(goal_list, file)
        
        #It closes the file
        
        file.close()
        
        #It shows a success message
        
        tkinter.messagebox.showinfo(title="Superb, Soldier!", message="Goals Saved To " + file_name)

#We use loadgoal() function to load the tasks from a file
        
def loadgoal():
    
    #It asks the user to choose a file to load
    
    file_name = tkinter.filedialog.askopenfilename(title="Load Your Goals, Soldier!", filetypes=[("DAT files", "*.dat")])
    if file_name:
        
        #It opens the file in read mode
        
        file = open(file_name, "rb")
        
        #It uses pickle to load the tasks_list from the file
        
        global goal_list
        goal_list = pickle.load(file)
        
        #It closes the file
        
        file.close()
        
        #It clears the listbox
        
        listbox_goal.delete(0, END)
        
        #It updates the listbox with the tasks and deadlines
        
        for goal, deadline in goal_list:
            listbox_goal.insert(END, goal + " (" + deadline.strftime("%Y-%m-%d") + ")")
            
        #It shows a success message
            
        tkinter.messagebox.showinfo(title="Superb, Soldier!", message="Goals Loaded From " + file_name)

#Creating the initial window
        
window=Tk()

#Giving a title

window.title("PhoenixBird")

#Frame widget to hold the listbox and the scrollbar

frame_goal=Frame(window)
frame_goal.pack()

#To hold items in a listbox

listbox_goal=Listbox(frame_goal,bg="black",fg="white",height=15,width=50,font = "Arial")  
listbox_goal.pack(side=tkinter.LEFT)

#Scrolldown in case the total list exceeds the size of the given window

scrollbar_goal=Scrollbar(frame_goal)
scrollbar_goal.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_goal.config(yscrollcommand=scrollbar_goal.set)
scrollbar_goal.config(command=listbox_goal.yview)

#Button widget

entry_button=Button(window,text="Set Your Goals",width=50,command=entergoal)
entry_button.pack(pady=3)

delete_button=Button(window,text="Delete Goals That You Don't Want",width=50,command=deletegoal)
delete_button.pack(pady=3)

mark_button=Button(window,text="Mark Your Goals As Won ",width=50,command=markcompleted)
mark_button.pack(pady=3)

save_button=Button(window,text="Save Your Goals",width=50,command=savegoal)
save_button.pack(pady=3)

load_button=Button(window,text="Load Your Goals",width=50,command=loadgoal)
load_button.pack(pady=3)

#It initializes the goal_list as an empty list

goal_list = []

window.mainloop()

