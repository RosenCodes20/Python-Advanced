from math import pi

r1, h1, r2, h2 = [int(el) for el in input().split(",")]

first_cylinder_volume_in_cm = (pi * r1 ** 2 * h1) / 1000
second_cylinder_volume_in_cm = (pi * r2 ** 2 * h2) / 1000

if first_cylinder_volume_in_cm == second_cylinder_volume_in_cm:
    print(f"{second_cylinder_volume_in_cm:.2f}")

elif first_cylinder_volume_in_cm > second_cylinder_volume_in_cm:
    print(f"{first_cylinder_volume_in_cm:.2f}")

elif first_cylinder_volume_in_cm < second_cylinder_volume_in_cm:
    print(f"{second_cylinder_volume_in_cm:.2f}")
