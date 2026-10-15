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