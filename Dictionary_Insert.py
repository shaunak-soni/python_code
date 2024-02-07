#the below dictionary is a grade book that contains student's name as the key, and the value is results for a series of tests, from most recent to oldest.
#Write code that updates the grades dictionary by adding the newly received test result to the beginning of each list corresponding to the student. 
#If the new exam grade is missing for a student, assign the value None

#grade book 
grades = {
    'John': [90, 95, 98],
    'Eric': [86, 84, 92],
    'Michael': [90, 89, 85]
}

print(f'The original grade-book is: \n {grades}')

#Newly Received latest exam scores
exam = {
    'Eric': 99,
    'John': 100
} 

print(f'\nThe Newly Received latest exam scores are: \n {exam}')

for student in grades:
    if student in exam:
        grades[student].insert(0, exam[student])
    else:
        grades[student].insert(0, None)
        
print(f'\nThe updated grade-book is: \n {grades}')