# Assignment: Books, Phase 1 
# Muyang Shi and Justin T. Washington
import csv, sys
from operator import itemgetter

filename = sys.argv[1]
action = sys.argv[2]
try:
	sortDirection = sys.argv[3]
except:
	pass

books = []
sortlist = []
reader = csv.reader(open(filename))
for row in reader:
	books.append(row)

#figure out how to negate cases
if action == "books":
	books.sort()
	for row in books:
		print(row[0])
elif action == "authors":
	for row in books:
		sortlist.append(row[2])
	print(sortlist)
	books.sort(key = itemgetter(2))
	