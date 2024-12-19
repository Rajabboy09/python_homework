
def invest(amount, rate, years):
    for i in range(1,years+1):
        amount = amount*(1+rate/100)
        print (f"year {i}: ${amount:.2f}")
    
amount = float(input("Amount = "))
rate = float(input("Percentage rate  = "))
years = int(input("Years = "))
invest(amount,rate,years)