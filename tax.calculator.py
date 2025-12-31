filing_status = {
    0: "Single",
    1: "Married Filling Jointly or Qualified Widow(er)",
    2: "Married Filling Separately",
    3: "Head of Household"
}

while True:
    try:
        status = int(input("Specify your filing status (0 - 3): "))
        if 0 <= status <= 3:
            print(f"Your filing status is {filing_status[status]}")
            break
        else:
            print("Please enter a number between 0 and 3.")
    except ValueError:
        print("Invalid input. Enter a number.")

taxable_income = int(input("Enter your taxable income: $"))

tax_brackets = {
    0: [  # For Single
        (8350, .10),
        (33950, .15),
        (82250, .25),
        (171550, .28),
        (372950, .33),
        (float("inf"), .35)
    ],

    1: [  # For Married Filing Jointly or Qualifying Widow(er)
        (16700, .10),
        (67900, .15),
        (137050, .25),
        (208850, .28),
        (372950, .33),
        (float("inf"), .35)
    ],

    2: [  # For Married Filing Separately
        (8350, .10),
        (33950, .15),
        (68525, .25),
        (104425, .28),
        (186475, .33),
        (float("inf"), .35)
    ],

    3: [  # For Head of Household
        (11950, .10),
        (45500, .15),
        (117450, .25),
        (190200, .28),
        (372950, .33),
        (float("inf"), .35)
    ]

}


class Tax_payer:
    def __init__(self, status, income):
        self.status = status
        self.income = income

    def calculate_tax(self):
        brackets = tax_brackets[self.status]

        remaining_income = self.income
        total_tax = 0
        previous_limit = 0

        for upper_limit, rate in brackets:
            if remaining_income <= 0:
                break

            taxable_amount = min(
                upper_limit - previous_limit, remaining_income)
            total_tax += taxable_amount * rate

            remaining_income -= taxable_amount
            previous_limit = upper_limit
        return total_tax


taxpayer = Tax_payer(status, taxable_income)
tax = taxpayer.calculate_tax()
print(f"Total tax owed: ${tax:.2f}")            
