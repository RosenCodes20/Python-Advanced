def students_credits(*args):
    nums_dict = {}
    result = []
    sum_of_credits = 0
    for element in args:
        course, credit, max_points, diyan_points = element.split("-")
        credit, max_points, diyan_points = int(credit), int(max_points), int(diyan_points)
        percentage = (diyan_points / max_points) * 100
        course_credits = (percentage * credit) / 100
        if course not in nums_dict:
            nums_dict[course] = course_credits

    for courses, courses_credits in sorted(nums_dict.items(), key=lambda x: -x[1]):
        sum_of_credits += courses_credits
        result.append(f"{courses} - {courses_credits:.1f}")
    if sum_of_credits >= 240:
        return f"Diyan gets a diploma with {sum_of_credits:.1f} credits.\n" + "\n".join(result)
    else:
        return f"Diyan needs {240 - sum_of_credits:.1f} credits more for a diploma.\n" + "\n".join(result)


print(
        students_credits(
            "Computer Science-12-300-250",
            "Basic Algebra-15-400-200",
            "Algorithms-25-500-490"
        )
    )

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

