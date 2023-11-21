import os
from time import sleep
try:
    f=open("hello text")
    print(f.readline())
    f.write("\n i was written from python")
    f.close()
    sleep(4)
    os.remove('arko.txt')
except FileNotFoundError:
    print("file not found")
except FileExistsError:
    print("file already already")    
except Exception as e:
    print("An error occured",e)


# to do:homework
#  take input from user to create File
#  
    