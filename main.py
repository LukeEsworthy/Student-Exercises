from cohort import Cohort
from exercise import Exercise
from instructor import Instructor
from student import Student


# Create 4 or more exercises
methods_review = Exercise("Methods Review", "Python")
classes_practice = Exercise("Practice Making Classes", "Python")
face_space = Exercise("Facespace Social Media", "React")
sleepster = Exercise("Sleepster Media Streaming", "Javascript")

# Create 3 or more cohorts
cohort_44 = Cohort("Cohort 44: The Awesome")
cohort_103 = Cohort("Cohort 103: The Brave")
cohort_113 = Cohort("Cohort 113: The Perseverant")

# Create 4 or more students, and assign them to a cohort
me = Student("Luke", "Esworthy", "lukeesworthy")
you = Student("Jim", "Bob", "JimboRox")
siri = Student("Siri", "Robot", "heysiri")
alexa = Student("Alexa", "Hola", "heyalexa")

# Create 3 or more instructors and assign them to a cohort
lupin = Instructor("Romulus", "Lupin", "howlsatthemoon",
                   "always has chocolate")
snape = Instructor("Severus", "Snape", "snivellus", "looking gloomy")
lockhart = Instructor("Gilderoy", "Lockhart",
                      "sexyandiknowit", "hair is always on point")
