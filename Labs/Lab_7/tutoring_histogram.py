# Tutoring Attendance Histogram
#
# How many students came to tutoring each day of the week?

# student names
#    keys: (str) studentID
#    value: (list) [last, first]
student_names = { 'be621':['Brown','Ella'],
                  'ff100':['Fitzroy','Farrah'],
                  'gm318':['Graham','Moses'],
                  'ik992':['Ingalls','Kelsey'],
                  'tc51':['Taylor','Cora'],
                  'sj281':['Smith','James'],
                  'sj152':['Smith','Joe'],
                  'rh150':['Ricks','Hunter'],
                  'wm97':['Wong','Ming'],
                  'jd437':['Jones','Devante'],
                  'kc870':['Kumar','Chahna'],
                  'mp411':['Malley','Patrick'],
                  'na559':['Ng','Amy'],
                  'mx672':['Morales','Xavier']
                }

# How many students came to tutoring each day?
#   keys: (str) Monday, Tuesday, Wednesday, Thursday, Friday
#   value: (int) count of students who came that day
students_per_day = {}

# How many days per week did each student attend tutoring?
#   keys: (str) studentID
#   value: (int) number of days the student went to tutoring this week
days_per_student = {}

# -------------------------------------------------------------------------------
# DO NOT MODIFY ABOVE THIS LINE
# -------------------------------------------------------------------------------

def reset_weekly_data():
    '''
    Clear both students_per_day and days_per_student.
    Both should be empty.
    '''
    global students_per_day, days_per_student
    students_per_day.clear()
    days_per_student.clear()

    # TODO - write this function's body

    return

# -------------------------------------------------------------------------------

def add_attendance_data( studentID, day ):
    '''
    Add attendance data.
    Updates the students per day dictionary.
    Updates the days per student dictionary.

    parameters: studentID (str)
                day (str)

    returns: no return value
    '''

    

    # TODO - write this function's body

    
    if day not in students_per_day:
        students_per_day[day] = 1
    else:
        students_per_day[day] += 1 
    
    if studentID  not in days_per_student:
        days_per_student[studentID] = 1
    else:
        days_per_student[studentID] += 1

    

    return

# --------------------------------------------------------------------------------

def print_day_histogram():
    '''
    Print a histogram showing how many students
    attended tutoring each day of the week.

    parameters: no parameters

    returns: no return value
    '''
    dictionary = ['Monday','Tuesday','Wednesday','Thursday', 'Friday']

    print( 'students per day\n' )
    
    # TODO - write code that prints the histogram
    for day in dictionary:
        if day in students_per_day:
            string = str(day[0:3:]) +': '
            for i in range(students_per_day[day]):
                string += '#'
            print(string)
        else:
            print(f'{str(day[0:3:])}: ')
        

        
    print( '' )

    return

# ---------------------------------------------------------------------------------

def print_attendance_report():
    '''
    Print a tutoring attendance report for the week.
    Alphabetical order by studentID
    studentID TWO SPACES First Last ONE SPACE days attended

    field width
    5 studentID
    20 First Last
    1 days attended
    '''

    print( 'attendance report\n' )
    
    # TODO - write code that prints the attendance report
    for id in sorted(student_names.keys()):
        if id in days_per_student:
            name = f'{student_names[id][1]} {student_names[id][0]}'
            print(f'{id:<5}  {name:<20} {days_per_student[id]}')
        else:
            name = f'{student_names[id][1]} {student_names[id][0]}'
            print(f'{id:<5}  {name:<20} 0')
            


        

    print( '' )

    return

# ----------------------------------------------------------------------------------
# DO NOT MODIFY BELOW THIS LINE
# ----------------------------------------------------------------------------------

def read_data_file( filename ):

    datafile = open( filename, "r" )

    textline = datafile.readline()
    while textline != '':
        studentID, day = textline.split()
        add_attendance_data( studentID, day )
        textline = datafile.readline()

    datafile.close()

    return

# ----------------------------------------------------------------------------------

def test( filename ):

    reset_weekly_data()
    read_data_file( filename )
    print_attendance_report()
    print_day_histogram()

    return

# ----------------------------------------------------------------------------------

def main():

    print( "choose a week (1-3): ", end="" )
    choice = int(input(''))
    print( '' )

    if choice == 1:
        test( 'test_data_1.txt' )
    elif choice == 2:
        test( 'test_data_2.txt' )
    else:
        test( 'test_data_3.txt' )

    return


if __name__ == '__main__':
    main()
    
