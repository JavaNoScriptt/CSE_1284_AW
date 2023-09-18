## This is an exceise to make use of 2-d list and loops

tanscript = []


loops = int(input('How Many courses did you take last semester?? \t'))

for i in range(0,loops):
    print(f'Enter data for course {i+1}')
    dept = input('Dept.\t')
    course_num = int(input('Course Number:\t'))
    class_name = input('Class Name:\t')
    grade = input('Grade:\t')
    tanscript.append([dept,course_num,class_name,grade])
    print()


for x in tanscript:
    print(f'''dept.:{x[0]}
number: {x[1]}  
title: {x[2]}  
Grade: {x[3]}''')


print(tanscript)