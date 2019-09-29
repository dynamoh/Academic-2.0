import os

import xlrd
from django.contrib.auth.models import User

from applications.academic_information.models import Student
from applications.globals.models import DepartmentInfo, Designation, ExtraInfo

excel = xlrd.open_workbook(
    os.path.join(
        os.getcwd(),
        'dbinsertscripts/academics/StudentInformation.xlsx'))
z = excel.sheet_by_index(0)
# print(z.cell(5,0))
# print(z.cell(12,2).value)
#file = xlrd.open_workbook(excel,'r')

nahihua = []
for i in range(1, 1121):
    try:
        roll_no = int(z.cell(i, 0).value)
        username = roll_no

        name = (str(z.cell(i, 1).value)).split()
        first_name = str(name[0])
        programme = str(z.cell(i, 3).value)
        print(programme)
        last_name = ""
        if(len(name) > 1):
            last_name = str(name[1])
        sex = 'M'
        print(first_name, last_name)
        unique_id = int(roll_no)
        designation = 'student'
        dep = str(z.cell(i, 2).value)
        print(dep)
        department = DepartmentInfo.objects.get(name=dep)
        print(department)
        user_type = 'student'
        email = str(z.cell(i, 4).value)
        print(email)

        

        k = ExtraInfo.objects.create(
            sex=sex,
            user=u,
            id=unique_id,
            department=department,
            age=18,
            about_me='Hello I am ' + first_name + last_name,
            user_type='student',
            phone_no=9999999999
        )

        z2 = Student.objects.create(
            id=k,
            programme=programme,
            cpi=7.0,
            category='GEN',
            father_name='Mr.',
            mother_name='Mrs.',
            hall_no=4,
            specialization='None'
        )

        print(str(i) + "done")
    except Exception as e:
        print(e)
        print(i)
        nahihua.append(i)

print(nahihua)
