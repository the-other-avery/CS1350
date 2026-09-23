inventory = {"apples": 50, "bananas": 30, "oranges": 25}

for product in inventory:
    print(product)
total = sum(inventory.values())

print(total)
for product, quantity in inventory.items():
    print(product, quantity)

print("\n")

prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}

for product, value in sorted(prices.items()):
    print(f"{product}: {value}")

lowest_to_largest = dict(sorted(prices.items(), key=lambda x:[1]))

for key, value in lowest_to_largest.items():
    print(f"{key}: {value}")

print(max(prices.items()))


temps = {"Mon": 72, "Tue": 68, "Wed": 75, "Thu": 80, "Fri": 65}

print((sum(temps.values()) / len(temps.values())))

hottest_day, hottest_temp = None, float("-inf")
coldest_day, coldest_temp = None, float("inf")

for day, temp in temps.items():
    if temp > hottest_temp:
        hottest_day, hottest_temp = day, temp
    if temp < coldest_temp:
        coldest_day, coldest_temp = day, temp

print(f"Hottest: {hottest_day} ({hottest_temp}°)")
print(f"Coldest: {coldest_day} ({coldest_temp}°)")


for day,temp in temps.items():
    if temp > (sum(temps.values()) / len(temps.values())):
        print(day, temp)



products = {
    "laptop": {"price": 999, "stock": 15},
    "phone": {"price": 699, "stock": 50},
    "tablet": {"price": 449, "stock": 30}
}

print(products["laptop"]["price"])

for product, details in products.items():
    print(product, details["stock"])

countries = ["USA", "Canada", "Mexico"]
capitals = ["Washington", "Ottawa", "Mexico City"]

country_capitals = dict(zip(countries, capitals))
print(country_capitals)

products["tablet"] = {"price": 449, "stock": 30}
print(products)

products = {name: details for name, details in products.items() if details["stock"] >= 20}
print(products)

company = {
    "Engineering": {"Alice": 95000, "Bob": 85000},
    "Marketing": {"Carol": 75000, "Dave": 70000}
}

for department, employees in company.items():
    print(f"{department}:")
    for name, salary in employees.items():
        print(f"  {name}: ${salary:,}")

for department, employees in company.items():
    average = sum(employees.values()) / len(employees.values())
    print(f"{department}: ${average:,.2f}")

top_name, top_dept, top_salary = max(
    ((name, dept, salary) for dept, emps in company.items() for name, salary in emps.items()),
    key=lambda x: x[2]
)
print(f"Highest paid: {top_name} ({top_dept}) — ${top_salary:,}")

