class Pizza:
    def dough(self):
        print("dough")
        return self
    
    def sauce(self):
        print("sauce")
        return self
    
    def mushroom(self):
        print("mushroom")
        return self
    
    def cheeese(self):
        print("cheese")
        return self
pizza =Pizza()

pizza \
    .dough() \
    .sauce() \
    .mushroom() \
    .cheeese() \
    .cheeese()


 