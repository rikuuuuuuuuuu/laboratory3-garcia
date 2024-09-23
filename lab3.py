def check_loan_eligibility():
    salary = float(input("Enter your monthly salary: "))
    loan_amount = float(input("Enter the loan amount you want to request: "))

    if salary >= 30000.00:
        max_loan_amount = salary * 10
        if loan_amount <= max_loan_amount:
            print("You are eligible for the loan.")
            months_to_pay = int(input("How many months do you want to pay the loan? "))
            interest = loan_amount * 0.10
            total_amount = loan_amount + interest
            print(f"Total amount to be paid: {total_amount:.2f}")
            print(f"Monthly payment over {months_to_pay} months: {total_amount / months_to_pay:.2f}")
        else:
            print("Loan request is too high. You can request up to:", max_loan_amount)
    else:
        print("Salary is too low. You need a monthly salary of at least 30,000.00.")

check_loan_eligibility()