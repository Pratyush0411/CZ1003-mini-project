# importing all the required modules and libraries

from tkinter import *
from tkcalendar import *
from tkinter import messagebox
from PIL import Image, ImageTk
import functools
import datetime
# importing the function Stallinfos from json_test
from json_file import Stallinfos

'''
Jing
The following code is just calling Stallinfos() function and creating suitable variables.
In this, the root and background image are being created
'''
time, menu_for_soup, menu_for_salad, menu_for_miniwok, menu_for_macdonalds, menu_for_chickenrice = Stallinfos()
root = Tk()
bgimg = Image.open("back.gif")
photo1 = ImageTk.PhotoImage(bgimg)  # .resize((1000,1000), Image.ANTIALIAS))
w, h = photo1.width(), photo1.height()
root.geometry('{W}x{H}'.format(W=w, H=h))
root.resizable(False, False)

'''
Pratyush 
The class Restaurants is a special class in the sense that it has parameterized constructor which assigns values to 
instance variables rest_name and food. After class declaration instances of the class are created as the stalls.
'''


class Restaurants:
    def __init__(self, name, menu):
        self.rest_name = name  # instantiating variable rest_name
        self.food = menu  # instantiating variable food


'''
Pratyush 
The following is the object declaration and passing of values for instance variables for rest_name and food
'''
soup = Restaurants("Soup", menu_for_soup)
mcdonalds = Restaurants("Macdonalds", menu_for_macdonalds)
miniwok = Restaurants("Mini wok", menu_for_miniwok)
chickenrice = Restaurants("Chicken rice", menu_for_chickenrice)
salad = Restaurants("Salad", menu_for_salad)
'''
Jing
The following snippet is just storing the object in a list and creating the clock, background image labels and placing
them on the frame '''
# creating a list of all the objects for the stalls
stalls = [soup, mcdonalds, miniwok, chickenrice, salad]
root.title("Mini Project")  # main window or root
LabelPhoto = Label(root, image=photo1)  # creating label for background image
LabelPhoto.place(x=0, y=0, relwidth=1, relheight=1 )
clock = Label(root, font=14)  # creating label for clock
clock.place(x=170, y=0)

'''

Pratyush 
The tick() function is just used to keep the clock label ticking using the methods .after(...) and .config(...)
'''


def tick():
    timenow = (datetime.datetime.now()).strftime('%H:%M:%S')
    clock.config(text=timenow + ' Hrs')
    clock.after(200, tick)


tick()

'''

Jing 
The buttons for main Frame i.e button1 and button2 besides the title label was made and placed inside this main Frame
(frame)
'''
frame = Frame(LabelPhoto, width=100, height=100)
frame.place(x=130, y=160)
title = Label(frame, font=14, text="Welcome to Nanyang Technological University\nCanteen Information System",
              bg="#2DA463", fg="black", relief=GROOVE)
title.pack()
# tuple for storing weekdays
weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
datelabel = Label(root, font=14,
                  text=f"{weekdays[int((datetime.datetime.now()).weekday())]}," + (datetime.datetime.now()).strftime(
                      "%m/%d/%Y"))
datelabel.place(x=0, y=0)

'''

Jing 
The back_button(...) takes in the cuurent frame, previous frame and the X and Y co-ordinates of the previous frame. 
The functionality is very simple as it just forgets to place the current frame and places the previous frame. One can 
that several function take in the frame which calls them as an arguement for making the backbutton operational'''


def back_button(current, prev, X, Y):
    current.place_forget()
    prev.place(x=X, y=Y)


'''

Pratyush 
openWindow1() function is used to open a frame inside the root when  button1 "View Today's Stores" is clicked. This 
function open a frame f1 which displays the stall buttons which when clicked call the displaymenu(). The function has 
nested looping design to check for open or closed stores.

'''


