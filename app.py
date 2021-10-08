import my_functions
import os

#functions in app
show_options = my_functions.print_options
create_book = my_functions.create_book
save_books = my_functions.save_books
load_books = my_functions.load_books
issue_book = my_functions.issue_book
return_book = my_functions.return_book
update_book = my_functions.update_book
show_all_books = my_functions.show_all_books
show_book = my_functions.show_book

show_options()

option = input()

books =[]

while option !='x' and option != 'X':
	#do stuff here
	if option == "1":
		books.append(create_book())
	elif option == '2':
		save_books(books)
	elif option == '3':
		books = load_books()
	elif option == '4':
		print(issue_book(books))
	elif option == '5':
		return_book(books)
	elif option == '6':
		update_book(books)
	elif option == '7':
		show_all_books(books)
	elif option == '8':
		show_book(books)
	else:
		print("The given command doesn't exist..")
	
	input("press enter to continue")
	
	#asking for input
	os.system("clear")
	show_options()
	option=input()
