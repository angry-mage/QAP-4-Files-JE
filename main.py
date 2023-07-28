# Program for One Stop Insurance Company to process and store new insurance policy information for it's cusotmers

# Written by : Jay Eagles

# Written on : 07/22/2023 - 07/28/2023

# Import libraries

import datetime as datetime
import FormatValues as FV

CurrDate = datetime.datetime.now()  # Defining the current date for later use

# Define constants by reading from the OSIC defaults file

f = open('OSICDef.dat', 'r')
NEXT_POL_NUM = int(f.readline())
BASE_PREMIUM = float(f.readline())
ADD_CAR_DISCOUNT = float(f.readline())
COST_EXTRA_LIABILITY = float(f.readline())
COST_GLASS = float(f.readline())
COST_LOAN_CAR = float(f.readline())
HST_RATE = float(f.readline())
MONTH_PROC_FEE = float(f.readline())
f.close()

# Define required functions

# Main Program

allowed_letters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
allowed_numbers = set("0123456789")

PolNumCtr = 0

while True:
    while True:
        CustFirst = input("Enter the customer's first name: ").title()
        if CustFirst == "":
            print("Error - Customer's first name cannot be blank.")
        else:
            break

    while True:
        CustLast = input("Enter the customer's last name: ").title()
        if CustLast == "":
            print("Error - Customer's last name cannot be blank.")
        else:
            break

    while True:
        StAdd = input("Enter the customer's street address: ")
        if StAdd == "":
            print("Error - Customer's street address cannot be blank.")
        else:
            break

    while True:
        City = input("Enter the customer's city: ").title()
        if City == "":
            print("Error - Customer's city cannot be blank.")
        else:
            break

    while True:
        ProvList = ["QC", "MB", "NS", "NL", "ON", "SK", "AB", "PE", "NB", "BC", "YK", "NW", "NV"]
        Prov = input("Enter the customer's province: ").upper()
        if Prov == "":
            print("Error - Province cannot be blank.")
        elif len(Prov) != 2:
            print("Error - Province must be 2 characters long.")
        elif Prov not in ProvList:
            print("Error - Province must be a valid input.")
        else:
            break

    while True:
        PostCode = input("Enter the customer's postal code (L9L9L9): ").upper()
        if PostCode == "":
            print("Error - Postal code cannot be blank.")
        elif len(PostCode) != 6:
            print("Error - Postal code must be 6 characters.")
        elif not set(PostCode[0]).issubset(allowed_letters):
            print("Error - First character in the postal code must be a letter.")
        elif not set(PostCode[2]).issubset(allowed_letters):
            print("Error - Third character in the postal code must be a letter.")
        elif not set(PostCode[4]).issubset(allowed_letters):
            print("Error - Fifth character in the postal code must be a letter.")
        elif not set(PostCode[1]).issubset(allowed_numbers):
            print("Error - Second character in the postal code must be a number.")
        elif not set(PostCode[3]).issubset(allowed_numbers):
            print("Error - Forth character in the postal code must be a number.")
        elif not set(PostCode[5]).issubset(allowed_numbers):
            print("Error - Sixth character in the postal code must be a number.")
        else:
            break

    while True:
        PhoneNum = input("Enter the customer's phone number (9999999999): ")
        if PhoneNum == "":
            print("Error - Phone number cannot be blank.")
        elif len(PhoneNum) != 10:
            print("Error - Phone number must be 10 digits.")
        elif not PhoneNum.isdigit():
            print("Error - Phone number must be a valid input.")
        else:
            break

    while True:
        try:
            NumCar = int(input("Enter the number of cars being insured: "))
        except:
            print("Error - Number of cars must be a valid input.")
        else:
            break

    while True:
        OptLiable = input("Enter if the customer wants extra liability (Up to $1,000,000.00 - (Y / N): ").upper()
        if OptLiable == "":
            print("Error - Extra liability cannot be blank.")
        elif OptLiable != "Y" and OptLiable != "N":
            print("Error - Extra liability must be a valid input.")
        else:
            break

    while True:
        OptGlass = input("Enter if the customer opted for glass coverage (Y / N): ").upper()
        if OptGlass == "":
            print("Error - Glass coverage option cannot be blank.")
        elif OptGlass != "Y" and OptGlass != "N":
            print("Error - Glass coverage option must be a valid input.")
        else:
            break

    while True:
        OptLoanCar = input("Enter if the customer opted for a loaner car (Y / N): ").upper()
        if OptLoanCar == "":
            print("Error - Loaner car option cannot be blank.")
        elif OptLoanCar != "Y" and OptLoanCar != "N":
            print("Error - Loaner car option must be a valid input.")
        else:
            break

    while True:
        PayMethodList = ["Full", "Monthly"]
        PayMethod = input("Enter if the customer wants to pay in full or monthly: ").title()
        if PayMethod == "":
            print("Error - Payment method cannot be blank.")
        elif PayMethod not in PayMethodList:
            print("Error - Payment method must be 'Full' or 'Monthly'.")
        else:
            break

    # Perfrom calculations

    if NumCar > 1:
        InsurePrem = BASE_PREMIUM + ((BASE_PREMIUM * ADD_CAR_DISCOUNT) * (NumCar - 1))
    else:
        InsurePrem = BASE_PREMIUM

    if OptLiable == "Y":
        LiableCost = COST_EXTRA_LIABILITY
    else:
        LiableCost = 0

    if OptGlass == "Y":
        GlassCost = COST_GLASS
    else:
        GlassCost = 0

    if OptLoanCar == "Y":
        LoanCarCost = COST_LOAN_CAR
    else:
        LoanCarCost = 0

    TotExtraCost = LiableCost + GlassCost + LoanCarCost

    TotInsurePrem = TotExtraCost + InsurePrem

    HST = TotInsurePrem * HST_RATE

    TotCost = TotInsurePrem + HST

    if PayMethod == "Monthly":
        MonthPay = (TotCost + MONTH_PROC_FEE / 8)
    else:
        MonthPay = 0

    InvDate = CurrDate
    NextPayDate = InvDate.replace(day=1) + datetime.timedelta(days=30)

    # Format values for display

    InvDateDsp = FV.FDateS(InvDate)
    CustNameDsp = CustFirst + " " + CustLast
    PostCodeDsp = PostCode[0:3] + " " + PostCode[3:6]
    PhoneNumDsp = "(" + PhoneNum[0:3] + ") " + PhoneNum[3:6] + "-" + PhoneNum[6:10]
    AddressDsp = StAdd + ", " + City + " " + Prov

    # Display input and calculated values in a well-designed receipt

    print()
    print("              ONE STOP INSURANCE COMPANY")
    print(" ", "-"*50)
    print(f"  Policy #: {NEXT_POL_NUM}            Invoice Date: {InvDateDsp}")
    print()
    print("  Customer Information")
    print("  --------------------------------------------------")
    print(f"  Name:              {CustNameDsp:>31}")
    print(f"  Address:           {AddressDsp:>31}")
    print(f"  Postal Code:       {PostCodeDsp:>31}")
    print(f"  Phone Number:      {PhoneNumDsp:>31}")
    print()
    print("  Policy Information")
    print("  --------------------------------------------------")
    print(f"  Number of Cars:    {NumCar:>31}")
    print(f"  Payment Method:    {PayMethod:>31}")
    print(f"  Extra Liability:   {OptLiable:>31}")
    print(f"  Glass Coverage:    {OptGlass:>31}")
    print(f"  Loaner Car:        {OptLoanCar:>31}")
    print()
    print("  Payment Details")
    print("  --------------------------------------------------")
    print(f"  Insurance Premium: {FV.FDollar2(InsurePrem):>31}")
    print(f"  Extra Coverages:   {FV.FDollar2(TotExtraCost):>31}")
    print(f"  Policy Subtotal:   {FV.FDollar2(TotInsurePrem):>31}")
    print(f"  HST:               {FV.FDollar2(HST):>31}")
    print()
    print(f"  Total Cost:        {FV.FDollar2(TotCost):>31}")
    print("  --------------------------------------------------")
    if PayMethod == "Monthly":
        print(f"  Next Payment Date: {FV.FDateS(NextPayDate):>31}")
        print(f"  Monthly Payment:   {FV.FDollar2(MonthPay):>31}")

    f = open('Policies.dat', 'a')

    f.write("{}, ".format(str(NEXT_POL_NUM)))
    f.write("{}, ".format(str(InvDateDsp)))
    f.write("{}, ".format(CustFirst))
    f.write("{}, ".format(CustLast))
    f.write("{}, ".format(StAdd))
    f.write("{}, ".format(City))
    f.write("{}, ".format(Prov))
    f.write("{}, ".format(PostCode))
    f.write("{}, ".format(PhoneNum))
    f.write("{}, ".format(str(NumCar)))
    f.write("{}, ".format(OptLiable))
    f.write("{}, ".format(OptGlass))
    f.write("{}, ".format(OptLoanCar))
    f.write("{}, ".format(PayMethod))
    f.write("{}\n".format(str(TotInsurePrem)))

    f.close()

    print()
    print("Policy information successfully saved ...")
    NEXT_POL_NUM += 1

    print()
    Continue = input("Would you like to process another insurance policy? (Y / N): ").upper()
    if Continue == "N":
        break

f = open('OSICDef.dat', 'w')
f.write("{}\n".format(NEXT_POL_NUM))
f.write("{}\n".format(BASE_PREMIUM))
f.write("{}\n".format(ADD_CAR_DISCOUNT))
f.write("{}\n".format(COST_EXTRA_LIABILITY))
f.write("{}\n".format(COST_GLASS))
f.write("{}\n".format(COST_LOAN_CAR))
f.write("{}\n".format(HST_RATE))
f.write("{}\n".format(MONTH_PROC_FEE))
f.close()
