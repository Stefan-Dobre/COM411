print("How many bars should be charged?")
bars_to_be_charged = int(input())
bars_charged = 0
print()
while bars_charged < bars_to_be_charged:
    bars_charged = bars_charged +1
    print(f"Charging: {'█' * bars_charged}")
print("Batery charging is complete")
