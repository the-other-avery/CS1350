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

class CardioWorkout(Workout):
    def __init__(self, name, duration_minutes, date, avg_heart_rate):
        super().__init__(name, duration_minutes, date)
        self.avg_heart_rate = avg_heart_rate

    def calories_burned(self):
        return self.duration_minutes * (self.avg_heart_rate / 100) * 5

    @property
    def intensity(self):
        if self.avg_heart_rate >= 150:
            return "High"
        elif self.avg_heart_rate >= 120:
            return "Moderate"
        else:
            return "Low"


class StrengthWorkout(Workout):
    def __init__(self, name, duration_minutes, date, sets, reps_per_set, weight_lbs):
        super().__init__(name, duration_minutes, date)
        self.sets = sets
        self.reps_per_set = reps_per_set
        self.weight_lbs = weight_lbs

    def calories_burned(self):
        return self.sets * self.reps_per_set * (self.weight_lbs / 100) * 3

    @property
    def total_volume(self):
        return self.sets * self.reps_per_set * self.weight_lbs

if __name__ == "__main__":
    w = Workout("Benchpress", 45, "2026-02-23")
    print(w)

    try:
        w.duration_minutes = 0
    except ValueError as e:
        print(e)
