class Bird:
    def __init__(self) :
        print(f"The {self.bird} is flying")
    bird="bat"
    
class Mammal(Bird):
    def __init__(self) :
        super().__init__()
        print("The mammal is running")

class Bat(Mammal):
    pass

bat=Bat()
print(Bat.bird)


    