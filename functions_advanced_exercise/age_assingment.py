def age_assignment(*args, **kwargs):
    result = []
    for name in args:
        for letter in kwargs:
            if name.startswith(letter):
                result.append(f"{name} is {kwargs[letter]} years old.")

    return "\n".join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))
