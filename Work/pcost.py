# pcost.py
#
# Exercise 1.27
import csv
import sys
def portfolio_cost(filename):
    total = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:	
                numShares = int(row[1])
                priceOfShares = float(row[2])
                total += numShares * priceOfShares
            except ValueError:
                print("Invalid Literal", row)
    return total

## cost = portfolio_cost('Data/portfolio.csv')
if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)

print('Total cost: ', cost)