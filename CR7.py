CourseRoom = {'CSC101':'3004',
              'CSC102': '4501',
              'CSC103': '6755',
              'NET110':'1244',
              'COM241':'1411'}

CourseInstructor = {'CSC101':'Haynes',
              'CSC102': 'Alvarado',
              'CSC103': 'Rich',
              'NET110':'Burke',
              'COM241':'Lee'}

CourseTime = {'CSC101':'8:00 a.m.',
              'CSC102': '9:00 a.m',
              'CSC103': '10:00 a.m.',
              'NET110':'11:00 a.m.',
              'COM241':'1:00 a.m.'}

CourseNumber = input('Enter the course number.')

if CourseNumber in CourseRoom:
    print('Room Number: {}'.format(CourseRoom[CourseNumber]))
else:
    print('Room number not available')

if CourseNumber in CourseInstructor:    
    print('Instructor: {}'.format(CourseInstructor[CourseNumber]))
else:
    print('Instructor not available')

if CourseNumber in CourseInstructor:
    print('Course Time: {}'.format(CourseTime[CourseNumber]))
else:
    print('Course time not available')