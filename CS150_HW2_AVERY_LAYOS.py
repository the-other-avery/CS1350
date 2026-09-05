import sys

# week 1 lecture 1

grades = {"Alice": 85, "Bob": 92, "Carol": 78}

my_info = dict(name="Avery", age=20, major="cybersecurity")

print(my_info)

menu = {
    "Pizza slice": 2.99,
    "Monster energy": 1.99,
    "Cheeseburger": 4.99
}

print(menu)

course_credits = {
    "CS1350": 3,
    "CS2500": 3,
    "CYS4100": 3,
    "EGR2000": 3,
    "PSY1700": 3
}

print(course_credits)

pet = {"name": "Buddy", "type": "dog", "age": 3}

print(pet.get("name"), pet.get("age"))
print(pet.get("color"))

def has_passed(name, grades, passing_grade=60):
    grade = grades.get(name)
    if grade is None:
        return f"{name} not found in records."
    if grade >= passing_grade:
        return f"{name} passed with a grade of {grade}."
    else:
        return f"{name} did not pass. Grade: {grade}."

print(has_passed("Alice", grades))
print(has_passed("Bob", grades))
print(has_passed("Dave", grades))


products = {"laptop": 999.99, "mouse": 29.99, "keyboard": 79.99}

def check_price(product_name, products):
    price = products.get(product_name)
    if price is None:
        print("Product not available")
    else:
        print(f"{product_name}: ${price}")

check_price("laptop", products)
check_price("mouse", products)
check_price("monitor", products)

inventory = {"pears": 8, "oranges": 6, "apples": 10}

scores = {"Team A": 45, "Team B": 38}
print(scores)

scores['Team B'] = 52
scores.update({'Team C': 41})
print(scores)

print(scores.pop("Team A"))

cart = {}
print(cart)

cart.update({"cereal": 6.99})
cart.update({"monster energy": 1.99})
cart.update({"Call of duty": 16.99})
print(cart)

cart['cereal'] = 8.99
print(cart)

cart.pop("Call of duty")
print(cart)

# week 1 lecture 2

# Which of these are valid dictionary keys? Write "valid" or "invalid" and explain why:
# a) "student_name"     # _valid_ (reason: _strings are immutable and hashable_)
# b) [1, 2, 3]          # _invalid_ (reason: _lists are mutable, so they're unhashable, Python needs a key's hash to stay constant for the dict to work reliably_)
# c) 100                # _valid_ (reason: _integers are immutable and hashable_)
# d) ("x", "y")         # _valid_ (reason: _tuples are immutable and hashable, as long as all their elements are also hashable_)
# e) {"a": 1}           # _invalid_ (reason: _dicts are mutable, so they're unhashable, just like lists_)
# f) frozenset({1,2})   # _valid_ (reason: _frozensets are the immutable version of sets, so they're hashable_)

locations = {(40.7, -74.0): "New York", (34.0, -118.2): "Los Angeles"}

data = {"a": 1, "b": 2, "a": 3, "b": 4}

# 1: it will print the list {'a': 3, 'b': 4}
print(data)

# 2: it will print the length of the list
print(len(data))


print(hash("Avery"))
print(hash(100))

high_scores = {
    ("Alice", "Tetris"): 15000,
    ("Bob", "Pac-Man"): 8200,
    ("Alice", "Pac-Man"): 9700,
    ("Charlie", "Tetris"): 21000,
}

key = ("Alice", "Tetris")
print(f"{key} -> {high_scores[key]}")

temps = {"Monday": 72, "Tuesday": 75, "Wednesday": 68}

print("Days:", list(temps.keys()))

print("Temperatures:", list(temps.values()))

print("Number of days:", len(temps))


highest = max(temps.values())
lowest = min(temps.values())
print(f"Highest temperature: {highest}")
print(f"Lowest temperature: {lowest}")


if "Friday" in temps:
    print("Friday is in the dictionary.")
else:
    print("Friday is not in the dictionary.")

temps.setdefault("Thursday", 70)
print("After setdefault:", temps)

day_keys = temps.keys()
print("Keys view before adding Friday:", day_keys)

temps["Friday"] = 80
print("Keys view after adding Friday:  ", day_keys)



prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}


total = sum(prices.values())
average = total / len(prices)
print(f"Total value: ${total}")
print(f"Average price: ${average:.2f}")


most_expensive_name = max(prices, key=prices.get)
least_expensive_name = min(prices, key=prices.get)
print(f"Most expensive: {most_expensive_name} (${prices[most_expensive_name]})")
print(f"Least expensive: {least_expensive_name} (${prices[least_expensive_name]})")


keys_view = prices.keys()
keys_list = list(prices.keys())
print(f"Size of prices.keys() view:  {sys.getsizeof(keys_view)} bytes")
print(f"Size of list(prices.keys()): {sys.getsizeof(keys_list)} bytes")


prices.update({"headphones": 199, "keyboard": 89, "mouse": 49})
for name, price in prices.items():
    print(f"  {name}: ${price}")



colors = {"apple": "red", "banana": "yellow", "grape": "purple"}

for fruit, color in colors.items():
    print(f"The {fruit} is {color}")

# prediction for the output: [('apple', 'red'), ('banana', 'yellow'), ('grape', 'purple')]

print(list(colors.items()))


prices = {"coffee": 4.50, "tea": 3.00, "juice": 5.25}

for item, price in prices.items():
    with_tax = price * 1.10
    print(f"{item}: ${price:.2f} + tax = ${with_tax:.2f}")

count = 0
for item, price in prices.items():
    if price > 4.00:
        count += 1
print(f"Items over $4.00: {count}")

x = 10
y = 20
x, y = y, x
print(f"x = {x}, y = {y}")

numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(f"First: {first}")
print(f"Middle: {middle}")
print(f"Last: {last}")



top_student = max(scores.items(), key=lambda pair: pair[1])
print(f"Highest score: {top_student[0]} with {top_student[1]}")

passed = {}
failed = {}
for name, grade in scores.items():
    if grade >= 70:
        passed[name] = grade
    else:
        failed[name] = grade

average = sum(scores.values()) / len(scores)
deviations = {name: round(grade - average, 2) for name, grade in scores.items()}

n = 50_000
big_dict = {f"student_{i}": i for i in range(n)}

def sum_with_items():
    total = 0
    for key, value in big_dict.items():
        total += value
    return total

def sum_with_keys_lookup():
    total = 0
    for key in big_dict.keys():
        total += big_dict[key]
    return total