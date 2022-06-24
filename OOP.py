def method_name(a,b):
    print("A methood")

class person:
    def __init__(self,person_name):
       self.name = person_name

    def get_name(self):
          return self.name

method_name(10,20)
a_person = person("apple")
b_person =person("opel")


print(a_person.get_name())
print(b_person.get_name())


