# CodeAlpha Task 2 - Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 200,
    "MSFT": 300
}

total = 0

print("📈 Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stocks.keys()))

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stocks:
        quantity = int(input("Enter quantity: "))
        value = stocks[stock] * quantity
        total += value
        print(f"{stock}: ₹{value}")
    else:
        print("Stock not found!")

print("\nTotal Investment Value: ₹", total)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: ₹{total}")

print("Portfolio saved successfully in portfolio.txt")