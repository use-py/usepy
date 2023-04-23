from usepy.utils import useFuncName


def abc():
    print("my name is " + useFuncName())


class A:
    def __init__(self):
        self.name = "A"
    
    def abc(self):
        print("my name is " + useFuncName(self))


abc()
A().abc()
