# pcost.py
#
# Exercise 1.27
f = open('Data/portfolio.csv', 'rt')
headers = next(f)
total = 0
for line in f:
	row = line.split(',')
	numShares = int(row[1])
	priceOfShares = float(row[2])
	total += numShares * priceOfShares

print('Total ', total)
