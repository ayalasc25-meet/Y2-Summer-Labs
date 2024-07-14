import random
even=0
temperature=[]
gooddays=[]
aboveaverage=[]
days=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
n=1
for i in range(7):
	temperature.append(random.randint(26,40))
for i in range(7):
    if temperature[i] % 2 == 0:
        even += 1
        gooddays.append(days[i])
highesttemp=max(temperature)
lowesttemp=min(temperature)
lowesttempday=days[temperature.index(lowesttemp)]
highesttempday=days[temperature.index(highesttemp)]
averagetemp=sum(temperature)/7
for i in range(7):
	if temperature[i]>averagetemp:
		aboveaverage.append(days[i])
print(temperature)
print("The days with even temperatures are:", gooddays) 
print("The day with the highest temperature is",highesttempday)
print("The day with the lowest temperature is",lowesttempday)
print("The average temperature for this week is",averagetemp)
print("The days with above average temperature are",aboveaverage)

