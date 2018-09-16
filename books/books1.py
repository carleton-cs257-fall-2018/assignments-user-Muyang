# Assignment: Books, Phase 1 
# Muyang Shi and Justin T. Washington
import csv, sys
from operator import itemgetter

filename = sys.argv[1]
action = sys.argv[2]
#Sort Direction is optional, if the user does not specify, the program
#will sort in forward direction
try:
	sortDirection = sys.argv[3]
except:
	sortDirection = "forward"
	print("Sorted in forward alphabetical order")
	pass

books = []
sortlist = []
reader = csv.reader(open(filename))
for row in reader:
	books.append(row)

#figure out how to negate cases
if (sortDirection != "forward") and (sortDirection != "reverse"):
	print("Usage: Optional [sort-direction] can be either forward or backward.")
	print("		Please try again")
else:
	if action == "books":
		if sortDirection == "forward":
			books.sort()
		elif sortDirection == "reverse":
			books.sort(reverse = True)
		for row in books:
			print(row[0])
		#else:
		#	print("Usage: Optional [sort-direction] can be either forward or backward.")
		#	print("		Please try again")
	if action == "authors":
		for row in books:
			sortlist.append(row[2])
		if sortDirection == "forward":
			sortlist.sort(key = lambda x: x.split(" ")[-2])
		elif sortDirection == "reverse":
			sortlist.sort(key = lambda x: x.split(" ")[-2], reverse = True)
		for author in sortlist:
			print(''.join(names for names in author if names not in '()-1234567890'))

input("\nPress the enter key to exit.")
	