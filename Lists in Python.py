 #(Lists)#
students = ["Alex", "Mike", "Daniel"]
len(students)
print(students)
print(students[0])
print(students[1])
                     # Adding  (Append) insert (in the middle or in the begining)
cars = ["toyota","honda", "lexus", "audi"]
cars.insert(0, "BMW")
massage = "My first car was " + cars[1].title() + "."
print(massage)
print(cars)

cars = ["toyota","honda", "lexus", "audi"]
cars.append("BMW")
massage = "My first car was " + cars[1].title() + "."
print(massage)
print(cars)
               #Removing from the lists "del" by number
cars = ["toyota","honda", "lexus", "audi"]
del cars[0]
print(cars)
               #Removing from the lists "remove" by value
cars = ["toyota","honda", "lexus", "audi"]
cars.remove("honda")
massage = "My first car was " + cars[1].title() + "."
print(massage)
print(cars)
          # Sort() by alphabetic order) #
cars = ["toyota", "honda", "lexus", "audi"]
cars.sort()
print(cars)

cars = ["toyota", "honda", "lexus", "audi"]
cars.sort(reverse=True)
print(cars)

 #friends = ["shahnoza", "Gulya", "Nazira", "Shahlo"]
#massage = (friends)
#print(massage)
#print(friends[0].title() + " lets learn python together.")
#print("My best friend is " + friends[1])
#print("We studied with " + friends[2] + " at same school.")
#print(friends[-1] + " is my roomate.")
