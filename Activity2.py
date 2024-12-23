cost_price = float(input("Enter The Cost Price: "))

sell_price = float(input("Enter The Sell Price: "))

if sell_price > cost_price:
    profit = sell_price - cost_price
    print(f"{profit} Is The Profit Of {cost_price}")

elif sell_price < cost_price:
    loss = cost_price - sell_price
    print(f"{loss} is the loss of {cost_price}")

elif sell_price == cost_price:
    print("It Is Nor A Profit Or A Loss")