# Opening a .txt file into a python file

# create a 'Fahim.txt' file before at hand to open

xy = open ('Fahim.txt', 'r+')      # 'r' for read mode     # 'w' for write mode    # 'r+' means both
                                   # 'xy' is a variable
# print(xy.readable())             # check whether the file is 'readable' or not

# print(xy.writable())

# file = (xy.read())               # 'file' is a variable
# print(file)                      # read the file in the 'output'

# print(len(file))                 # calculate the overall 'characters' of the file

# felix = xy.readlines()           # convert the whole file into a 'list'
# print(felix)                     # 'felix' is a variable

# felix = xy.readlines()[0]        # print the 'first line' of the file using 'index value'
# print(felix)

for lines in xy :                  # print the whole file using 'for loop'
   print(lines)


xy.close()                         # when to open a file other than 'python file', the good practice is to give a 'close' command as well