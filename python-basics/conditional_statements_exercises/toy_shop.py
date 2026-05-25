price_of_the_excursion = float(input())
number_of_puzzles = int(input())
number_of_the_talking_dolls = int(input())
number_of_the_teddy_bears = int(input())
number_of_minions = int(input())
number_trucks = int(input())

price_of_puzzles = number_of_puzzles * 2.60
price_of_talking_dolls = number_of_the_talking_dolls * 3
price_of_teddy_bears = number_of_the_teddy_bears * 4.10
price_of_minions = number_of_minions * 8.20
price_of_trucks = number_trucks * 2

counter_of_ordered_toys = (
    number_of_puzzles + number_of_the_talking_dolls
    + number_of_the_teddy_bears + number_of_minions
    + number_trucks
)

total_price = (
    price_of_puzzles + price_of_talking_dolls
    + price_of_teddy_bears + price_of_minions
    + price_of_trucks
)

if counter_of_ordered_toys >= 50:
    total_price *= 0.75

rent = total_price * 0.10
total_price_with_rent = total_price - rent
remaining_money = abs(total_price_with_rent - price_of_the_excursion)

if total_price_with_rent >= price_of_the_excursion:
    print(f"Yes! {remaining_money:.2f} lv left.")
else:
    print(f"Not enough money! {remaining_money:.2f} lv needed.")
