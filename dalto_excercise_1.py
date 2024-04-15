#Ejercicio
#diferenciar el curso actual (1.5H) de:

#el curso más rapido(2.5)
#el curso promedio(4H)
#el curso mas lento(7H)

#Procentaje de material inservible que se reduce en:

#El curso actual(3.5)
#el curso promedio(5H)

#ver 10 horaa de este curso a cuantas horas de otros cursos equivale?

dalto_course = 1.5
speed_percentage_1 = 0
speed_percentage_2 = 0
speed_percentage_3 = 0
time_percentage = 0

#data for first operation
fastest_course = 2.5
promedy_course  = 4
slowest_course = 7

#data for second operation
trash_content_dalto_course = 3.5
trash_content_other_courses = 5

#We calculate the first percentage
speed_percentage_1= ((fastest_course - dalto_course) / fastest_course) * 100

#And print the percentage in screen
print(f"Dalto's course is {speed_percentage_1}% fastest that the fastest other python courses")

print("-------------")#Indent

#We calculate the second percentage
speed_percentage_2 = ((promedy_course - dalto_course) / promedy_course) * 100

#And print the percentage in screen
print(f"Dalto's course is {speed_percentage_2}% fastest that the promedy other python courses")

print("-------------")#Indent

#We calculate the third percentage 
speed_percentage_3 = ((slowest_course - dalto_course) * 1000 // slowest_course) / 10 

#And print the percentage in screen
print(f"Dalto's course is {speed_percentage_3}% fastest that the slowest other python courses")

print("-------------")#Indent

#Time percentage saved in dalto course
time_percentage = ((trash_content_dalto_course - dalto_course) * 1000 // trash_content_dalto_course) / 10

#We print the percentage
print(f"The saved time respect the trash content of dalto course it's {time_percentage}%%")

print("-------------")#Indent

#Time percentage saved in fastest course
time_percentage = ((trash_content_dalto_course - fastest_course) * 1000 // trash_content_dalto_course) / 10

#We print the percentage 
print(f"The saved time respect the trash content & the fastest course it's {time_percentage}%")

print("-------------")#Indent

#Time percentage saved in promedy course
time_percentage = ((trash_content_dalto_course - promedy_course) * 1000 // trash_content_dalto_course) / 10


#We calculate how many time are 10 hours of other courses respect the daltor course:

#ten hours of fastest respect dalto's course
time_percentage = 10 - (speed_percentage_1 * 10 // 10) / 10

#We show the hours
print(f"Ten hours of fastest course are equal to {time_percentage} hours of dalto's course")

print("-------------")#Indent

#ten hours respect the promedy course 
time_percentage = 10 - (speed_percentage_2 * 10 // 10) / 10

#We show the hours
print(f"Ten hours of promedy course are equal to {time_percentage} hours of dalto's course")

print("-------------")#Indent

#ten hours respect the slowestcourse 
time_percentage = 10 - (speed_percentage_3 * 10 // 10) / 10

#We show the hours
print(f"Ten hours of slowest course are equal to {time_percentage} hours of dalto's course")

print("-------------")#Indent


#We calculate how many time are 10 hours of this course respect the other courses:

#ten hours respect the fastest course
time_percentage = 10 + (speed_percentage_1 * 10 // 10) / 10

#We show the hours
print(f"Ten hours of dalto's course are equal to {time_percentage} hours of fastest course")

print("-------------")#Indent

#ten hours respect the promedy course 
time_percentage = 10 + (speed_percentage_2 * 10 // 10) / 10

#We show the hours
print(f"Ten hours of dalto's course are equal to {time_percentage} hours of promedy course")

print("-------------")#Indent

#ten hours respect the slowestcourse 
time_percentage = 10 + (speed_percentage_3 * 10 // 10) / 10

#We show the hours
print(f"Ten hours of dalto's course are equal to {time_percentage} hours of slowest course")