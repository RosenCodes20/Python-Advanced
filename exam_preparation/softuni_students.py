def softuni_students(*args, **kwargs):
    users = {}
    invalid = set()
    for element in args:
        id, name = element
        if id not in users:
            users[id] = [name]
        else:
            users[id].append(name)

        if id not in kwargs.keys():
            invalid.add(name)
            users[id].remove(name)
    for course_id, course in sorted(users.items()):
        users[course_id] = course

    result = ""
    for course_id, student in users.items():
        course_name = kwargs.get(course_id, '')
        for students in student:
            result += f"*** A student with the username {students} has successfully finished the course {course_name}!\n"

    if invalid:
        result += f"!!! Invalid course students: {', '.join(invalid)}"

    return result


print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))

print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))


print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
