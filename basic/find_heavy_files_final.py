import os #used for greping
import sys #used for checking py version installed
#TODO: Get Current Working Directory

#TODO: Write a function to retrieve all files within a directory and its subdirectories.
def get_all_files(root):


#TODO: Create a function to get the sizes of all files.
def get_all_sizes(list_of_files, unit):
 

#TODO: Write a function to sort a dictionary by its values.
def sort_dict_by_value(d, reverse = False): 

particular_file_extension_flag = False

unit_entered_flag = True
while unit_entered_flag:
    if sys.version_info[0] < 3: # most servers have py2 installed, so checking the version is done to make it compatable for both 2 and 3 (2 uses raw_input insted of input)
        unit = raw_input("In what unit would you like to display files?\nEnter g for GB ; Enter m for MB ; Enter k for KB: ")
        extension = raw_input("Do you want to find files of any particular extension?\n If yes, enter it (for example .trn .vcd .log etc). If not just hit Enter key:   ")
    else:
        unit = input("In what unit would you like to display files?\nEnter g for GB ; Enter m for MB ; Enter k for KB: ")
        extension = input("Do you want to find files of any particular extension?\n If yes, enter it (for example .trn .vcd .log etc). If not just hit Enter key:   ")
    if unit == "g" or unit == "m" or unit == "k":
        unit_entered_flag = False
    else:
        print("\n Error! Please try again.\n")

files = get_all_files(rootdir) #get all files from the sorted dictionary
sizes = get_all_sizes(files, unit) #get all file sizes from the sorted dictionary

if extension != "": #that means user wants to find only files that have a particual extension
    new_files = []
    new_sizes = []
    for i in range(0, len(files)):
        if files[i].find(extension) != -1: #if there is a extension substring in file name add this file and its size to new list
            new_files.append(files[i])
            new_sizes.append(sizes[i])
    sizes = new_sizes
    files = new_files


if sys.version_info[0] < 3:
    total_files_to_print = int(raw_input("How many heavy files do you want to print: "))
    if len(files) < total_files_to_print: #if there are less files than you'd want to print, it will print them all
        total_files_to_print = len(files)
    for i in range(0, total_files_to_print):
        max_value = max(sizes)
        max_index = sizes.index(max_value)
        print("file = " + files[max_index]  + "\nsize = " + str(sizes[max_index]) + "\n")
        files.pop(max_index)
        sizes.pop(max_index)

else:
    file_size = {} #dictionary is used to pair matching file and size, to sort it as it should

    for i in range(0, len(files)): #used to fill dictionary with matching file and size
        file_size[files[i]] = sizes[i]

    sorted_dict = sort_dict_by_value(file_size, True) #sorting dictionary by its value (size) in dec order

    heavy_files = list(sorted_dict.keys()) #load all sorted files in list, for printing purpases
    heavy_files_sizes = list(sorted_dict.values()) #load all sorted files in list, for printing purpases

    total_files_to_print = int(input("How many heavy files do you want to print: "))

    if len(heavy_files) < total_files_to_print: #if there are less files than you'd want to print, it will print them all
        total_files_to_print = len(heavy_files)

    print("Here are" + str(total_files_to_print) + "heaviest files and their size: \n \n")
    for i in range(0,total_files_to_print):
        print("file = " + heavy_files[i] + "\nsize = " + str(heavy_files_sizes[i]) + "\n")

