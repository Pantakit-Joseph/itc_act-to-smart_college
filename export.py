from pprint import pprint
import data
from generate import generate_username


def generateSQL(table_name, columns, rows):
    columns = ['`{}`'.format(column) for column in columns]
    sql = f'INSERT INTO `{table_name}` ({", ".join(columns)}) VALUES\n'
    data_rows = ["({})".format(', '.join([value for value in item])) for item in rows]
    sql += ',\n'.join(data_rows)
    sql += ';'
    return sql


def degreeLevelSQL():
    degree_level = data.loadDataDegreeLevel()
    columns = ['id', 'degreelevel_code', 'degreelevel_name', 'degreelevel_abbrev']
    rows = [[f'\'{i[0]}\'', f'\'{i[1]}\'', f'\'{i[2]}\'', f'\'{i[3]}\''] for i in degree_level]
    sql = generateSQL('degreelevel', columns, rows)
    write_file(sql, 'output/degree_level.sql')
    append_file(sql, 'output/all.sql')


def semesterSQL():
    semesters = data.loadDataSemester()
    columns = ['id', 'semester_no', 'semester_year', 'created_at', 'updated_at', 'status']
    rows = [[f'\'{i[0]}\'', f'\'{i[1]}\'', f'\'{i[2]}\'', "NOW()", "NOW()", f'\'{i[3]}\''] for i in semesters]
    sql = generateSQL('semester', columns, rows)
    write_file(sql, 'output/semester.sql')
    append_file(sql, 'output/all.sql')


def majorsSQL():
    majors = data.loadDataMajors()
    columns = ['id', 'major_code', 'major_name', 'major_eng', 'created_at', 'updated_at', 'status']
    rows = [[f'\'{i[0]}\'', f'\'{i[2]}\'', f'\'{i[3]}\'', f'\'{i[4]}\'', "NOW()", "NOW()", '1'] for i in majors]
    sql = generateSQL('majors', columns, rows)
    write_file(sql, 'output/majors.sql')
    append_file(sql, 'output/all.sql')


def minorsSQL():
    minors = data.loadDataMinors()
    columns = ['id', 'minor_code', 'minor_name', 'minor_eng', 'major_id', 'created_at', 'updated_at', 'status']
    rows = [[f'\'{i[0]}\'', f'\'{i[3]}\'', f'\'{i[4]}\'', f'\'{i[5]}\'', f'\'{i[1]}\'', "NOW()", "NOW()", '1'] for i in
            minors]
    sql = generateSQL('minors', columns, rows)
    write_file(sql, 'output/minors.sql')
    append_file(sql, 'output/all.sql')


def groupsSQL():
    groups = data.loadDataGroups()
    columns = ['id', 'group_code', 'group_name', 'degreelevel_id', 'minor_id', 'created_at', 'updated_at', 'status']
    rows = []
    for i in groups:
        g_name = str(i[4]).strip()
        de_id = ''
        match g_name[0]:
            case 'A':
                de_id = '4'
            case 'B':
                de_id = '4'
            case 'C':
                de_id = '4'
            case 'D':
                de_id = '6'
            case 'E':
                de_id = '6'
            case _:
                de_id = ''
        rows.append([f'\'{i[0]}\'', f'\'{i[3]}\'', f'\'{i[4]}\'', f'\'{de_id}\'', f'\'{i[1]}\'', "NOW()", "NOW()", '1'])
    sql = generateSQL('groups', columns, rows)
    write_file(sql, 'output/groups.sql')
    append_file(sql, 'output/all.sql')


def usersSQL():
    users = data.loadDataUsers()
    columns = ['id', 'username', 'email', 'password', 'firstname', 'lastname', 'user_type', 'created_at', 'updated_at',
               'status']
    rows = [
        [f'\'{i[0]}\'', f'\'{i[7] + i[0]}\'', f'\'{i[7] + i[0] + "@demo.com"}\'', f'\'{i[3]}\'', f'\'{i[5]}\'',
         f'\'{i[6]}\'',
         f'\'{i[7]}\'',
         "NOW()", "NOW()", '1'] for i in users]
    sql = generateSQL('users', columns, rows)
    write_file(sql, 'output/users.sql')
    append_file(sql, 'output/all.sql')


def usersStudentSQL():
    students = data.loadDataUsersStudent()
    columns = ['id', 'user_id', 'student_code', 'created_at', 'updated_at', 'status']
    rows = [[f'\'{i[0]}\'', f'\'{i[1]}\'', f'\'{i[4]}\'', "NOW()", "NOW()", '1'] for i in students]
    sql = generateSQL('users_student', columns, rows)
    write_file(sql, 'output/users_student.sql')
    append_file(sql, 'output/all.sql')


def usersAdvisorSQL():
    advisors = data.loadDataUsersAdvisor()
    columns = ['id', 'user_id', 'major_id', 'created_at', 'updated_at', 'status']
    rows = [[f'\'{i[0]}\'', f'\'{i[1]}\'', f'\'{i[2]}\'', "NOW()", "NOW()", '1'] for i in advisors]
    sql = generateSQL('users_advisor', columns, rows)
    write_file(sql, 'output/users_advisor.sql')
    append_file(sql, 'output/all.sql')


def usersHeaddepartmentSQL():
    advisors = data.loadDataUsersHeaddepartment()
    columns = ['id', 'user_id', 'major_id', 'created_at', 'updated_at', 'status']
    rows = [[f'\'{i[0]}\'', f'\'{i[1]}\'', f'\'{i[2]}\'', "NOW()", "NOW()", '1'] for i in advisors]
    sql = generateSQL('users_headdepartment', columns, rows)
    write_file(sql, 'output/users_headdepartment.sql')
    append_file(sql, 'output/all.sql')


def studentsGroupsSQL():
    students_groups = data.loadDataStudentsGroups()
    columns = ['id', 'student_id', 'group_id', 'semester_id', 'created_at', 'updated_at', 'status']
    rows = [[f'\'{i[0]}\'', f'\'{i[2]}\'', f'\'{i[1]}\'', f'\'{i[4]}\'', "NOW()", "NOW()", '1'] for i in
            students_groups]
    sql = generateSQL('students_groups', columns, rows)
    write_file(sql, 'output/students_groups.sql')
    append_file(sql, 'output/all.sql')


def advisorsGroupsSQL():
    advisors_groups = data.loadDataAdvisorsGroups()
    columns = ['id', 'advisor_id', 'group_id', 'advisor_type', 'semester_id', 'created_at', 'updated_at', 'status']
    rows = [[f'\'{i[0]}\'', f'\'{i[1]}\'', f'\'{i[2]}\'', f'\'{i[6]}\'', '2', "NOW()", "NOW()", '1'] for i in
            advisors_groups]
    sql = generateSQL('advisors_groups', columns, rows)
    write_file(sql, 'output/advisors_groups.sql')
    append_file(sql, 'output/all.sql')


def write_file(content, filename):
    f = open(filename, "w", encoding='UTF8')
    f.write(content + '\n')
    f.close()


append_file_set = set()


def append_file(content, filename):
    global append_file_set
    if not (filename in append_file_set):
        append_file_set.add(filename)
        f = open(filename, "w", encoding='UTF8')
    else:
        f = open(filename, "a", encoding='UTF8')
    f.write(content + '\n\n')
    f.close()
