
def amortization(principal, annual_rate, years, extra_payments):
    snapshot = int(input("Enter month to view a snapshot of interest payments and principal balance at that point in time \n"))
    
    monthly_rate = annual_rate / 12/ 100
    months = years * 12
    fixed_monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    monthly_payment = fixed_monthly_payment
    
    balance = principal
    month = 1
    interest_total = 0
    total_payments = 0
    
 
    while balance > 0 and month <= months:
        interest_payment = balance * monthly_rate
        principal_payment = monthly_payment - interest_payment
        extra_payment = extra_payments.get(month, 0) if extra_payments else 0
                       
        # For loop option if using a list or tuple for the extra payments. 
        
        # for x in extra_payment_month:
        #     if month == x:
        #         balance -= extra_payment
        #         total_payments += extra_payment
                # print("extra payment:", f"${extra_payment:,.0f}")
        
        month += 1 
        
        interest_total += interest_payment
        total_payments += (monthly_payment + extra_payment)
        
        if month == snapshot:
            print("Snapshot for month: ", snapshot)
            print("Total payments: ", f"${total_payments:,.2f}","\nInterest paid: ", f"${interest_total:,.2f}", "\nPrincipal remaining: ", f"${balance:,.2f}")
        
        if balance <= monthly_payment + extra_payment:
            principal_payment = balance
            monthly_payment = principal_payment + interest_payment
            balance = 0
        else: 
            balance -= (principal_payment + extra_payment)
    
        # print(f"{month}\t${monthly_payment:,.0f}\t\t${interest_payment:,.0f}\t\t${principal_payment:,.0f}\t\t${balance:,.0f}")

    repayment_time = month
    
    print("\nLife of Mortgage")
    print("Monthly payment: ", f"${fixed_monthly_payment:,.2f}")
    print("Total payments: ", f"${total_payments:,.2f}")
    print("Total interest paid: ", f"${interest_total:,.2f}")
    print("Time to pay off: ", repayment_time // 12, "years and", repayment_time % 12, "months" )

    
principal = 410000
annual_rate = 6.6
years = 30
extra_payments = {8:1000, 12:1000, 18:1000}

amortization(principal, annual_rate, years, extra_payments)


    


