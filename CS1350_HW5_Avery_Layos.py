class Workout:
    def __init__(self, name, duration_minutes, date):
        self.name = name
        self.date = date
        self.duration_minutes = duration_minutes

    @property
    def duration_minutes(self):
        return self._duration_minutes

    @duration_minutes.setter
    def duration_minutes(self, value):
        if value <= 0:
            raise ValueError("Duration must be greater than 0")
        self._duration_minutes = value

    def calories_burned(self):
        return 0

    def __str__(self):
        return f"{self.name} - {self.duration_minutes}min on {self.date} ({self.calories_burned()} cal)"


if __name__ == "__main__":
    w = Workout("Benchpress", 45, "2026-02-23")
    print(w)

    try:
        w.duration_minutes = 0
    except ValueError as e:
        print(e)