budget_of_film = float(input())
counter_of_extras = int(input())
price_for_dress_per_extras = float(input())

decor = budget_of_film * 0.10

price_for_dress = price_for_dress_per_extras * counter_of_extras
if counter_of_extras > 150:
    price_for_dress *= 0.90

necessary_resources = decor + price_for_dress
money = abs(budget_of_film - necessary_resources)

if necessary_resources <= budget_of_film:
    print(f"Action!")
    print(f"Wingard starts filming with {money:.2f} leva left.")
else:
    print(f"Not enough money!")
    print(f"Wingard needs {money:.2f} leva more.")


