import os 

#Specifiying the Directory we want to list
directory_path =  'F:\Python\PythonCodewithHary'

contents = os.listdir(directory_path)

#Printing Directory and name
for item in contents:
    print(item)