import json
"""
Mervyn 
This is the parsing of data from json files which houses the canteen,time and day information 
the pathway used is the full pathway so that it is less likely to encounter any errors

insert these 2 lines into the main file and it should work, also change the path directory and also remember to edit the 
cases, because it os all in strings and are in a line. ive seperated them by " \n " the "food:price" in that part

from json_test import Stallinfos
time,menu_for_soup,menu_for_salad,menu_for_miniwok,menu_for_macdonalds,menu_for_chickenrice = Stallinfos()
 
"""
def Stallinfos():
    try:
        with open(r"updatedtime.json", "r") as read_file:
            time = json.load(read_file)
        with open(r"souplinesdict.json", "r") as read_file:
            menu_for_soup = json.load(read_file)
        with open(r"saladlinesdict.json", "r") as read_file:
            menu_for_salad = json.load(read_file)
        with open(r"miniwokupdated.json", "r") as read_file:
            menu_for_miniwok = json.load(read_file)
        with open(r"macsupdated.json", "r") as read_file:
            menu_for_macdonalds = json.load(read_file)
        with open(r"chickenricelistdict.json", "r") as read_file:
            menu_for_chickenrice = json.load(read_file)
        return time,menu_for_soup,menu_for_salad,menu_for_miniwok,menu_for_macdonalds,menu_for_chickenrice

    except:
        print("File is not detected please change the pathway in the python code and try again")
        quit()
Stallinfos()