def openWindow1():
    global root, frame, weekdays
    frame.place_forget()
    f1 = Frame(LabelPhoto)
    f1.place(x=210, y=130)
    user_data = datetime.datetime.now()
    time_want = user_data
    day = time_want.weekday()
    chooseLabel = Label(f1, font=14, text='Please choose a store')
    chooseLabel.pack(fill=X)
    counter = 0
    '''
    
    Pratyush
    The loop design is such that the outer loop iterates over the keys of time dictionary that stores the operating 
    hours of each stall and the inner loop iterates over stalls which is a list of objects of stall created in which the
    displaymenu(....) function is called. If the stall is closed then as status False is passed.
    '''
    # outer loop iterates over the keys of time dictionary
    for key in time:
        # checking if the stall is closed
        if time[key][str(day)] == "closed":
            for item in stalls:
                # finding the object for the stall which is closed and status is passed as True
                if (item.rest_name).lower() == key.lower():
                    button1 = Button(f1, font=14, text=f"{item.rest_name}", relief=GROOVE, bg='lightblue',
                                     command=lambda item=item: displaymenu(item, time_want, f1, False))
                    button1.pack(fill=X)
        else:
            # splitting the operation hours string from time dictionary
            ot, ct = time[key][str(day)].split("-")
            ohours, ominutes = map(int, ot.split(":"))
            chours, cminutes = map(int, ct.split(":"))
            opening_time = time_want.replace(hour=ohours, minute=ominutes, second=0, microsecond=0)
            closing_time = time_want.replace(hour=chours, minute=cminutes, second=0, microsecond=0)
            # if the stall is open then checking whether entered time is within the operating hours
            if (time_want < closing_time) and (time_want >= opening_time):
                counter += 1  # counting the number of stalls open
                for item in stalls:
                    # finding the object for the stall which is open and status is passes as True
                    if (item.rest_name).lower() == key.lower():
                        button1 = Button(f1, font=14, text=f"{item.rest_name}", relief=GROOVE, bg='lightblue',
                                         command=lambda item=item: displaymenu(item, time_want, f1, True))
                        button1.pack(fill=X)
            else:
                for item in stalls:
                    # finding the stall as an object which is closed and status is passed as False
                    if item.rest_name == key:
                        button1 = Button(f1, font=14, text=f"{item.rest_name}", relief=GROOVE, bg='lightblue',
                                         command=lambda item=item: displaymenu(item, time_want, f1, False))
                        button1.pack(fill=X)
    backbutton = Button(f1, font=14, relief=GROOVE, text="Back", command=lambda: back_button(f1, frame, 130, 160))
    backbutton.pack(fill=X)
    if counter == 0:
        # showing message box if all the stores are closed and counter is 0
        messagebox.showinfo("Information", " All stores are closed now")


'''

Pratyush
The operating(...) function takes in one parameter that is the object and displays the operating hours in a day by day 
manner as the stalls can have different operating hours on different days. The loop design employed here is to make 
strings out of keys and elements in the nested dictionary time
'''


def operating(object):
    string = ''
    for key in time[object.rest_name]:
        # displaying the operation hours for each day
        string = string + f"{weekdays[int(key)]}:{time[object.rest_name][key]} \n"
    messagebox.showinfo("Information", f"{string}")


'''

Pratyush
The displaymenu(....) function takes in the object (stall), the required time, previous frame from which it was called(
for the operation of back button) and status of the stall (if it is open or closed). If the stall is closed then it 
shows closed in the menu else it displays the menu for the stall according to the day and time. This function is called 
from the loop structure in openWindow1() and check() functions.
'''


