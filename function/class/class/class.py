class File:
    def __init__(self):
        self.name = "syc"
        self.create_time = " today "
        self.change_num = 0
    def change_name(self,new_name):
        self.name = new_name
        self.change_num += 1
        #self.crate_time = "today"+str(self.change_num)
        string_out = str(self.name)+str(" is changed at ")+self.create_time+str(self.change_num)
        return string_out

myFile = File()
print(myFile.name)
print(myFile.create_time)
myFile.name = "syc2"
print(myFile.name)
print(myFile.change_name(123))
print(myFile.name)