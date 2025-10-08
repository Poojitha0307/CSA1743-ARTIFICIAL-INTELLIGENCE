% student(StudentID, StudentName)
student(101, 'Alice').
student(102, 'Bob').
student(103, 'Charlie').
student(104, 'Diana').

% teacher(TeacherID, TeacherName)
teacher(201, 'Mr. Smith').
teacher(202, 'Ms. Johnson').
teacher(203, 'Dr. Brown').

% subject(SubCode, SubjectName, TeacherID)
subject('CS101', 'Computer Science', 201).
subject('MA101', 'Mathematics', 202).
subject('PH101', 'Physics', 203).
subject('CS102', 'Data Structures', 201).

% enrollment(StudentID, SubCode)
enrollment(101, 'CS101').
enrollment(101, 'MA101').
enrollment(102, 'CS101').
enrollment(102, 'PH101').
enrollment(103, 'MA101').
enrollment(104, 'CS102').
