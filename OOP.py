def method_name(a,b):
    print("A methood")

class person:
    def __init__(self,person_name,date_of_birtth,ht):
       self.name = person_name
       self.date_of_birth= date_of_birtth
       self.hight=ht

    def get_name(self):
          return self.name

    def get_summary(self):
        return f"name:{self.name}, DoB:{self.date_of_birth},Hight:{self.hight}"

method_name(10,20)
a_person = person("apple")
b_person =person("opel")


print(a_person.get_name())
print(b_person.get_name())