def displaymenu(object, time_want, frame, status):
    global root, weekdays
    frame.place_forget()
    f1 = Frame(LabelPhoto)
    f1.place(x=180, y=30)
    print(object.rest_name)
    datelabel = Label(f1, font=14, text=f"{weekdays[int(time_want.weekday())]}," + time_want.strftime(
        "%d/%m/%Y") + ',' + time_want.strftime('%H:%M'), bg="lightblue")
    datelabel.pack(fill=X)
    label1 = Label(f1, font=14, text=f"Welcome to {object.rest_name}", bg='#AECF3D', fg='black')
    label1.pack(fill=X)
    operation = Button(f1, font=14, relief=GROOVE, text="Operating Hours", command=lambda: operating(object))
    operation.pack()
    weekday = time_want.weekday()
    menu = Label(f1, font=14, text="Menu")
    menu.pack(fill=X)
    '''
    
    Pratyush
    The loop checks for the time key of the weekday key in the nested dictionary for menus for each stall.The menu for
    each stall has been stored as a single string for the time key. Hence the loop first checks for the day and then the
    time and displays the menu accordingly
    '''
    # if the stall is open then status is True
    if status:
        for key2 in object.food[str(weekday)]:
            # splitting the different time frames and accessing the menu for that time frame when it is matched
            it, bt = key2.split("-")
            ih, im = map(int, it.split(":"))
            bh, bm = map(int, bt.split(":"))
            inner_time = time_want.replace(hour=ih, minute=im, second=0, microsecond=0)
            outer_time = time_want.replace(hour=bh, minute=bm, second=0, microsecond=0)
            # checking if the user time is within the time frame key of the menu
            if (time_want < outer_time) and (time_want >= inner_time):
                menulabel = Label(f1)
                menulabel.configure(font=14, text=f"{object.food[str(weekday)][key2]}")
                menulabel.pack(fill=X)
            else:
                continue
    else:
        # if the stall is closed then closed is displayed in place of menu
        menulabel = Label(f1)
        menulabel.configure(font=14, text="Closed")
        menulabel.pack(fill=X)
    LabelEntry = Label(f1, font=14, text="Enter the no of people\nbefore you in the queue")
    LabelEntry.pack(fill=X)
    try:
        no_of_persons = Entry(f1, font=14)
        no_of_persons.pack(fill=X)
        calc = Button(f1, font=14, text="Calculate waiting time", relief=GROOVE,
                      command=lambda: estimatewaittime(no_of_persons, f1))
        calc.pack(fill=X)
    except:
        # error message is shown when there is an invalid input
        messagebox.showinfo("Warning", "Please enter integer value for no: of persons")
    backbutton = Button(f1, font=14, relief=GROOVE, text="Back", command=lambda: back_button(f1, frame, 210, 120))
    backbutton.pack(fill=X)


'''
Mervyn 
The estimatewaittime(...) function finds the waiting time at each stall. The parameters are user defined pax queuing and 
and previous frame which called the function (for the back button)
It takes 85 seconds per person and calculates the waiting time accordingly.
It is called from displaymenu(...) when the button calc is pressed. The GUI part of this functio was developed by
Jing
'''


def estimatewaittime(no_of_persons, frame):
    try:
        pax = int(no_of_persons.get())
        if pax < 0:
            raise ValueError
        # standard wait time per person is taken as 85 seconds
        Timesec = pax * 85
        Timemin = Timesec // 60
        Timesec = Timesec % 60
        # if wait time is more that 1 hour then a message is displayed
        if Timemin > 59:
            frame.place_forget()
            f1 = Frame(LabelPhoto)
            f1.place(x=210, y=160)
            approx_time2 = Label(f1, font=14, text="Waiting time is more than 1 hour\n Please look for another store")
            approx_time2.pack()
        else:
            # if not then the approximate wait time is displayed
            frame.place_forget()
            f1 = Frame(LabelPhoto)
            f1.place(x=210, y=160)
            approx_time = Label(f1, font=14,
                                text=f"Approximate waiting time:     \n{Timemin} minutes and {Timesec} seconds")
            approx_time.pack()
        backbutton = Button(f1, font=14, relief=GROOVE, text="Back", command=lambda: back_button(f1, frame, 180, 30))
        backbutton.pack(fill=X)
    except ValueError:
        messagebox.showinfo("Warning", "Please enter positive integer value for no: of persons")


# button for current date and time
button1 = Button(frame, font=12, text="View Today's stores", bg="#458CD3", relief=GROOVE, command=lambda: openWindow1())
button1.pack(fill=X)

'''

Jing
The function openWindow2() has been designed to open a frame when the button2 "View by other dates" is pressed.
The class dateandtime and the instantization of objects was done by me whereas the nested function check()
was made by Pratyush. Creating the class makes it easier as it adds a tag to user date ad time for the entire function
 '''


