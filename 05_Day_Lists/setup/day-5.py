empty_list = list()
print(len(empty_list))
fruits = ["banana", "orange", "mango", "lemon"]  # list of fruits
vegetables = [
    "Tomato",
    "Potato",
    "Cabbage",
    "Onion",
    "Carrot",
]  # list of vegetables
animal_products = [
    "milk",
    "meat",
    "butter",
    "yoghurt",
]  # list of animal products
web_techs = [
    "HTML",
    "CSS",
    "JS",
    "React",
    "Redux",
    "Node",
    "MongDB",
]  # list of web technologies
countries = ["Finland", "Estonia", "Denmark", "Sweden", "Norway"]

print("Fruits:", fruits)
print("Number of fruits: ", len(fruits))
print("Vegetable: ", vegetables)
print("Number of vegetables: ", len(vegetables))
print("Animal products: ", animal_products)
print("Number of animal products:", len(animal_products))
print("Web technologies:", web_techs)
print("Number of web technologies:", len(web_techs))
print("Number of countries:", len(countries))


fruits = ["banana", "orange", "mango", "lemon"]
first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)  # orange
last_fruit = fruits[3]
print(last_fruit)  # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

fruits = ["banana", "orange", "mango", "lemon"]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)
print(second_last)

fruits = ["banana", "orange", "mango", "lemon"]
all_fruits = fruits[0:4]
all_fruits = fruits[0:]
orange_and_mango = fruits[1:3]
orange_mango_lemon = fruits[1:3]

fruits = ["banana", "orange", "mango", "lemon"]
all_fruits = fruits[-4:]
orange_and_mango = fruits[-3:-1]
orange_mango_lemon = fruits[-3:]

fruits = ["banana", "orange", "mango", "lemon"]
fruits[0] = "Avocado"
print(fruits)
fruits[1] = "apple"
print(fruits)
last_index = len(fruits) - 1
fruits[last_index] = "lime"
print(fruits)

fruits = ["banana", "orange", "mango", "lemon"]
does_exist = "banana" in fruits
print(does_exist)
does_exist = "lime" in fruits
print(does_exist)


fruits = ["banana", "orange", "mango", "lemon"]
fruits.append("apple")
print(fruits)
fruits.append("lime")
print(fruits)

fruits = ["banana", "orange", "mango", "lemon"]
fruits.insert(2, "apple")
print(fruits)
fruits.insert(3, "lime")
print(fruits)

fruits = ["banana", "orange", "mango", "lemon"]
fruits.remove("banana")
print(fruits)
fruits.remove("lemon")
print(fruits)

fruits = ["banana", "orange", "mango", "lemon"]
fruits.pop()
print(fruits)
fruits.pop(0)
print(fruits)

fruits = ["banana", "orange", "mango", "lemon"]
del fruits[0]
print(fruits)
del fruits[1]
print(fruits)
del fruits
# print(fruits)

fruits = ["banana", "orange", "mango", "lemon"]
fruits.clear()
print(fruits)

fruits = ["banana", "orange", "mango", "lemon"]
fruits_copy = fruits.copy()
print(fruits_copy)

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ["banana", "orange", "mango", "lemon"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print("Number: ", num1)
negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print("Integers: ", negative_numbers)
fruits = ["banana", "orange", "mango", "lemon"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
fruits.extend(vegetables)
print("Fruits and vegetables: ", fruits)

fruits = ["banana", "orange", "mango", "lemon"]
print(fruits.index("orange"))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)

fruits = ["banana", "orange", "mango", "lemon"]
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)
