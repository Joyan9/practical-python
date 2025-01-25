# pcost.py
#
# Exercise 1.27
'''
The columns in portfolio.csv correspond to the 
stock name, number of shares, and purchase price of a single stock holding. 
Write a program called pcost.py that opens this file, reads all lines, 
and calculates how much it cost to purchase all of the shares in the portfolio.

Hint: to convert a string to an integer, use int(s). To convert a string to a floating point, 
use float(s).
'''
cost = 0
f = open('/workspaces/practical-python/Work/Data/portfolio.csv', 'rt')
'''
r: This stands for "read mode," meaning the file is opened for reading. The file must exist; otherwise, an error will occur.
t: This stands for "text mode," meaning the file is opened as a text file (as opposed to binary mode).
'''
headers = next(f).split(',')
for line in f:
    row = line.split(',')
    price = float(row[-1])
    shares = float(row[1])
    cost = cost + (shares*price)
print(cost)
f.close()


