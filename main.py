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

me.cohort = "cohort_44"
you.cohort = "cohort_113"
siri.cohort = "cohort_44"
alexa.cohort = "cohort_103"

# Create 3 or more instructors and assign them to a cohort
lupin = Instructor("Romulus", "Lupin", "howlsatthemoon",
                   "always there if you need chocolate")
snape = Instructor("Severus", "Snape", "snivellus", "looking gloomy")
lockhart = Instructor("Gilderoy", "Lockhart",
                      "sexyandiknowit", "always looking fresh")

lupin.cohort = "cohort_44"
snape.cohort = "cohort_113"
lockhart.cohort = "cohort_103"


# Have each instructor assign 2 exercises to each of the students
lupin.assign_exercise(me, methods_review)
lupin.assign_exercise(me, classes_practice)
lupin.assign_exercise(you, methods_review)
lupin.assign_exercise(you, classes_practice)
lupin.assign_exercise(siri, methods_review)
lupin.assign_exercise(siri, classes_practice)
lupin.assign_exercise(alexa, methods_review)
lupin.assign_exercise(alexa, classes_practice)

snape.assign_exercise(me, face_space)
snape.assign_exercise(me, sleepster)
snape.assign_exercise(you, face_space)
snape.assign_exercise(you, sleepster)
snape.assign_exercise(siri, face_space)
snape.assign_exercise(siri, sleepster)
snape.assign_exercise(alexa, face_space)
snape.assign_exercise(alexa, sleepster)

lockhart.assign_exercise(me, methods_review)
lockhart.assign_exercise(me, face_space)
lockhart.assign_exercise(you, methods_review)
lockhart.assign_exercise(you, face_space)
lockhart.assign_exercise(siri, methods_review)
lockhart.assign_exercise(siri, face_space)
lockhart.assign_exercise(alexa, methods_review)
lockhart.assign_exercise(alexa, face_space)


for exercise in me.exercises:
    print(exercise)
