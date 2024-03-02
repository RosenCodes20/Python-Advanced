def even_odd_filter(**kwargs):
    if "even" in kwargs:
        kwargs["even"] = [int(nums) for nums in kwargs["even"] if int(nums) % 2 == 0]

    if "odd" in kwargs:
        kwargs["odd"] = [int(nums) for nums in kwargs["odd"] if int(nums) % 2 != 0]

    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
