city = input()
sells = float(input())
percentage_of_sales = 0

if city == "Sofia":
    if 0 <= sells <= 500:
        percentage_of_sales = 0.05
    elif 500 <= sells <= 1000:
        percentage_of_sales = 0.07
    elif 1000 <= sells <= 10000:
        percentage_of_sales = 0.08
    elif sells > 10000:
        percentage_of_sales = 0.12
    else:
        total = "error"
if city == "Varna":
    if 0 <= sells <= 500:
        percentage_of_sales = 0.045
    elif 500 <= sells <= 1000:
        percentage_of_sales = 0.075
    elif 1000 <= sells <= 10000:
        percentage_of_sales = 0.10
    elif sells > 10000:
        percentage_of_sales = 0.13
    else:
        total = "error"
if city == "Plovdiv":
    if 0 <= sells <= 500:
        percentage_of_sales = 0.055
    elif 500 <= sells <= 1000:
        percentage_of_sales = 0.08
    elif 1000 <= sells <= 10000:
        percentage_of_sales = 0.12
    elif sells > 10000:
        percentage_of_sales = 0.145
    else:
        total = "error"

if percentage_of_sales <= 0:
    print("error")
else:
    total = sells * percentage_of_sales
    print(f"{total:.2f}")