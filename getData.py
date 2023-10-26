from connnect import db


# from pprint import pprint


def getStudents():
    sql = """
    SELECT 
        `users_student`.`user_id`,
        `users_student`.`firstname`,
        `users_student`.`lastname`,
        `users_student`.`email`,
        `users_student`.`student_id`,
        `groups`.`group_name`,
        `minors`.`minor_name`,
        `majors`.`major_name`
    FROM `users_student` 
    INNER JOIN `groups` ON `groups`.`id`=`users_student`.`group_id`
    INNER JOIN `minors` ON `minors`.`id`=`groups`.`minor_id`
    INNER JOIN `majors` ON `majors`.`id`=`minors`.`major_id`
    WHERE 
        `users_student`.`status`=1
        AND `groups`.`status`=1
        AND `minors`.`status`=1
        AND `majors`.`status`=1
    """
    db.execute(sql)

    result = db.fetchall()
    result = list(result)

    for i in range(len(result)):
        result[i] = list(result[i])
        for n in range(len(result[i])):
            if type(result[i][n]) is str:
                result[i][n] = result[i][n].replace(
                    '\n', '').replace('\r', '').replace(' ', '')

            result[i][3] = result[i][3].replace('ุ', '')
            result[i][4] = result[i][4].replace('ุ', '')

    return result


def getGroups():
    sql = """
    SELECT `id`, `group_code`, `group_name`, `minor_id` FROM `groups` WHERE `status`!=-1;
    """
    db.execute(sql)

    result = db.fetchall()
    result = list(result)
    result = [list(i) for i in result]

    return result


def getMajors():
    sql = """
    SELECT `id`, `major_code`, `major_name`, `major_eng` FROM `majors` WHERE `status`=1
    """
    db.execute(sql)

    result = db.fetchall()
    result = list(result)
    result = [list(i) for i in result]

    return result


def getMinors():
    sql = """
    SELECT `id`, `minor_code`, `minor_name`, `minor_eng`, `major_id` FROM `minors` WHERE `status`=1
    """
    db.execute(sql)

    result = db.fetchall()
    result = list(result)
    result = [list(i) for i in result]

    return result


def getUsers():
    sql = """
        SELECT 
            `id`, 
            `username`, 
            '$2y$10$3Rrp21DZXiQtqaRBAOX5qOct3TvstP60d.CVc42UR.FFTJO83mAKW' AS `password`, 
            `email`, 
            `firstname`, 
            `lastname`,
            `user_type` 
        FROM `users`
        WHERE `user_type` NOT IN ('headadvisor')
        """
    db.execute(sql)

    result = db.fetchall()
    result = list(result)
    result = [list(i) for i in result]
    for i in range(len(result)):
        result[i] = list(result[i])
        for n in range(len(result[i])):
            if type(result[i][n]) is str:
                result[i][n] = result[i][n].replace(
                    '\n', '').replace('\r', '').replace(' ', '')

            result[i][3] = result[i][3].replace('ุ', '')

    return result


def getUsersStudent():
    sql = """
        SELECT `id`, `user_id`, `student_id`, `group_id` FROM `users_student` WHERE `status`=1;
        """
    db.execute(sql)

    result = db.fetchall()
    result = list(result)
    result = [list(i) for i in result]

    for i in range(len(result)):
        result[i] = list(result[i])
        for n in range(len(result[i])):
            if type(result[i][n]) is str:
                result[i][n] = result[i][n].replace(
                    '\n', '').replace('\r', '').replace(' ', '')

            result[i][2] = result[i][2].replace('ุ', '')

    return result


def getUsersAdvisor():
    sql = """
        SELECT `users_advisor`.`id`, `users_advisor`.`user_id`, `users_advisor`.`major_id`
        FROM `users_advisor`
        JOIN `users` ON `users`.`id`=`users_advisor`.`user_id`;
        """
    db.execute(sql)

    result = db.fetchall()
    result = list(result)
    result = [list(i) for i in result]

    return result


def getUsersHeaddepartment():
    sql = """
        SELECT `users_headdepartment`.`id`, `users_headdepartment`.`user_id`, `users_headdepartment`.`major_id`  FROM `users_headdepartment`
        JOIN `users` ON `users`.`id` = `users_headdepartment`.`user_id`;
        """
    db.execute(sql)
    result = db.fetchall()
    result = list(result)
    result = [list(i) for i in result]

    return result


def getAdvisorsGroups():
    sql = """
        SELECT `id`, `advisor_id`, `group_id`, `advisor_type` FROM `advisors_groups` 
        WHERE `status`=1
        """
    db.execute(sql)

    result = db.fetchall()
    result = list(result)
    result = [list(i) for i in result]

    return result
