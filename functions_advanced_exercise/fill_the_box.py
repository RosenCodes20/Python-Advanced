from collections import deque


def fill_the_box(h, l, w, *args):
    area_to_fill = h * l * w
    elements = deque(args)
    while elements[0] != "Finish":
        area_to_fill -= elements.popleft()

        if area_to_fill < 0:
            cubes_left = sum(c for c in elements if c != "Finish")
            return f"No more free space! You have {cubes_left + abs(area_to_fill)} more cubes."

    return f"There is free space in the box. You could put {area_to_fill} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))