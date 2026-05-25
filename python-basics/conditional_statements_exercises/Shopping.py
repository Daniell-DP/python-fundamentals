budget = float(input())
counter_video_cards = int(input())
counter_processor = int(input())
counter_ram_memory = int(input())

price_for_video_cards = counter_video_cards * 250
price_for_processor = (price_for_video_cards * 0.35) * counter_processor
price_for_ram_memory = (price_for_video_cards * 0.10) * counter_ram_memory

all_prices = price_for_video_cards + price_for_processor + price_for_ram_memory

if counter_video_cards > counter_processor:
    all_prices *= 0.85

residual_budget = abs(all_prices - budget)
if all_prices <= budget:
    print(f"You have {residual_budget:.2f} leva left!")
else:
    print(f"Not enough money! You need {residual_budget:.2f} leva more!")
