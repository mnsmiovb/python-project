electricityUsage=float(input('Write monthly electricity usage in kWh:'))
if electricityUsage>=0:
    if electricityUsage<=100:
        selectedRateUnder100=0.08
        print('Monthly electricity usage is',electricityUsage,', applied rate is',selectedRateUnder100,'.So total bill is',electricityUsage*selectedRateUnder100)
    elif electricityUsage<=300:
        selectedRateUnder300=0.12
        print('Monthly electricity usage is',electricityUsage,', applied rate is',selectedRateUnder300,'.So total bill is',electricityUsage*selectedRateUnder300)
    else:
        selectedRateAbove300=0.15
        print('Monthly electricity usage is',electricityUsage,', applied rate is',selectedRateAbove300,'.So total bill is',electricityUsage*selectedRateAbove300)
else:
    print('invalid')