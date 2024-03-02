def gather_credits(credit, *args):
    course_dict = {}
    result = ""
    max_sum = 0
    courses = []
    needed_credits = 0
    for element in args:
        course_name, course_credits = element
        course_credits = int(course_credits)
        needed_credits = credit - course_credits
        if course_name not in course_dict:
            course_dict[course_name] = course_credits

    for course, course_credit in course_dict.items():
        max_sum += course_credit
        courses.append(course)

        if max_sum >= credit:
            break

    if max_sum >= credit:
        return f"""Enrollment finished! Maximum credits: {max_sum}.Courses: {', '.join(sorted(courses))}"""

    else:
        return f"""You need to enroll in more courses! You have to gather {needed_credits} credits more."""




print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 50)
))


print(gather_credits(
    80,
    ("Basics", 27),
))


print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
