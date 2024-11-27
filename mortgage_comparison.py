class Mortgage:
    def __init__(self, principal, annual_rate, years, extra_payments):
        self.principal = principal
        self.annual_rate = annual_rate
        self.years = years
        self.extra_payments = extra_payments if extra_payments else {}
        self.monthly_payment = self.calculate_monthly_payment()
        self.constant_monthly_payment = self.calculate_monthly_payment()
        self.total_payments = 0
        self.interest_total = 0
        self.repayment_time = 0
        
    def calculate_monthly_payment(self):
        monthly_rate = self.annual_rate / 12 / 100
        self.months = self.years * 12
        return self.principal * (monthly_rate * (1 + monthly_rate) ** self.months) / ((1 + monthly_rate) ** self.months - 1)
        
    def amortization_schedule(self):
        self.balance = self.principal
        self.month = 0
        self.schedule = []
                
        while self.balance > 0 and self.month <= self.months:
            monthly_rate = self.annual_rate / 12 / 100
            self.interest_payment = self.balance * monthly_rate
            self.principal_payment = self.monthly_payment - self.interest_payment
            self.extra_payment = self.extra_payments.get(self.month, 0)
            
            self.interest_total += self.interest_payment
            self.total_payments += (self.monthly_payment + self.extra_payment)  
                    
            if self.balance <= self.monthly_payment + self.extra_payment:
                self.principal_payment = self.balance
                self.monthly_payment = self.principal_payment + self.interest_payment
                self.balance = 0
            else: 
                self.balance -= (self.principal_payment + self.extra_payment)

            self.month += 1
            
            self.repayment_time = self.month
            
            self.schedule.append({
                "Month": self.month,
                "Monthly payment": self.monthly_payment,
                "Interest payment": self.interest_payment,
                "Principal payment": self.principal_payment,
                "Extra payment": self.extra_payment,
                "Balance": self.balance,
            })
                 
        
    def get_total_payments(self):
        if self.total_payments == 0:
            self.amortization_schedule()
        return self.total_payments
    
    def get_total_interest(self):
        if self.interest_total == 0:
             self.amortization_schedule()
        return self.interest_total
    
    def summary(self):
        print(f"Monthly payment: ${self.constant_monthly_payment:,.2f}")
        print(f"Total Paid: ${self.get_total_payments():,.2f}")
        print(f"Total Interest: ${self.get_total_interest():,.2f}")
        print(f"Time to pay off: {self.repayment_time // 12} years and {self.repayment_time % 12} months")
        print(f"Extra payment savings: ${abs(self.get_total_payments() - (self.constant_monthly_payment * self.months)):,.0f}")
    
    def amortization_output(self):
        print(f"Month\tmonthly payment\tinterest\tprincipal\tbalance")
        for entry in self.schedule:
            print(f"{entry['Month']}\t${entry['Monthly payment']:,.0f}\t${entry['Interest payment']:,.0f}\t${entry['Principal payment']:,.0f}\t${entry['Extra payment']:,.0f}\t${entry['Balance']:,.0f}")
        
        # if self.extra_payment:
        #     print("extra payment:", f"${self.extra_payment:,.0f}")
       # print(f"{self.month}\t${self.monthly_payment:,.0f}\t\t${self.interest_payment:,.0f}\t\t${self.principal_payment:,.0f}\t\t${self.balance:,.0f}")
            