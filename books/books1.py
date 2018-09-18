# Assignment: Books, Phase 1 

# Muyang Shi, Justin T. Washington, Chae Kim

import csv, sys

def main():
	try:
		filename = sys.argv[1]
		action = sys.argv[2].lower()
		#Sort Direction is optional, if the user does not specify, the program
		#will sort in forward direction
	except:
		throw_error()
	try:
		sortDirection = sys.argv[3].lower()
	except:
		sortDirection = "forward"
	booksHelper(filename, action, sortDirection)

def booksHelper(filename, action, sortDirection):
	#list for all CSV rows, unsorted
	books = []
	#list to place sorted books[] into (only for authors action)
	sortlist = []

	reader = csv.reader(open(filename))
		#Get all CSVs into book[]
	for row in reader:
		books.append(row)
	#Check for proper input
	if (sortDirection != "forward") and (sortDirection != "reverse"):
		print("Usage: Optional [sort-direction] can be either forward or backward.")
		throw_error()
	elif (action != "books") and (action != "authors"):
		print("Usage: action can be either books or authors")
		throw_error()
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
				#if row[2], the authors, contains " and " 
				#then add the split of that to sortlist
				if " and " in row[2]:
					sortlist = sortlist + row[2].split(" and ")
				else:
					sortlist.append(row[2])
			if sortDirection == "forward": #This needs to speicify forward or nothing
				#split authors line by space and 
				#sort by the second to last item (last name), 
				#the [-2] gives the second to last in a row, which is lastname
				sortlist.sort(key = lambda x: x.split(" ")[-2])
			elif sortDirection == "reverse":
				#we might be able to consolidate this line with the other
				sortlist.sort(key = lambda x: x.split(" ")[-2], reverse = True)
			for author in sortlist:
				#handle rejoining of names and exlude all non-name parts
				print(''.join(names for names in author if names not in '()-1234567890'))
def throw_error():
	print("Usage: python3 books1.py input-file action [sort-direction]", file = sys.stderr)
	quit()

if __name__ == "__main__":
	main()