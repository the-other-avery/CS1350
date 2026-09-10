# Contact records: name -> dictionary of details
contact_book = {
"Mom": {"phone": "555-1234", "category": "Family", "city": "Fort Wayne"},
"Dad": {"phone": "555-4321", "category": "Family", "city": "Fort Wayne"},
"Sister": {"phone": "555-7777", "category": "Family", "city": "Chicago"},
"Best Friend": {"phone": "555-8888", "category": "Friend", "city": "Indianapolis"},
"Roommate": {"phone": "555-3141", "category": "Friend", "city": "Fort Wayne"},
"Boss": {"phone": "555-0000", "category": "Work", "city": "Chicago"},
"Professor": {"phone": "555-2718", "category": "Work", "city": "Fort Wayne"},
"Dentist": {"phone": "555-2222", "category": "Business", "city": "Indianapolis"},
}

call_log = {
"Mom": {"Jan": 120, "Feb": 95, "Mar": 140},
"Dad": {"Jan": 45, "Feb": 60, "Mar": 30},
"Sister": {"Jan": 80, "Mar": 70},
"Best Friend": {"Jan": 200, "Feb": 180, "Mar": 220},
"Roommate": {"Feb": 15, "Mar": 25},
"Boss": {"Jan": 60, "Feb": 90, "Mar": 75},
"Professor": {"Feb": 20, "Mar": 35},
"Dentist": {"Jan": 10},
}

# phase 1

quick_contacts = {"Mom": "555-1234", "Dad": "555-5678", "Best Friend": "555-8888", "Pizza Place": "555-9999", "Work": "555-0000"}

print(quick_contacts["Mom"])
quick_contacts["Dad"] = "555-4321"
print("Dad's number updated:", quick_contacts["Dad"])
quick_contacts["Dentist"] = "555-2222"

print(quick_contacts)

del quick_contacts["Pizza Place"]
old_work = quick_contacts["Work"]
quick_contacts.pop("Work")
print("Removed work number:", old_work)

print(len(quick_contacts))
print(quick_contacts.keys())
print(quick_contacts.values())
print(list(quick_contacts))

# phase 2

total_minutes = {}

for contact, months in call_log.items():
    num_months = len(months)
    total = sum(months.values())
    average = total / num_months
    busiest_month = max(months, key=months.get)
    busiest_minutes = months[busiest_month]

    total_minutes[contact] = total

    print(f"{contact}: {num_months} month(s), {total} min total, avg: {average:.2f}, busiest: {busiest_month} ({busiest_minutes})")


total_minutes = {
    'Mom': 355, 'Dad': 135, 'Sister': 150, 'Best Friend': 600,
    'Roommate': 40, 'Boss': 225, 'Professor': 55, 'Dentist': 10
}

month_stats = {}

for contact, months in call_log.items():
    for month, minutes in months.items():
        if month not in month_stats:
            month_stats[month] = {"minutes": [], "total": 0, "avg": 0.0, "contacts": 0}
        month_stats[month]["minutes"].append(minutes)

for month, stats in month_stats.items():
    stats["total"] = sum(stats["minutes"])
    stats["contacts"] = len(stats["minutes"])
    stats["avg"] = stats["total"] / stats["contacts"]

print("=== Phase 3: Monthly Stats ===")
for month, stats in sorted(month_stats.items(), key=lambda item: item[1]["avg"], reverse=True):
    print(f"{month}: {stats['contacts']} contact(s), {stats['total']} min total, avg: {stats['avg']:.2f}")


month_stats = {
    'Jan': {'minutes': [120, 45, 80, 200, 60, 10], 'total': 515, 'avg': 85.83, 'contacts': 6},
    'Feb': {'minutes': [95, 60, 180, 15, 90, 20], 'total': 460, 'avg': 76.67, 'contacts': 6},
    'Mar': {'minutes': [140, 30, 70, 220, 25, 75, 35], 'total': 595, 'avg': 85.0, 'contacts': 7},
}

# phase 3

minutes_by_category = {}
minutes_by_city = {}
contacts_per_city = {}

for contact, minutes in total_minutes.items():
    details = contact_book[contact]
    category = details["category"]
    city = details["city"]

    minutes_by_category[category] = minutes_by_category.get(category, 0) + minutes
    minutes_by_city[city] = minutes_by_city.get(city, 0) + minutes
    contacts_per_city[city] = contacts_per_city.get(city, 0) + 1

print("=== Phase 3: Aggregations ===")
print("Monthly summary (sorted by average, highest first):")
for month, stats in sorted(month_stats.items(), key=lambda item: item[1]["avg"], reverse=True):
    print(f"{month}: {stats['total']} min total, {stats['avg']:.2f} avg ({stats['contacts']} contacts)")

