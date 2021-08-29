# oop part1:
# class Sample():
#     pass

# x = Sample()
# print(type(x))
# -------------------------------------------

# oop part2:
# class Dog():
#     # Class object attribute
#     species = 'mammal'
    
#     def __init__(self, breed, name = "Jacky"):
#         self.breed = breed
#         self.name = name

# mydog = Dog(breed = "Lab", name ='sammy')
# print(mydog.breed) # 這裡只是個標籤，並非一個func因此不需要小括號執行。

# otherdog = Dog(breed = "Huskie")
# print(otherdog.breed)

# print(mydog.name)
# print(otherdog.name)

# print(mydog.species)

# ----------------------------------
# Create a clss

# class Circle():
#     pi = 3.14

#     def __init__(self,radius = 1):
#         self.radius = radius
    
#     def area(self):
#         return self.radius * self.radius * Circle.pi
    
#     def set_radius(self , new_r):
#         self.radius = new_r

# myc =Circle(3)
# myc.radius = 100
# myc.set_radius(999)
# print(myc.area())

# ------------------------------------------------------
# oop part3
# Inheritance
# class Animal():
    
#     def __init__(self):
#         print("animal created")
    
#     def whoAmI(self):
#         print("Animal")

#     def eat(self):
#         print("Eating")

# class Dog(Animal):

#     def __init__(self):
#         # Animal.__init__(self)
#         print("Dog created")
    
#     def bark(self):
#         print("woof")
    
#     def eat(self):
#         print("Dog eatnig")


# mya = Animal()
# mya.whoAmI()
# mya.eat()

# mydog = Dog()
# mydog.whoAmI()
# mydog.eat()
# mydog.bark()

# special method

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title,self.author,self.pages)
    
    def __len__(self):
        return self.pages

    def __del__(self):
        print("a book is destroyed!")


b= Book("Python", "Jose", 200)
print(b)
print(len(b))

del b