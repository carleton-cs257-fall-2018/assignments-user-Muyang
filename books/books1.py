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

#list for all CSVs, unsorted
books = []
#list to place sorted books[] into (only for authors action)
sortlist = []

reader = csv.reader(open(filename))

#Get all CSVs into book[]
for row in reader:
	books.append(row)

#Check for proper input
#@Muyang I Think if we can check for this before appending all CSVs that'd be good
#we also need this to ask repeatedly and change sys.argv[2], rather than just asking
#once or jumping down to the end line after this if statement.
if (sortDirection != "forward") and (sortDirection != "reverse"):
	print("Usage: Optional [sort-direction] can be either forward or backward.")
	print("		Please try again")
else:
	#handle sorting by books
	if action == "books":
		if sortDirection == "forward":
			#this will sort by the first item, which is the title of the books
			books.sort()
		elif sortDirection == "reverse":
			#reverse if sortdirection specifies reverse
			books.sort(reverse = True)
		for row in books:
			#out of the list of lists, books[], print the first item (the titles)
			print(row[0])
	#handle sorting by authors
	if action == "authors":
		for row in books:
			#append all authors names/years to sortlist
			sortlist.append(row[2])
		if sortDirection == "forward": #This needs to speicify forward or nothing
			#split authors line by space and 
			#sort by the second to last item (last name)
			sortlist.sort(key = lambda x: x.split(" ")[-2])
		elif sortDirection == "reverse":
			#we might be able to consolidate this line with the other
			sortlist.sort(key = lambda x: x.split(" ")[-2], reverse = True)
		for author in sortlist:
			#handle rejoining of names and exlude all non-name parts
			print(''.join(names for names in author if names not in '()-1234567890'))

input("\nPress the enter key to exit.")
	