from pprint import pprint
import csv
import pandas as pd
import data
import getData
import export
import uuid

# data.saveMajors()
# data.saveMinors()
# data.saveGroups()
# data.saveUsers()
# data.saveUsersStudent()
# data.saveUsersAdvisor()
# data.saveUsersHeaddepartment()
# data.saveStudentsGroups()
# data.saveAdvisorsGroups()

export.degreeLevelSQL()
export.semesterSQL()
export.majorsSQL()
export.minorsSQL()
export.groupsSQL()
export.usersSQL()
export.usersStudentSQL()
export.usersAdvisorSQL()
export.usersHeaddepartmentSQL()
export.studentsGroupsSQL()
export.advisorsGroupsSQL()
