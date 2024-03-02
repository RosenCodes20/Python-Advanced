from collections import deque

food_portions = deque([int(el) for el in input().split(", ")])
stamina = deque([int(el) for el in input().split(", ")])
peaks = {"Vihren": 0, "Kutelo": 0, "Banski Suhodol": 0, "Polezhan": 0, "Kamenitza": 0}
peaks_sum = 0
climbed_peaks = []
day = 1
while food_portions and stamina:

    current_portion = food_portions.pop()
    current_stamina = stamina.popleft()

    current_sum = current_portion + current_stamina

    if current_sum == 80:
        peaks["Vihren"] += 1

    elif current_sum == 90:
        peaks["Kutelo"] += 1
    elif current_sum >= 100:
        peaks["Banski Suhodol"] = 1

    elif current_sum == 60:
        peaks["Polezhan"] += 1

    elif current_sum == 70:
        peaks["Kamenitza"] += 1

    day += 1


for peak, peak_concurred in peaks.items():
    peaks_sum += peak_concurred
    if peak_concurred > 0:
        climbed_peaks.append(peak)
if peaks_sum >= 5 and day > 7:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")

else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if climbed_peaks:
    print(f"Conquered peaks:")
    print("\n".join(climbed_peaks))