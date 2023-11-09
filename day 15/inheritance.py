class GrandFather:
    def _init_(self):
       print(f"Grandfather owns {self.car}")
    car ="lambo"


class Father(GrandFather):
     
    def _init_(self):
       car="ferrari"
       super()._init_()
       print(f"Father owns {self.car}")
    house = "luxery house"

class Mother:
   jewellary="dimond necklace"

class Son (Father,Mother) :
  game_boy="ps5"

son = Son()
# father=Father()

# print(isinstance(father,object))

#print(son.house)
# print(son.car)
# print(son.jewellary)
# print(son.ring)
# print(son.game_boy)