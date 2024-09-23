def loan_eligibility():
    # Input: Monthly salary
    monthly_salary = float(input("Enter your monthly salary: "))
    
    # Input: Requested loan amount
    requested_loan_amount = float(input("Enter the requested loan amount: "))
    
    # Eligibility check
    if monthly_salary < 30000:
        print("Loan not approved: Salary is too low.")
    elif requested_loan_amount > (10 * monthly_salary):
        print("Loan not approved: Requested amount exceeds limit.")
    else:
        print("You are eligible for the loan.")
        
        # Input: Number of months to pay
        months_to_pay = int(input("Enter the number of months to pay: "))
        
        # Calculate total loan amount with interest
        interest = 0.10
        total_loan_amount = requested_loan_amount * (1 + interest)
        
        # Output the results
        print(f"Total loan amount with interest: {total_loan_amount:.2f}")
        monthly_payment = total_loan_amount / months_to_pay
        print(f"Monthly payment: {monthly_payment:.2f}")

# Call the function to execute the program
loan_eligibility()