print(f"Minutes by category: {minutes_by_category}")
print(f"Minutes by city: {minutes_by_city}")
print(f"Contacts per city: {contacts_per_city}")

contact_book = {
    "Mom": {"category": "Family", "city": "Fort Wayne"},
    "Dad": {"category": "Family", "city": "Fort Wayne"},
    "Sister": {"category": "Family", "city": "Chicago"},
    "Best Friend": {"category": "Friend", "city": "Indianapolis"},
    "Roommate": {"category": "Friend", "city": "Fort Wayne"},
    "Boss": {"category": "Work", "city": "Chicago"},
    "Professor": {"category": "Work", "city": "Fort Wayne"},
    "Dentist": {"category": "Business", "city": "Indianapolis"},
}

# phase 4

phone_numbers = {
    "Mom": "555-1234",
    "Dad": "555-4321",
    "Sister": "555-7777",
    "Best Friend": "555-8888",
    "Roommate": "555-3141",
    "Boss": "555-0000",
    "Professor": "555-2718",
    "Dentist": "555-2222",
}

phone_book = {name: phone_numbers[name] for name in contact_book}

local_contacts = {name: phone_numbers[name] for name, details in contact_book.items() if details["city"] == "Fort Wayne"}

activity_level = {name: ("Frequent" if minutes >= 200 else "Occasional") for name, minutes in total_minutes.items()}

print("=== Phase 4: Comprehensions ===")
print("Phone book:", phone_book)
print("Local contacts (Fort Wayne):", local_contacts)
print("Activity level:", activity_level)

# phase 5

def get_tier(minutes):
    if minutes >= 400:
        return "Platinum"
    elif minutes >= 200:
        return "Gold"
    elif minutes >= 100:
        return "Silver"
    elif minutes >= 50:
        return "Bronze"
    else:
        return "Inactive"

print("=== Phase 5: Tier Report ===")
for name, minutes in total_minutes.items():
    tier = get_tier(minutes)
    print(f"{name}: {minutes} min ({tier})")

# --- Part B: Count ---
platinum_count = 0
gold_count = 0
silver_count = 0
bronze_count = 0
inactive_count = 0

for name, minutes in total_minutes.items():
    tier = get_tier(minutes)
    if tier == "Platinum":
        platinum_count += 1
    elif tier == "Gold":
        gold_count += 1
    elif tier == "Silver":
        silver_count += 1
    elif tier == "Bronze":
        bronze_count += 1
    else:
        inactive_count += 1

print("--- Tier Distribution ---")
print(f"Platinum: {platinum_count}")
print(f"Gold: {gold_count}")
print(f"Silver: {silver_count}")
print(f"Bronze: {bronze_count}")
print(f"Inactive: {inactive_count}")

# --- Part C: Rank ---
most_name = None
most_minutes = -1
least_name = None
least_minutes = float("inf")
grand_total = 0

for name, minutes in total_minutes.items():
    if minutes > most_minutes:
        most_minutes = minutes
        most_name = name
    if minutes < least_minutes:
        least_minutes = minutes
        least_name = name
    grand_total += minutes

average = grand_total / len(total_minutes)

print("--- Top and Bottom ---")
print(f"Most contacted: {most_name} ({most_minutes} min)")
print(f"Least contacted: {least_name} ({least_minutes} min)")
print(f"Total minutes: {grand_total}")
print(f"Average per contact: {average:.2f}")

print("--- Above Average Contacts ---")
for name, minutes in total_minutes.items():
    if minutes > average:
        print(f"{name}: {minutes}")

# phase 6

def get_tier(minutes):
    if minutes >= 400:
        return "Platinum"
    elif minutes >= 200:
        return "Gold"
    elif minutes >= 100:
        return "Silver"
    elif minutes >= 50:
        return "Bronze"
    else:
        return "Inactive"

print("=== Phase 6: Contact Hub Report ===")
header = f"{'Name':<14}{'Category':<10}{'City':<14}{'Minutes':>8} {'Tier':<10}"
print(header)
print("-" * 57)

for name, minutes in sorted(total_minutes.items(), key=lambda item: item[1], reverse=True):
    details = contact_book[name]
    category = details["category"]
    city = details["city"]
    tier = get_tier(minutes)
    print(f"{name:<14}{category:<10}{city:<14}{minutes:>8} {tier:<10}")

print("-" * 57)

num_contacts = len(total_minutes)
grand_total = sum(total_minutes.values())
average = grand_total / num_contacts

print(f"{num_contacts} contacts | {grand_total} total minutes | {average:.2f} average")