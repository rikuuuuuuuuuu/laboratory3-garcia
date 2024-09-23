def checkout():
    prices = [float(input(f"Enter price of item: ₱")) for i in range(3)]

    total = sum(prices)
    discount = 0.1 * total if total > 100 else 0 
    final_total = total - discount
    points = final_total // 10 

    print (f"Total : ₱{final_total:.2f}, Loyalty Points: {int(points)}")

    while True:
        payment = float(input(f"Enter payment (min ₱{final_total:.2f}): ₱"))
        if payment >= final_total:
            print(f"Payment accepted! Change: ₱{payment - final_total:.2f}")
            break
        print("Not enough! Try again.")

checkout()