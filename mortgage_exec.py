from mortgage_comparison import *

mortgage1 = Mortgage(176500, 3.125, 20, {12: 1000, 24:1000})
mortgage2 = Mortgage(450000, 6.0, 30, {12: 1000, 24:1000})

mortgages = [mortgage1, mortgage2]

print("Mortgage 1")
mortgage1.summary()
print("*******")

print("Mortgage 2")
mortgage2.summary()
print("*******")

def amort_prompt(): 
    amort_entry = input(f"Would you like to print the amortization scheudle for? y for yes, n for no\t").lower()
    if amort_entry == "y":
        mortgage1.amortization_output()
        # for instance in mortgages:
        #     instance.amortization_output()
    elif amort_entry == "n":
        print("Ok, summary is sufficient")
    else:
        print("Invalid entry. Please enter y or n")
        return amort_prompt()

amort_prompt()

print("**********")
# Comparisons

print("Comparison between mortgage 1 and mortgage 2")
monthly_payment_dif = mortgage1.monthly_payment - mortgage2.monthly_payment
print(f"Monthly payments for mortgage 1 are ${abs(monthly_payment_dif):,.0f} {"more" if monthly_payment_dif > 0 else "less"} than mortgage 2")
repayment_dif = mortgage1.month# - mortgage2.month
print(f"Repayment time for mortagage 1 is {abs(repayment_dif)} {"more" if repayment_dif > 0 else "less"} months than mortgage 2")
total_dif = mortgage1.total_payments - mortgage2.total_payments
print(f"Total payments for mortagage 1 are ${abs(total_dif):,.0f} {"more" if total_dif > 0 else "less"} than mortgage 2")
interest_dif = mortgage1.get_total_interest() - mortgage2.get_total_interest()
print(f"Total interest for mortagage 1 is ${abs(interest_dif):,.0f} {"more" if interest_dif > 0 else "less"}  than mortgage 2")
