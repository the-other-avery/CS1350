import time

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


cubes = {n: n**3 for n in range(1, 6)}

temps = {"Mon": 72, "Tue": 68, "Wed": 75}
temps_c = {day: round((f - 32) * 5/9, 1) for day, f in temps.items()}
print(temps_c)

scores = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}

passing = {name: score for name, score in scores.items() if score >= 70}
print(passing)

def to_letter(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else: return "F"

letter_grades = {name: to_letter(score) for name, score in scores.items()}
print(letter_grades)

student_ids = {"Alice": 101, "Bob": 102}

id_to_name = {student_id: name for name, student_id in student_ids.items()}
print(id_to_name)


sales = [
    ("North", "Alice", 5000), ("South", "Bob", 4500),
    ("North", "Carol", 6000), ("South", "Alice", 3500)
]

totals_by_region = {}
for region, name, amount in sales:
    totals_by_region[region] = totals_by_region.get(region, 0) + amount
print(totals_by_region)

totals_by_person = {}
for region, name, amount in sales:
    totals_by_person[name] = totals_by_person.get(name, 0) + amount
print(totals_by_person)

nested = {}
for region, name, amount in sales:
    nested.setdefault(region, {})
    nested[region][name] = nested[region].get(name, 0) + amount
print(nested)




vowels = set(['a', 'e', 'i', 'o', 'u'])
numberList = set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) # it has 4 elements
print(len(numberList))

# empty = {} it should instead be empty = set()

text = "mississippi"
unique_chars = set(text)
print(unique_chars)
print(len(unique_chars))

emails = ["a@b.com", "c@d.com", "a@b.com", "e@f.com", "c@d.com"]

unique_emails = list(set(emails))
print(unique_emails)

# s = {[1, 2], [3, 4]} fails because it is unhashable with the square brackets

numbers_list = list(range(1_000_000))
numbers_set = set(range(1_000_000))

start = time.perf_counter()
999999 in numbers_list
list_time = time.perf_counter() - start

start = time.perf_counter()
999999 in numbers_set
set_time = time.perf_counter() - start

print(f"List lookup: {list_time*1e6:.2f} µs")
print(f"Set lookup:  {set_time*1e6:.2f} µs")
print(f"Set is ~{list_time/set_time:.0f}x faster")

game_results = {
    frozenset(["Alice", "Bob"]): "Alice won",
    frozenset(["Carol", "Dave"]): "Draw",
}

print(game_results[frozenset(["Bob", "Alice"])])

edges = [(1, 2), (2, 3), (1, 3), (3, 4)]

nodes = {node for edge in edges for node in edge}
print(nodes)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

unique_numbers = a | b
print(unique_numbers)

numberSets = a & b
print(numberSets)

only_in_a = a - b
print(only_in_a)

morning_shift = {"Alice", "Bob", "Carol"}
evening_shift = {"Carol", "Dave", "Eve"}
weekend_shift = {"Alice", "Eve", "Frank"}

all_shifts = morning_shift & evening_shift & weekend_shift
print(all_shifts) #empty because no one works all shifts

at_least_one_shift = morning_shift | evening_shift | weekend_shift
print(at_least_one_shift)

only_morning = morning_shift - evening_shift - weekend_shift
print(only_morning)

exactly_one = (
    (morning_shift - evening_shift - weekend_shift) |
    (evening_shift - morning_shift - weekend_shift) |
    (weekend_shift - morning_shift - evening_shift)
)
print(exactly_one)

prereqs_met = {"Alice", "Bob", "Carol", "Dave"}
has_space = {"Bob", "Carol", "Eve", "Frank"}
paid_tuition = {"Alice", "Carol", "Eve"}

all_Met = prereqs_met & has_space & paid_tuition
print(all_Met, "has all three of these met to enroll.")

noTuition = prereqs_met - paid_tuition
print(noTuition, "have pre reqs met but have not paid tuition.")

prereqORtuition = prereqs_met or paid_tuition
print(prereqORtuition)




numbers = {1, 2, 3}
print(numbers)

numbers.add(4)
print(numbers)

numbers.remove(1)
print(numbers)

evens = {x for x in range(21) if x % 2 == 0}
print(evens)

s = {2, 4, 6}
s.discard(99) # no error only discards if item is in set
print(s)
# s.remove(99)  # KeyError: 99

intermediate_s = [4, 5, 2, 4, 8, 5, 2, 1, 9, 4]
print(intermediate_s)
result = list(dict.fromkeys(intermediate_s))
print(result)

sentence = "To be or not to be that is the question"
unique_words = {word.lower() for word in sentence.split()}
print(*unique_words)

expected = set(range(1, 11))
actual = {1, 2, 4, 5, 7, 8, 10}

missing = expected - actual
print(sorted(missing))

def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return duplicates

alice = {"Python", "SQL", "Excel", "Tableau"}
bob = {"Python", "Java", "SQL", "AWS"}
carol = {"Python", "R", "SQL", "Tableau"}

allSkills = alice & bob & carol
print("alice, bob and carol all have skills in:", allSkills)

onlyAlice = alice - bob - carol
print(onlyAlice)

uniqueSkills = alice | bob | carol
print(uniqueSkills)

def common_chars(s1, s2):
    return set(s1) & set(s2)

print(common_chars("hello", "world"))