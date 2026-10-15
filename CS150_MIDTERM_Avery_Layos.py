class Gradebook:
    def __init__(self):
        # YOUR CODE HERE
        pass
    def add_score(self, student, assignment, score):
        pass
    def student_average(self, student):
        pass
    def assignment_average(self, assignment):
        pass
    def top_students(self, n):
        pass
    def missing(self, assignment):
        pass


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