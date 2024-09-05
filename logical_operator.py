high_income=True 
good_credit=True
if high_income and good_credit:
    print("Eligible for loan")
else:
    print("we are sorry, you are not eligible for loan")

high_income=False 
good_credit=False
if high_income or good_credit:
    print("Eligible for loan")
else:
    print("we are sorry, you are not eligible for loan")

    
has_good_credit = False
has_criminal_record = True
if has_criminal_record and not has_good_credit:
    print("You are eleigible for loan")
