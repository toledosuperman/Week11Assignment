employee_numbers=[1121,1122,1127,1132,1137,1138,1152,1157]
employee_name=["Jackie Grainger","Jignesh Thrakkar","Dion Green","Jacob Gerber","Sarah Sanderson","Brandon Heck","David Toma","Charles King"]
hourly_rate=[22.22,25.25,28.75,24.32,23.45,25.84,22.65,23.75]
company_raises=[]
max_value=0
total_hourly_rate=[]
underpaid_salaries=[]
for i in range(0,len(hourly_rate)):
    total_hourly_rate.append(hourly_rate[i]*1.3)
for i in range(0,len(total_hourly_rate)):
    if(total_hourly_rate[i]>max_value):
        max_value=total_hourly_rate[i] 
if(max_value>37.30):
    print("\n Error in data.\n")
for i in range(0,len(total_hourly_rate)):
    if(total_hourly_rate[i]>=28.15 and total_hourly_rate[i]<=28.15):
        underpaid_salaries.append(total_hourly_rate[i])
for i in range(0,len(hourly_rate)):
    if(hourly_rate[i]>22 and hourly_rate[i]<24):
        hourly_rate[i]+=((hourly_rate[i]/100)*5)
    elif(hourly_rate[i]>24 and hourly_rate[i]<26):
        hourly_rate[i]+=((hourly_rate[i]/100)*4)
    elif(hourly_rate[i]>26 and hourly_rate[i]<28):
        hourly_rate[i]+=((hourly_rate[i]/100)*3)
    else:
        hourly_rate[i]+=((hourly_rate[i]/100)*2)
company_raises.extend(hourly_rate)
for i in range(0,len(hourly_rate)):
    hourly_rate[i]= (hourly_rate[i]+((hourly_rate[i]/100)*5)) if (hourly_rate[i]>22 and hourly_rate[i]<24) else (hourly_rate[i]+((hourly_rate[i]/100)*4)) if (hourly_rate[i]>24 and hourly_rate[i]<26) else hourly_rate[i]+((hourly_rate[i]/100)*2)
print(employee_numbers)
print(employee_name)
print(hourly_rate)
