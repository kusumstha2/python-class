while True:
    try:
        number = int(input("Enter a number:"))
        second_number =int (input("Enter a number:"))

        print(number/second_number)
    except ValueError:
        print("you didn't enter an integer!")
    except ZeroDivisionError:
        print("Number cannot be divisible by zero")

    except:
       raise Exception ("unexpected error occured") 
       print("error!")  


               