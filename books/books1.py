# Assignment: Books, Phase 1 
# Muyang Shi, Justin T. Washington, Chae Kim
import csv, sys

#list for all CSV rows, unsorted
books = []
#list to place sorted books[] into (only for authors action)
sortlist = []

try:
	filename = sys.argv[1]
	try:
		reader = csv.reader(open(filename))
		#Get all CSVs into book[]
		for row in reader:
			books.append(row)
	except:
		print('File not found')
	action = sys.argv[2]
except:
	action = 'empty'
	print("Usage: python3 books1.py input-file action [sort-direction]", file = sys.stderr)


#Sort Direction is optional, if the user does not specify, the program
#will sort in forward direction
try:
	sortDirection = sys.argv[3]
except:
	sortDirection = "forward"



#Check for proper input
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
	elif action == "authors":
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
			#if author.contain('and'):
			#	print(''.join(names for names in author))
			print(''.join(names for names in author if names not in '()-1234567890'))
	else:
		#action is not accepted
		print('action can be either books or authors \nPlease try again')