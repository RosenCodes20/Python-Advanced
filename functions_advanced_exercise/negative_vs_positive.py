def negative_positive(number):
    negative_sum = 0
    positive_sum = 0
    for num in number:
        if num > 0:
            positive_sum += num

        elif num < 0:
            negative_sum += num
    print(negative_sum)
    print(positive_sum)
    if abs(negative_sum) > positive_sum:
        print(f"The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


nums = [int(el) for el in input().split()]
negative_positive(nums)