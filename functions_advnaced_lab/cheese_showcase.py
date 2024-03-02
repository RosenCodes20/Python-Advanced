def sorting_cheeses(**kwargs):
    result = ""
    sorted_result = sorted(
        kwargs.items(),
        key=lambda x: (-len(x[1]), x[0]),
    )

    for cheese, value in sorted_result:
        result += f"{cheese}\n"
        for values in sorted(value, key=lambda x: -x):
            result += f"{values}\n"
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
