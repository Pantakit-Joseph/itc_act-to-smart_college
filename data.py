from pprint import pprint
import getData
import csv
import pandas as pd


def saveMajors():
    majors = getData.getMajors()
    with open('data/majors.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # add group row number
        for index, item in enumerate(majors):
            majors[index].insert(0, index + 1)
        writer.writerow(['id_run', 'id', 'major_code', 'major_name', 'major_eng'])
        writer.writerows(majors)
    # pprint(majors)


def loadDataMajors():
    with open('data/majors.csv', 'r', encoding='UTF8') as f:
        majors = [row for row in csv.reader(f)]
        del majors[0]
    return majors


def saveMinors():
    minors = getData.getMinors()
    majors = loadDataMajors()
    major_id_dict = {str(major[1]): str(major[0]) for major in majors}
    with open('data/minors.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # add group row number
        for index, item in enumerate(minors):
            minors[index].insert(0, index + 1)
            minor_id_run = major_id_dict.get(str(minors[index][5]), '')
            minors[index].insert(1, minor_id_run)

        writer.writerow(['id_run', 'major_id_run', 'id', 'minor_code', 'minor_name', 'minor_eng', 'major_id'])
        writer.writerows(minors)
    # pprint(minors)


def loadDataMinors():
    with open('data/minors.csv', 'r', encoding='UTF8') as f:
        minors = [row for row in csv.reader(f)]
        del minors[0]
    return minors


def saveGroups():
    groups = getData.getGroups()
    minors = loadDataMinors()
    minor_id_dict = {str(minor[2]): str(minor[0]) for minor in minors}
    with open('data/groups.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # add group row number
        for index, item in enumerate(groups):
            groups[index].insert(0, index + 1)
            minor_id_run = minor_id_dict.get(str(groups[index][4]), '')
            groups[index].insert(1, minor_id_run)
        writer.writerow(['id_run', 'minor_id_run', 'id', 'group_code', 'group_name', 'minor_id'])
        writer.writerows(groups)
    # pprint(groups)


def saveUsers():
    users = getData.getUsers()
    with open('data/users.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        for index, item in enumerate(users):
            users[index].insert(0, index + 1)
        writer.writerow(['id_run', 'id', 'username', 'password', 'email', 'firstname', 'lastname', 'user_type'])
        writer.writerows(users)
    # pprint(users)


def loadDataUsers():
    with open('data/users.csv', 'r', encoding='UTF8') as f:
        users = [row for row in csv.reader(f)]
        del users[0]
    return users


def saveUsersStudent():
    students = getData.getUsersStudent()
    users = loadDataUsers()

    user_id_dict = {str(user[1]): str(user[0]) for user in users}
    with open('data/users_student.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        for index, student in enumerate(students):
            students[index].insert(0, index + 1)
            user_id_run = user_id_dict.get(str(student[2]), '')

            students[index].insert(1, user_id_run)

        writer.writerow(['id_run', 'user_id_run', 'id', 'user_id', 'student_id', 'group_id'])
        writer.writerows(students)
    # pprint(students)


def saveUsersAdvisor():
    advisors = getData.getUsersAdvisor()
    users = loadDataUsers()
    majors = loadDataMajors()
    user_id_dict = {str(user[1]): str(user[0]) for user in users}
    major_id_dict = {str(major[1]): str(major[0]) for major in majors}
    with open('data/users_advisor.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        for index, advisor in enumerate(advisors):
            advisors[index].insert(0, index + 1)
            user_id_run = user_id_dict.get(str(advisor[2]), '')
            advisors[index].insert(1, user_id_run)
            major_id_run = major_id_dict.get(str(advisor[4]), '')
            advisors[index].insert(2, major_id_run)
        writer.writerow(['id_run', 'user_id_run', 'major_id_run', 'id', 'user_id', 'major_id'])
        writer.writerows(advisors)


def saveUsersHeaddepartment():
    headdepartments = getData.getUsersHeaddepartment()
    users = loadDataUsers()
    majors = loadDataMajors()
    user_id_dict = {str(user[1]): str(user[0]) for user in users}
    major_id_dict = {str(major[1]): str(major[0]) for major in majors}
    with open('data/users_headdepartment.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        for index, headdepartment in enumerate(headdepartments):
            headdepartments[index].insert(0, index + 1)
            user_id_run = user_id_dict.get(str(headdepartment[2]), '')
            headdepartments[index].insert(1, user_id_run)
            major_id_run = major_id_dict.get(str(headdepartment[4]), '')
            headdepartments[index].insert(2, major_id_run)
        writer.writerow(['id_run', 'user_id_run', 'major_id_run', 'id', 'user_id', 'major_id'])
        writer.writerows(headdepartments)


def loadDataUsersStudent():
    with open('data/users_student.csv', 'r', encoding='UTF8') as f:
        users = [row for row in csv.reader(f)]
        del users[0]
    return users


def loadDataGroups():
    with open('data/groups.csv', 'r', encoding='UTF8') as f:
        groups = [row for row in csv.reader(f)]
        del groups[0]
    return groups


def saveStudentsGroups():
    students = loadDataUsersStudent()
    groups = loadDataGroups()
    student_groups = [[i[1], i[5], '2'] for i in students]
    group_id_dict = {str(group[2]): str(group[0]) for group in groups}
    with open('data/students_groups.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        for index, student in enumerate(student_groups):
            student_groups[index].insert(0, index + 1)
            group_id_run = group_id_dict.get(str(student[2]), '')
            student_groups[index].insert(1, group_id_run)

        writer.writerow(['id', 'group_id_run', 'student_id', 'group_id', 'semester_id'])
        writer.writerows(student_groups)


def saveAdvisorsGroups():
    advisors_groups = getData.getAdvisorsGroups()
    users = loadDataUsers()
    groups = loadDataGroups()
    user_id_dict = {str(user[1]): str(user[0]) for user in users}
    group_id_dict = {str(group[2]): str(group[0]) for group in groups}
    with open('data/advisors_groups.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        for index, item in enumerate(advisors_groups):
            advisors_groups[index].insert(0, index + 1)
            advisor_id_run = user_id_dict.get(str(item[2]), '')
            advisors_groups[index].insert(1, advisor_id_run)
            group_id_run = group_id_dict.get(str(item[4]), '')
            advisors_groups[index].insert(2, group_id_run)

        writer.writerow(['id_run', 'advisor_id_run', 'group_id_run', 'id', 'advisor_id', 'group_id', 'advisor_type'])
        writer.writerows(advisors_groups)


def loadDataDegreeLevel():
    with open('data/degree_level.csv', 'r', encoding='UTF8') as f:
        degree_level = [row for row in csv.reader(f)]
        del degree_level[0]
    return degree_level


def loadDataSemester():
    with open('data/semester.csv', 'r', encoding='UTF8') as f:
        semester = [row for row in csv.reader(f)]
        del semester[0]
    return semester
