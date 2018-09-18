# Assignment: Books, Phase 1 
# Muyang Shi and Justin T. Washington
import csv, sys
from operator import itemgetter

def booksHelper(filename, action, sortDirection):
	books = []
	sortlist = []

	try:
		reader = csv.reader(open(filename))
	except:
		print("File does not exist")
		exit()

	for row in reader:
		books.append(row)
	
	#figure out how to negate cases
	while (sortDirection != "forward") and (sortDirection != "reverse"):
		print("Usage: Optional [sort-direction] can be either forward or reverse.")
		sortDirection = input("		Please try again ")
	while (action != "books") and (action != "authors"):
		print("Please choose an action - \"authors\" or \"books\"")
		action = input("	Please try again ")
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
			#if row[2] contains " and " then add the split of that to sortlist
			if " and " in row[2]:
				sortlist = sortlist + row[2].split(" and ")
			else:
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

	closing = input("\nPress the \"e\" to exit. ")
	if (closing != 'e'):
		retry = input("Would you like to try again? (y/n) ")
		if (retry.lower() == "y"):
			return(False)
	return(True)

def main():
	#Sort Direction is optional, if the user does not specify, the program
	#will sort in forward direction
	filename = "empty"
	action = "empty"

	try:
		filename = sys.argv[1]
		action = sys.argv[2]
	except:
		pass
	
	while filename == "empty":
		filename = input("Please input filename: ")
	while action == "empty":
		action = input("Please input action: ")

	try:
		sortDirection = sys.argv[3].lower()
	except:
		sortDirection = "forward"
	end = booksHelper(filename, action, sortDirection)
	while (not end):
		newCommands = input("Type in filename action sortDirection (ex. books.csv authors reverse) ").split(" ")
		filename = newCommands[0]
		action = newCommands[1]
		try:
			sortDirection = newCommands[2]
		except:
			sortDirection = "forward"
		end = booksHelper(filename, action, sortDirection)
	exit()


if __name__ == "__main__":
    main()