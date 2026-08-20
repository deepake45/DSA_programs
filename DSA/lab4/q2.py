class ArrayList:
    def _init_(self):
        self.data = []
        self.size = 0
    def add(self, element):
        self.data.append(element)
        self.size += 1
    def display(self):
        for element in self.data:
            print(element, end = " ")


mylist = ArrayList()
mylist.add(10)
mylist.add(20)
mylist.add(30)
mylist.add(40)
mylist.display()
