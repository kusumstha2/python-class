def sum(*numbers):   # * will change into tuple
    total=0
    for number in numbers:
        total+=number
    print(total)
sum(1,2,3,4,5,6,7,7,9,6)    