courses = input().split(" -> ")

commands = input().split(":")

while commands[0] != "start academy":
    command = commands[0]

    if command == "Add":
        course = commands[1]

        if course not in courses:
            courses.append(course)

    elif command == "Insert":
        course = commands[1]
        index = int(commands[2])

        if course not in courses:
            courses.insert(index, course)

    elif command == "Remove":
        course = commands[1]
        if course in courses:
            courses.remove(course)

    elif command == "Swap":
        first_course = commands[1]
        second_course = commands[2]

        if first_course in courses and second_course in courses:
            first_course_index = courses.index(first_course)
            second_course_index = courses.index(second_course)
            courses.remove(first_course)
            courses.remove(second_course)
            courses.insert(first_course_index, second_course)
            courses.insert(second_course_index, first_course)

    commands = input().split(":")

num = 1

for course in courses:
    print(f"{num}.{course}")
    num += 1