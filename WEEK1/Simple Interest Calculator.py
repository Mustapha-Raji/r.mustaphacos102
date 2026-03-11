principal = int(input("P($): "))
rate = int(input("R(%): "))/100
time = int(input("T: "))

calc1 = 1 + (rate * time)
calc2= principal * calc1
print(f"Amount: {calc2}")
