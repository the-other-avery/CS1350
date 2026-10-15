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