def openWindow2():
    global root, frame
    frame.place_forget()
    f2 = Frame(LabelPhoto)
    f2.place(x=200, y=160)

    class dateandtime:
        def __init__(self, window):
            # making labels for hours and minutes
            labelhh = Label(window, font=14, text="Hours:\n(24 hr)", bg="#83574D", fg='white')
            labelmins = Label(window, font=14, text="Minutes:", bg='#83574D', fg='white')
            # using tk calendar for making DateEntry
            self.cal = DateEntry(f2, font=14, width=9, background='darkblue', foreground='white', borderwidth=1)
            self.cal.grid(row=5, column=1, columnspan=10)
            labelhh.grid(row=7, column=1)
            global yy, mm, dd, tt
            # making entries for hours and minutes
            self.hour = Entry(window, width=5, font=14)
            self.minutes = Entry(window, width=5, font=14)
            self.hour.grid(row=7, column=2)
            labelmins.grid(row=7, column=3)
            self.minutes.grid(row=7, column=4)

    user_data = dateandtime(f2)
    '''
    
    Pratyush
    The check() function is very similar to the the openWindow1() as it employs the exact same looping design and calls
    displaymenu(..) when Enter is pressed.
    '''

    def check():
        try:
            # converting the day,month and year to int using map function after splitting the date string
            mm, dd, yy = map(int, f"{user_data.cal.get()}".split('/'))
            hh = int(user_data.hour.get())
            mins = int(user_data.minutes.get())
            time_want = datetime.datetime(yy, mm, dd, hh, mins, 0, 0)
            f2.place_forget()
            f3 = Frame(LabelPhoto)
            f3.place(x=210, y=120)
            counter = 0
            chooseLabel = Label(f3, font=14, text="Please choose a store")
            chooseLabel.pack()
            day = time_want.weekday()
            # outer loop iterates over the keys of time dictionary
            for key in time:
                # checking if the stall is closed
                if time[key][str(day)] == "closed":
                    for item in stalls:
                        # finding the stall as an object which is closed
                        if (f'{item.rest_name}').lower() == str(key).lower():
                            button1 = Button(f3, font=14, text=f"{item.rest_name}", relief=GROOVE, bg='lightblue',
                                             command=lambda item=item: displaymenu(item, time_want, f3, False))
                            button1.pack(fill=X)
                else:
                    # splitting the operation hours string from time dictionary
                    ot, ct = time[key][str(day)].split("-")
                    ohours, ominutes = map(int, ot.split(":"))
                    chours, cminutes = map(int, ct.split(":"))
                    opening_time = time_want.replace(hour=ohours, minute=ominutes, second=0, microsecond=0)
                    closing_time = time_want.replace(hour=chours, minute=cminutes, second=0, microsecond=0)
                    # if the stall is open then checking whether entered time is within the operating hours
                    if (time_want < closing_time) and (time_want >= opening_time):
                        counter += 1  # counting the no of stalls open
                        for item in range(len(stalls)):
                            # finding the object for the stall which is open and status is passed as True
                            if (stalls[item].rest_name).lower() == key.lower():
                                button1 = Button(f3, font=14, text=f"{stalls[item].rest_name}", relief=GROOVE,
                                                 bg='lightblue',
                                                 command=lambda item=item: displaymenu(stalls[item], time_want, f3,
                                                                                       True))
                                button1.pack(fill=X)
                    else:
                        for item in stalls:
                            # finding the stall as an object which is closed and status is passed as False
                            if item.rest_name == key:
                                button1 = Button(f3, font=14, text=f"{item.rest_name}", relief=GROOVE, bg='lightblue',
                                                 command=lambda item=item: displaymenu(item, time_want, f3, False))
                                button1.pack(fill=X)
            backbutton = Button(f3, relief=GROOVE, font=14, text="Back", command=lambda: back_button(f3, f2, 200, 160))
            backbutton.pack(fill=X)
            # If no stall is open then message box displayed
            if counter == 0:
                messagebox.showinfo("Information", " All stores are closed ")
        except:
            messagebox.showinfo("Warning", "Please enter valid date and time")

    # back button for second frame or f2 (date and time frame)
    backbutton = Button(f2, font=14, relief=GROOVE, text="Back", command=lambda: back_button(f2, frame, 130, 160))
    backbutton.grid(row=13, column=1, columnspan=10)
    # enter button for second frame or f2 (date and time frame)
    enter = Button(f2, font=14, relief=GROOVE, text="Enter", command=lambda: check())
    enter.grid(row=10, column=1, columnspan=10)


# button for custom date and time
button2 = Button(frame, font=12, text="View by other dates", bg="#458CD3", relief=GROOVE, command=lambda: openWindow2())
button2.pack(fill=X)
root.mainloop()

# 268 lines without comments
