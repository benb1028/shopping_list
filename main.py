# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 11:08:26 2020

@author: Ryan Marshall
"""
import csv

def list2menu(l, msg = "Type the number of the selection."):
    n = 1
    for item in l:
        print(str(n)+ ".) " + str(item))
        n += 1
    selection = None
    while selection == None:
        selection = input(msg + '\n')
        index = None
        try:
            index = int(selection) - 1
        except:
            print("Invalid Selection.")
        if index is not None:
            if index >= 0 and index < len(l):
                return index
            else:
                selection = None
                print("Invalid Selection.")
        else:
            selection = None
main_menu = ["Add an item", "Delete an item", "View list", "Exit program", "Export list", "Import list"]
shopping_list = []
while True:
    choice = list2menu(main_menu)
    if choice == 0:
        to_add = str(input("Enter the item to be added:\n"))
        shopping_list.append(to_add)
    elif choice == 1:
        to_delete = list2menu(shopping_list, "Type the number of the item to be deleted:\n")
        shopping_list.pop(to_delete)
    elif choice == 2:
        n = 1
        for item in shopping_list:
            print(str(n)+ ".) " + str(item))
            n += 1
        exit_view = input("Press any key to exit view.\n")
    elif choice == 3:
        break
    elif choice == 4:
        file_out = input("Enter a name for the file:\n") + ".csv"
        with open(file_out, 'w') as file:
            for item in shopping_list:
                file.write(item)
                file.write("\n")
            print("File saved successfully.")
    elif choice == 5:
        shopping_list.clear()
        file_in = input("Enter the name of the file you would like to open:\n")
        with open(file_in, 'r') as file:
            readfile = csv.reader(file, delimiter = ',')
            for row in readfile:
                shopping_list.append(row[0])