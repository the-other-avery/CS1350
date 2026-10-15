class Gradebook:
    def __init__(self):
        self.grades = {}

    def add_score(self, student, assignment, score):
        self.grades.setdefault(student, {})[assignment] = score

    def student_average(self, student):
        scores = self.grades.get(student)
        if not scores:
            return None
        return sum(scores.values()) / len(scores)

    def assignment_average(self, assignment):
        scores = [s[assignment] for s in self.grades.values() if assignment in s]
        if not scores:
            return None
        return sum(scores) / len(scores)

    def top_students(self, n):
        averages = {
            name: self.student_average(name)
            for name in self.grades
            if self.student_average(name) is not None
        }
        ranked = sorted(averages, key=lambda name: (-averages[name], name))
        return ranked[:n]

    def missing(self, assignment):
        return sorted(
            name for name, scores in self.grades.items()
            if assignment not in scores
        )


# Test cases
gb = Gradebook()
gb.add_score("Alice", "hw1", 90)
gb.add_score("Alice", "hw2", 80)
gb.add_score("Bob", "hw1", 70)
gb.add_score("Bob", "hw2", 60)
gb.add_score("Carol", "hw1", 100)
gb.add_score("Bob", "hw2", 75)      # overwrite
print(gb.student_average("Alice"))  # 85.0
print(gb.student_average("Bob"))    # 72.5
print(gb.student_average("Zed"))    # None
print(gb.assignment_average("hw1")) # 86.66666666666667
print(gb.assignment_average("hw9")) # None
print(gb.top_students(2))           # ['Carol', 'Alice']
print(gb.missing("hw2"))            # ['Carol']




class Door:
    def __init__(self, name):
        self.name = name
        self.cards = set()

    def grant(self, card_id):
        self.cards.add(card_id)

    def revoke(self, card_id):
        self.cards.discard(card_id)  # discard: no error if absent

    def can_open(self, card_id):
        return card_id in self.cards


def master_cards(doors):
    if not doors:
        return set()
    return set.intersection(*(d.cards for d in doors))


def single_door_cards(doors):
    counts = {}
    for d in doors:
        for c in d.cards:
            counts[c] = counts.get(c, 0) + 1
    return {c for c, n in counts.items() if n == 1}


def unused_cards(all_cards, doors):
    return set(all_cards) - set().union(*(d.cards for d in doors))


def audit(doors):
    for d in doors:
        print(f"{d.name}: {len(d.cards)} cards")
    print(f"Master cards: {master_cards(doors)}")

# Test cases
lobby = Door("Lobby")
for c in [101, 102, 103, 104]:
    lobby.grant(c)
    lab = Door("Lab")
for c in [101, 103, 105]:
    lab.grant(c)
    server = Door("Server Room")
for c in [101, 105]:
    server.grant(c)
    lab.revoke(105)
    lab.revoke(999) # no error
    print(lab.can_open(103), lab.can_open(105)) # True False
    doors = [lobby, lab, server]
    print(master_cards(doors)) # {101}
    print(single_door_cards(doors)) # {102, 104}
    print(unused_cards({101, 102, 105, 200}, doors)) # {200}
    audit(doors)
# Lobby: 4 cards
# Lab: 2 cards
# Server Room: 2 cards
# Master cards: {101}




import json

def process_readings(in_file, json_file, alert_file, limit):
    readings = {}  # sensor_id: list of values
    alerts = 0

    with open(in_file) as f, open(alert_file, "w") as out:
        for line in f:
            line = line.strip()
            if not line:
                continue
            timestamp, sensor, raw = line.split(",")
            value = float(raw)
            readings.setdefault(sensor, []).append(value)
            if value > limit:
                out.write(f"{timestamp} {sensor} {raw}\n")
                alerts += 1

    summary = {
        sensor: {
            "count": len(values),
            "average": sum(values) / len(values),
            "max": max(values),
        }
        for sensor, values in readings.items()
    }

    with open(json_file, "w") as f:
        json.dump(summary, f, indent=2)

    return alerts




from abc import ABC, abstractmethod


class Shipment(ABC):
    def __init__(self, tracking_id, weight_kg):
        Shipment.validate_weight(weight_kg)
        self.tracking_id = tracking_id
        self.weight_kg = weight_kg

    @abstractmethod
    def cost(self):
        pass

    def label(self):
        return f"{self.tracking_id} ({self.weight_kg} kg): ${self.cost():.2f}"

    @staticmethod
    def validate_weight(weight_kg):
        if weight_kg <= 0:
            raise ValueError("Weight must be positive")


class StandardShipment(Shipment):
    def __init__(self, tracking_id, weight_kg, rate_per_kg=2.00):
        super().__init__(tracking_id, weight_kg)
        self.rate_per_kg = rate_per_kg

    def cost(self):
        return self.weight_kg * self.rate_per_kg


class ExpressShipment(StandardShipment):
    def __init__(self, tracking_id, weight_kg, rate_per_kg=2.00, surcharge=10.00):
        super().__init__(tracking_id, weight_kg, rate_per_kg)
        self.surcharge = surcharge

    def cost(self):
        return super().cost() + self.surcharge


class InternationalShipment(Shipment):
    def __init__(self, tracking_id, weight_kg, country, customs_pct=0.15):
        super().__init__(tracking_id, weight_kg)
        self.country = country
        self.customs_pct = customs_pct

    def cost(self):
        return self.weight_kg * 5.00 * (1 + self.customs_pct)


def manifest(shipments):
    for s in shipments:
        print(s.label())
    total = sum(s.cost() for s in shipments)
    print(f"Total: ${total:.2f}")
    return total

# Test cases
shipments = [
    StandardShipment("S100", 4.0),
    ExpressShipment("E200", 2.5),
    InternationalShipment("I300", 3.0, country="Canada")
]
total = manifest(shipments)
# S100 (4.0 kg): $8.00
# E200 (2.5 kg): $15.00
# I300 (3.0 kg): $17.25
# Total: $40.25
try:
    Shipment.validate_weight(-1)
except ValueError as e:
    print("Caught:", e)
    # Caught: Weight must be positive




class Polynomial:
    # YOUR CODE HERE
    pass

# Test cases
p = Polynomial([1, 2, 3]) # 1 + 2x + 3x^2
q = Polynomial([0, 1]) # x
print(p) # 3x^2 + 2x + 1
print(q) # x
print(repr(p)) # Polynomial([1, 2, 3])
print(len(p)) # 3
print(p[2], p[7]) # 3 0
print(p(2)) # 17
print(q(5)) # 5
r = p + q
print(r) # 3x^2 + 3x + 1
print(p * 2) # 6x^2 + 4x + 2
print(p == Polynomial([5, 0, 1])) # True (both degree 2)
print(q < p) # True (degree 1 < degree 2)