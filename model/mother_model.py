from abc import ABC, abstractmethod

class AbstractParent(ABC):

    @abstractmethod
    def hell_friend(self):
        raise NotImplementedError

class Mother:

    def __init__(self, age=0):
        print("mother constructor")

    def do_work(self):
        print("I'm working")

    def do_house_work(self):
        print("listening to music")

    def go_shopping(self):
        print("Oh.... I love shopping very much))")

class Father(AbstractParent):

    def __init__(self):
        print("father constructor")

    def play_guitar(self):
        print("Play guitar")

    def do_house_work(self):
        print("sitting on the sofa and drink beer")

class Daughter(Mother, Father):

    def __init__(self, age=0):
        Mother.__init__(self, age=age)
        Father.__init__(self)

    def hell_friend(self):
        pass

    def do_work(self):
        print("I'm working like a horse")

class Friend:
    pass

def greet_mother(mother : Mother):
    print("Hello mother!!!")
    mother.do_work()

def greet_father(father : Father):
    print("Hello father!!!")
    father.play_guitar()

if __name__ == "__main__":

    daughter = Daughter()
    #daughter.do_work()

    # change object class
    #daughter.__class__ = Friend

    greet_mother(daughter)
    greet_father(daughter)
    daughter.hell_friend()
    daughter.do_house_work()
    daughter.go_shopping()

    for x in [daughter]:
        x.do_house_work()

    #list
    povtorka_list = ["matan_2", "programming_2", "super_prise"]

    #tuple
    vasian = ("11 year", 12, 3.14, daughter)

    #set
    my_set = {23, 11, 10, 11, "call"}
    print(my_set)

    #frozen set
    another_set = frozenset(["do", "re", "mi"])

    #dictionary
    my_dict = {1: "first", "2": 123}