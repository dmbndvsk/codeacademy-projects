class School:

    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_numberOfStudents(self):
        return self.numberOfStudents

    def set_numberOfStudents(self, new_numberOfStudents):
        self.numberOfStudents = new_numberOfStudents

    def __repr__(self):
        return(f"A {self.level} school name {self.name} with {self.numberOfStudents} students.")


my_school = School('No 9', 'high', 100)
print(my_school)
print(my_school.get_name())
print(my_school.get_level())
print(my_school.get_numberOfStudents())
my_school.set_numberOfStudents(200)
print(my_school.get_numberOfStudents())\



class PrimarySchool(School):

    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, "primary", numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def get_pickup(self):
        return self.pickupPolicy

    def pickupPolicy(self):
        return "Pickup after 3pm"

    def __repr__(self):
        super().__repr__()
        return (f"A {self.level} school name {self.name} with {self.numberOfStudents} students. {self.pickupPolicy}")


my_primary = PrimarySchool('No 53', 100, "Pickup Allowed")
print(my_primary.get_pickup())
print(my_primary)


class HighSchool(School):

    def __init__(self, name, numberOfStudents, sportsTeams):
        super().__init__(name, 'high', numberOfStudents)
        self.sportsTeams = sportsTeams

    def get_sportsTeams(self):
        return ['MU', 'Arsenal', 'Chealsea']

    def __repr__(self):
        super().__repr__()
        return (f"A {self.level} school name {self.name} with {self.numberOfStudents} students. There are a lot of sports teams like: {self.sportsTeams}")


my_high = HighSchool('No 99', 500, ['TTH', 'Wolves', 'Everton'])
print(my_high.get_sportsTeams())
print(my_high)
