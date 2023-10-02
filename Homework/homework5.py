var1 = int(input("Input the number of minutes:"))

minutes_in_day = 1440
minutes_in_year = 525600
# Calculate number of years
number_of_years = var1//minutes_in_year
# Calculate number of minutes left
var1 %= minutes_in_year
# Calculate number of minutes
number_of_days = var1//minutes_in_day

print(var1,"minutes is approximately",number_of_years,
      "years and",number_of_days,"days")














