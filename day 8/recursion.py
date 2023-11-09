# def hello():
#     print("hello World")
#     hello()

# hello()    

def number (n=0):
    print(n)
    if n==5:
        return
    number(n+1)
number()