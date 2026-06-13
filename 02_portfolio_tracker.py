# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420
}

total_investment = 0

# Number of different stocks
n = int(input("Enter the number of stocks: ")) # taking input from the user

portfolio_data = []

for i in range(n):
    stock = input("Enter stock symbol (AAPL, TSLA, GOOGL, MSFT): ").upper()
    quantity = int(input("Enter quantity: ")) 

    if stock in stock_prices:
        value = stock_prices[stock] * quantity
        total_investment += value

        portfolio_data.append(
            f"{stock} - Quantity: {quantity}, Value: ${value}"
        )
    else:
        print("Stock not found!")

print("\n----- Portfolio Summary -----")
for item in portfolio_data:
    print(item)

print(f"\nTotal Investment Value: ${total_investment}")

# Save to text file
with open("portfolio.txt", "w") as file:
    file.write("Portfolio Summary\n")
    file.write("-----------------\n")

    for item in portfolio_data:
        file.write(item + "\n")

    file.write(f"\nTotal Investment Value: ${total_investment}")

print("\nPortfolio saved to 'portfolio.txt'")
