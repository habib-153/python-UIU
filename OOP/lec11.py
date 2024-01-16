class Cat:
    def __init__(self,color,action) -> None:
        self.color = color
        self.action = action
    def view(self):
        print(self.color, "Cat is", self.action)

    def compare(self, cat):
        if self.action == cat.action:
            print("Both Cat are", cat.action)
        else:
            print("The are different")