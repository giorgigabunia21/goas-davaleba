games = ["farcry","gta","forza"]
games.append("ark survival evolved")
print(games)




guests = ["giorgi","luka","dachi","nika","zura"]
guests.append("demetre")
print(len(guests))



shopping_list = ["kitri","pomidori","kokakola","xaxvi","zeti"]
print(shopping_list)
shopping_list.pop(3)
print(shopping_list)
shopping_list.append("iogurti")
shopping_list.append("rdze")
print(shopping_list)



students = ["giorgi","nika","demetre","beka","zura"]
print(len(students))
students.pop(3)
print(students)
students.append("dachi")
students.append("luka")
print(students)
print(len(students))



def manage_list():
    numbers = [1,2,3]
    num = input("please enter new number: ")
    numbers.append(num)
    print(numbers)
    numbers.pop(2)
    print(numbers)
    print(len(numbers))
    print(numbers)

manage_list()