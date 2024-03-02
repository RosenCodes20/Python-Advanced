from collections import deque

colors_to_make = deque(input().split())

colors = {"red", "yellow", "purple", "green", "blue", "orange"}

how_colors_are_made = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"blue", "yellow"},
}
found_colors = []
a = 5

while colors_to_make:
    first_word = colors_to_make.popleft()
    second_word = colors_to_make.pop() if colors_to_make else ""

    for color in (first_word + second_word, second_word + first_word):
        if color in colors:
            found_colors.append(color)
            break

    else:
        for element in (first_word[:-1], second_word[:-1]):
            if element:
                colors_to_make.insert(len(colors_to_make) // 2, element)

for colores in set(how_colors_are_made.keys()).intersection(found_colors):
    if not how_colors_are_made[colores].issubset(found_colors):
        found_colors.remove(colores)

print(found_colors)