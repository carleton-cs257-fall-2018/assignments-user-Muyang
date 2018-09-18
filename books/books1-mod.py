# Assignment: Books, Phase 1 
# Muyang Shi and Justin T. Washington
import csv, sys
from operator import itemgetter

def booksHelper(filename, action, sortDirection):
	books = []
	sortlist = []
	reader = csv.reader(open(filename))
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
			print("Sorting in forward alphabetical order")
			books.sort()
		elif sortDirection == "reverse":
			print("Sorting in reverse alphabetical order")
			books.sort(reverse = True)
		for row in books:
			print(row[0])
	elif action == "authors":
		for row in books:
			sortlist.append(row[2])
		if sortDirection == "forward":
			sortlist.sort(key = lambda x: x.split(" ")[-2])
		elif sortDirection == "reverse":
			sortlist.sort(key = lambda x: x.split(" ")[-2], reverse = True)
		for author in sortlist:
			print(''.join(names for names in author if names not in '()-1234567890'))

	closing = input("\nPress the \"e\" to exit. ")
	if (closing != 'e'):
		retry = input("Would you like to try again? (y/n) ")
		if (retry.lower() == "y"):
			return(False)
	return(True)

def main():
	filename = sys.argv[1]
	action = sys.argv[2].lower()
	#Sort Direction is optional, if the user does not specify, the program
	#will sort in forward direction
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