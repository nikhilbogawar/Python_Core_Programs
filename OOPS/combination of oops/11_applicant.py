# 11.
# Create:
# • Class Applicant with private skills list
# • Overload:
# o + to add skill
# o - to remove skill
# o == to compare applicants who have identical skill sets
# • Use inheritance to create ExperiencedApplicant with additional fields
class Applicant:
    def __init__(self):
        self.__skills = []
    def __add__(self, skill):
        self.__skills.append(skill)
        return self
    def __sub__(self, skill):
        if skill in self.__skills:
            self.__skills.remove(skill)
        return self
    def __eq__(self, other):
        return set(self.__skills) == set(other.__skills)
class ExperiencedApplicant(Applicant):
    def __init__(self, exp_years):
        super().__init__()
        self.exp_years = exp_years
a1 = Applicant() + "Python" + "SQL"
a2 = Applicant() + "Python" + "SQL"
print(a1 == a2)