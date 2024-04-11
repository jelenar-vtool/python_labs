import os #used for greping
import sys #used for checking py version installed

rootdir = os.getcwd() #returns the CurrentWorkingDirectory (absolute path)

#recursive function that returns the list of all files in current dir and all its sub dirs
def get_all_files(root):
    all_files = [] 
    list_of_files = os.listdir(root) #returns all it finds in current dir (files and folders)

    for file in list_of_files:
        fullPath = os.path.join(root, file) #joining abs and relative path to change dir
        if os.path.isdir(fullPath): #if dir, then enter it and call the function again
            all_files = all_files + get_all_files(fullPath)
        else: #if file, append it in file list
            all_files.append(fullPath)
                
    return all_files #return all files appended in list

#returns the list of sizes of all files provided in list_of_files list
def get_all_sizes(list_of_files, unit):
    if unit == 'k':
        div_rate = 1 #kB = B / 1024
    if unit == 'm':
        div_rate = 2 #mB = B / 1024 / 1024
    if unit == 'g':
        div_rate = 3 #gB = B / 1024 / 1024 / 1024
    sizes = []
    for file in list_of_files:
        sizeB = os.path.getsize(file)
        for i in range (0, div_rate):
            sizeB = float(sizeB) / 1024.0
        sizes.append(sizeB) #getsize function returns file sizes in B

    return sizes

#returns dictionary sorted by its values, in either acc or dec order (for dec reverse = True)
def sort_dict_by_value(d, reverse = False): 
    return dict(sorted(d.items(), key = lambda x: x[1], reverse = True))

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

