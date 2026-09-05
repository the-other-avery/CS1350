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

# Call log: name -> {month -> minutes talked that month}
# Note: not every contact was called every month.
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