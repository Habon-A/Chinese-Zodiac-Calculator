#Zodiac Calculator

from zodiac_class_and_functions import * 

print('Chinese Zodiac Calculator')
print()

people_list =[] # List of the people who have used the zodiac calculator

name = input("Enter a Name:\n")

birthday = input("\nEnter a Birthday in MM/DD/YYYY Format: \n")  

birthday = birthday.split('/') #makes list to seperate month, date, and year

month = int(birthday[0]) #turns the dates into integers 
date = int(birthday[1])
year = int(birthday[2])

person_values = [] #for writing values 
person_values_list = []

# Not taking any birthdays that are earlier or later than the dates in the year_converter function
if year < 1924:
	print("Sorry, we aren't able to calculate your zodiac because you are too old for the calculator.")

elif year == 1924 and month == 1:
	print("Sorry, we aren't able to calculate your zodiac because you are too old for the calculator.")

elif year == 1924 and month == 2 and date < 5:
	print("Sorry, we aren't able to calculate your zodiac because you are too old for the calculator.")

elif year == 2023 and month == 1 and date > 21:
	print("Sorry, we aren't able to calculate your zodiac because you are too young for the calculator.")

elif year == 2023 and month > 1:
	print("Sorry, we aren't able to calculate your zodiac because you are too young for the calculator.")
	
elif year > 2023:
	print("Sorry, we aren't able to calculate your zodiac because you are too young for the calculator.")

else:

	year = year_converter(month,date,year)
	
	zodiac = find_zodiac(year)
	
	person = Person(name, zodiac) # uses __init__ method
	person.find_element()		  # uses find_element method
	people_list.append(person)
	print()
	print(person) #uses __str__ method
	
	person_values = [person.name, person.zodiac, person.element]  #seperate values for writing to file
	person_values_list.append(person_values)
	calculate_again = input("\nWould you like to calculate another person's zodiac? Type 'y' for yes or any other key for no.\n")
	
	while calculate_again == 'y':
		
		name = input("Enter a Name:\n")

		birthday = input("\nEnter a Birthday in MM/DD/YYYY Format: \n")  

		birthday = birthday.split('/') 

		month = int(birthday[0]) 
		date = int(birthday[1])
		year = int(birthday[2])



		if year < 1924:
			print("Sorry, we aren't able to calculate your zodiac because you are too old for the calculator.")

		elif year == 1924 and month == 1:
			print("Sorry, we aren't able to calculate your zodiac because you are too old for the calculator.")

		elif year == 1924 and month == 2 and date < 5:
			print("Sorry, we aren't able to calculate your zodiac because you are too old for the calculator.")

		elif year == 2023 and month == 1 and date > 21:
			print("Sorry, we aren't able to calculate your zodiac because you are too young for the calculator.")

		elif year == 2023 and month > 1:
			print("Sorry, we aren't able to calculate your zodiac because you are too young for the calculator.")
	
		elif year > 2023:
			print("Sorry, we aren't able to calculate your zodiac because you are too young for the calculator.")

		else:

			year = year_converter(month,date,year)
	
			zodiac = find_zodiac(year)
	
			person = Person(name, zodiac)   #uses __init__ method again
			person.find_element()			#uses find_element method again
			people_list.append(person)
			print()
			print(person)					#uses __str__ method again
			
			person_values = [person.name, person.zodiac, person.element]  #seperate values for writing to file
			person_values_list.append(person_values)                       # list of people's values
			
			calculate_again = input("\nWould you like to calculate another person's zodiac? Type 'y' for yes or any key for no.\n")


make_zodiac_file(person_values_list)
