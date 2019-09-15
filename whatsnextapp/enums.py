from django_enumfield import enum

class RequirementLevel(enum.Enum):
    SSC = 0
    HSC = 1
    BOTH = 2

class SchoolLevel(enum.Enum):
    SSC = 0
    HSC = 1

class Discipline(enum.Enum):
    SCIENCE = 0
    COMMERCE = 1
    ARTS = 2
    COMMON = 3

class DegreeLevel(enum.Enum):
    BACHELORS = 0
    MASTERS = 1

class VarsityCategory(enum.Enum):
    PUBLIC = 0
    PRIVATE = 1

class DepartmentCategory(enum.Enum):
    SCIENCE = 0
    COMMERCE = 1
    ARTS = 2

class RequirementType(enum.Enum):
    GRADE = 0
    YEAR = 1
    SUBJECTWISE = 2
    SUBJECTWISETOTAL = 3