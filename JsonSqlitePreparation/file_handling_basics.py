
# try:
#     with open('file.txt', 'r') as f:
#         # to complete file data
#         data = f.read()
#         print("data ",data)
#         # to read all lines 

#         lines = f.readlines()
#         print("lines", lines)

#     with open('file.txt', 'a') as f:
#         data = ["this is one more \n", "one more \n"]
#         f.writelines(data)

#         line = "last one \n"
#         f.write(line)

#     with open('file.txt', 'r') as f:
        
#         line = f.readline()
#         print("First Line --> ", line)
#         #now the f is moved to next line but if you still want to read first line 
#         f.seek(0)
#         line = f.readline()
#         print("First Line --> ", line)

#         print(f.tell())
#         import os
#         f_stat = os.fstat(f.fileno())
#         print(f_stat)
    
# except IOError as e:
#     print(e)
# except Exception as e:
#     print(e)


import os
try : 

    filename = "myfile.txt"
    directory_name = os.getcwd()

    filepath = os.path.join(directory_name, filename)
    print(filepath)
    print(os.path.abspath(filepath))
    print(os.path.dirname(filepath))
    print(os.path.exists(filepath))
    print(os.path.isfile(filepath))
    print(os.path.isdir(os.path.dirname(filepath)))
    print(os.path.splitext(filename))
    

except OSError as e:
    print(e)