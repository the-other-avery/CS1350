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