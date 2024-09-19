#zodiac_class_and_functions
import csv

class Person:

	def __init__(self, name='',zodiac=''):   #method 1
		self.name = name
		self.zodiac = zodiac
		self.element =''
		
	def find_element(self):					 #method 2
		fixed_elements = {'Rat':'Water', 'Ox': 'Earth','Tiger':'Wood', 'Rabbit': 'Wood',   
		'Dragon':'Earth', 'Snake':'Fire','Horse':'Fire', 'Goat':'Earth', 'Monkey':'Metal', 
		'Rooster':'Metal', 'Dog':'Earth', 'Pig':'Water'}

		for zodiac, element in fixed_elements.items():
			if zodiac == self.zodiac:
				self.element = element
		
		
	def __str__(self):						 #method 3
		return f'{self.name} was born in the year of the {self.zodiac}.\nThe fixed element for {self.zodiac} is {self.element}.'
	



#Conversion Function
'''
Takes your birthday as parameters and returns "chinese_year", which groups specific dates
of the gregorian calendar that fit into the Traditional Chinese Calendar years. The Traditional Chinese Calendar
years have animal zodiacs associated with each year. Grouping the dates into one year makes it easier to find a person's zodiac

Basically converts Gregorian dates into Traditional Chinese years, but with an inncorect year number.
'''

def year_converter(month,date,year):
	chinese_year = year 
#year stays the same unless born on some days in Jan and Feb in a specific year
		
#Nested selection statements	
	
	if month == 1 or month == 2:   						#only takes Jan and Feb
		if year == 1925 and month == 1 and date <= 23: #start with the end dates 
			chinese_year = 1924
		
		elif year== 1926 and month == 2 and date <= 12:
			chinese_year = 1925
		elif year == 1926 and month == 1 and date <= 31:
			chinese_year = 1925
		
		elif year== 1927 and month == 2 and date <= 1:
			chinese_year = 1926
		elif year == 1927 and month == 1 and date <= 31:
			chinese_year = 1926
		
		elif year== 1928 and month == 1 and date <= 22:
			chinese_year = 1927	
		
		elif year== 1929 and month == 2 and date <= 9:
			chinese_year = 1928
		elif year == 1929 and month == 1 and date <= 31:
			chinese_year = 1928
			
		elif year== 1930 and month == 1 and date <= 29:
			chinese_year = 1929

		elif year== 1931 and month == 2 and date <= 16:
			chinese_year = 1930
		elif year == 1931 and month == 1 and date <= 31:
			chinese_year = 1930
		
		elif year== 1932 and month == 2 and date <= 5:
			chinese_year = 1931
		elif year == 1932 and month == 1 and date <= 31:
			chinese_year = 1931
		
		elif year== 1933 and month == 1 and date <= 25:
			chinese_year = 1932

		elif year== 1934 and month == 2 and date <= 13:
			chinese_year = 1933
		elif year == 1934 and month == 1 and date <= 31:
			chinese_year = 1933
		
		elif year== 1935 and month == 2 and date <= 3:
			chinese_year = 1934		
		elif year == 1935 and month == 1 and date <= 31:
			chinese_year = 1934

		elif year== 1936 and month == 1 and date <= 23:
			chinese_year = 1935
		
		elif year== 1937 and month == 2 and date <= 10:
			chinese_year = 1936
		elif year == 1937 and month == 1 and date <= 31:
			chinese_year = 1936
	
		elif year== 1938 and month == 1 and date <= 30:
			chinese_year = 1937
			
		elif year== 1939 and month == 2 and date <= 18:
			chinese_year = 1938
		elif year == 1939 and month == 1 and date <= 31:
			chinese_year = 1938
			
		elif year== 1940 and month == 2 and date <= 7:
			chinese_year = 1939
		elif year == 1940 and month == 1 and date <= 31:
			chinese_year = 1939
			
		elif year == 1941 and month == 1 and date <= 26:
			chinese_year = 1940
		
		elif year == 1942 and month == 2 and date <= 14:
			chinese_year = 1941
		elif year == 1942 and month == 1 and date <= 31:
			chinese_year = 1941
	
		elif year == 1943 and month == 2 and date <= 4:
			chinese_year = 1942
		elif year == 1943 and month == 1 and date <= 31:
			chinese_year = 1942
			
		elif year == 1944 and month == 1 and date <= 24:
			chinese_year = 1943
			
		elif year == 1945 and month == 2 and date <= 12:
			chinese_year = 1944
		elif year == 1945 and month == 1 and date <= 31:
			chinese_year = 1944	
			
		elif year == 1946 and month == 2 and date <= 1:
			chinese_year = 1945
		elif year == 1946 and month == 1 and date <= 31:
			chinese_year = 1945
			
		elif year == 1947 and month == 1 and date <= 21:
			chinese_year = 1946
		
		elif year == 1948 and month == 2 and date <= 9:
			chinese_year = 1947
		elif year == 1948 and month == 1 and date <= 31:
			chinese_year = 1947
			
		elif year == 1949 and month == 1 and date <= 28:
			chinese_year = 1948
			
		elif year == 1950 and month == 2 and date <= 16:
			chinese_year = 1949
		elif year == 1950 and month == 1 and date <= 31:
			chinese_year = 1949

		elif year == 1951 and month == 2 and date <= 5:
			chinese_year = 1950
		elif year == 1951 and month == 1 and date <= 31:
			chinese_year = 1950

		elif year == 1952 and month == 1 and date <= 26:
			chinese_year = 1951
			
		elif year == 1953 and month == 2 and date <= 13:
			chinese_year = 1952
		elif year == 1953 and month == 1 and date <= 31:
			chinese_year = 1952
			
		elif year == 1954 and month == 2 and date <= 2:
			chinese_year = 1953
		elif year == 1954 and month == 1 and date <= 31:
			chinese_year = 1953
			
		elif year == 1955 and month == 1 and date <= 23:
			chinese_year = 1954
			
		elif year == 1956 and month == 2 and date <= 11:
			chinese_year = 1955
		elif year == 1956 and month == 1 and date <= 31:
			chinese_year = 1955
			
		elif year == 1957 and month == 1 and date <= 30:
			chinese_year = 1956
			
		elif year == 1958 and month == 2 and date <= 17:
			chinese_year = 1957
		elif year == 1958 and month == 1 and date <= 31:
			chinese_year = 1957
		
		elif year == 1959 and month == 2 and date <= 7:
			chinese_year = 1958
		elif year == 1959 and month == 1 and date <= 31:
			chinese_year = 1958
		
		elif year == 1960 and month == 1 and date <= 27:
			chinese_year = 1959
	
		elif year == 1961 and month == 2 and date <= 14:
			chinese_year = 1960
		elif year == 1961 and month == 1 and date <= 31:
			chinese_year = 1960
	
		elif year == 1962 and month == 2 and date <= 4:
			chinese_year = 1961
		elif year == 1962 and month == 1 and date <= 31:
			chinese_year = 1961
			
		elif year == 1963 and month == 1 and date <= 24:
			chinese_year = 1962
			
		elif year == 1964 and month == 2 and date <= 12:
			chinese_year = 1963
		elif year == 1964 and month == 1 and date <= 31:
			chinese_year = 1963
		
		elif year == 1965 and month == 2 and date <= 1:
			chinese_year = 1964
		elif year == 1965 and month == 1 and date <= 31:
			chinese_year = 1964
			
		elif year == 1966 and month == 1 and date <= 20:
			chinese_year = 1965
		
		elif year == 1967 and month == 2 and date <= 8:
			chinese_year = 1966
		elif year == 1967 and month == 1 and date <= 31:
			chinese_year = 1966
			
		elif year == 1968 and month == 1 and date <= 29:
			chinese_year = 1967
			
		elif year == 1969 and month == 2 and date <= 16:
			chinese_year = 1968
		elif year == 1969 and month == 1 and date <= 31:
			chinese_year = 1968
			
		elif year == 1970 and month == 2 and date <= 5:
			chinese_year = 1969
		elif year == 1970 and month == 1 and date <= 31:
			chinese_year = 1969
			
		elif year == 1971 and month == 1 and date <= 26:
			chinese_year = 1970
			
		elif year == 1972 and month == 2 and date <= 14:
			chinese_year = 1971
		elif year == 1972 and month == 1 and date <= 31:
			chinese_year = 1971
		
		elif year == 1973 and month == 2 and date <= 2:
			chinese_year = 1972
		elif year == 1973 and month == 1 and date <= 31:
			chinese_year = 1972
			
		elif year == 1974 and month == 1 and date <= 22:
			chinese_year = 1973
		
		elif year == 1975 and month == 2 and date <= 10:
			chinese_year = 1974
		elif year == 1975 and month == 1 and date <= 31:
			chinese_year = 1974
			
		elif year == 1976 and month == 1 and date <= 30:
			chinese_year = 1975

		elif year == 1977 and month == 2 and date <= 17:
			chinese_year = 1976
		elif year == 1977 and month == 1 and date <= 31:
			chinese_year = 1976
			
		elif year == 1978 and month == 2 and date <= 6:
			chinese_year = 1977
		elif year == 1978 and month == 1 and date <= 31:
			chinese_year = 1977
			
		elif year == 1979 and month == 1 and date <= 27:
			chinese_year = 1978
			
		elif year == 1980 and month == 2 and date <= 15:
			chinese_year = 1979
		elif year == 1980 and month == 1 and date <= 31:
			chinese_year = 1979

		elif year == 1981 and month == 2 and date <= 4:
			chinese_year = 1980
		elif year == 1981 and month == 1 and date <= 31:
			chinese_year = 1980
			
		elif year == 1982 and month == 1 and date <= 24:
			chinese_year = 1981
			
		elif year == 1983 and month == 2 and date <= 12:
			chinese_year = 1982
		elif year == 1983 and month == 1 and date <= 31:
			chinese_year = 1982
		
		elif year == 1984 and month == 2 and date <= 1:
			chinese_year = 1983
		elif year == 1984 and month == 1 and date <= 31:
			chinese_year = 1983
			
		elif year == 1985 and month == 2 and date <= 19:
			chinese_year = 1984
		elif year == 1985 and month == 1 and date <= 31:
			chinese_year = 1984
			
		elif year == 1986 and month == 2 and date <= 8:
			chinese_year = 1985
		elif year == 1986 and month == 1 and date <= 31:
			chinese_year = 1985
			
		elif year == 1987 and month == 1 and date <= 28:
			chinese_year = 1986
			
		elif year == 1988 and month == 2 and date <= 16:
			chinese_year = 1987
		elif year == 1988 and month == 1 and date <= 31:
			chinese_year = 1987
			
		elif year == 1989 and month == 2 and date <= 5:
			chinese_year = 1988
		elif year == 1989 and month == 1 and date <= 31:
			chinese_year = 1988
			
		elif year == 1990 and month == 1 and date <= 26:
			chinese_year = 1989
				
		elif year == 1991 and month == 2 and date <= 14:
			chinese_year = 1990
		elif year == 1991 and month == 1 and date <= 31:
			chinese_year = 1990
			
		elif year == 1992 and month == 2 and date <= 3:
			chinese_year = 1991
		elif year == 1992 and month == 1 and date <= 31:
			chinese_year = 1991
		
		elif year == 1993 and month == 1 and date <= 22:
			chinese_year = 1992
			
		elif year == 1994 and month == 2 and date <= 9:
			chinese_year = 1993
		elif year == 1994 and month == 1 and date <= 31:
			chinese_year = 1993
			
		elif year == 1995 and month == 1 and date <= 30:
			chinese_year = 1994
			
		elif year == 1996 and month == 2 and date <= 18:
			chinese_year = 1995
		elif year == 1996 and month == 1 and date <= 31:
			chinese_year = 1995
			
		elif year == 1997 and month == 2 and date <= 6:
			chinese_year = 1996
		elif year == 1997 and month == 1 and date <= 31:
			chinese_year = 1996
			
		elif year == 1998 and month == 1 and date <= 27:
			chinese_year = 1997
			
		elif year == 1999 and month == 2 and date <= 15:
			chinese_year = 1998
		elif year == 1999 and month == 1 and date <= 31:
			chinese_year = 1998
			
		elif year == 2000 and month == 2 and date <= 4:
			chinese_year = 1999
		elif year == 2000 and month == 1 and date <= 31:
			chinese_year = 1999
			
		elif year == 2001 and month == 1 and date <= 23:
			chinese_year = 2000
		
		elif year == 2002 and month == 2 and date <= 11:
			chinese_year = 2001
		elif year == 2002 and month == 1 and date <= 31:
			chinese_year = 2001
			
		elif year == 2003 and month == 1 and date <= 31:
			chinese_year = 2002
			
		elif year == 2004 and month == 1 and date <= 21:
			chinese_year = 2003
			
		elif year == 2005 and month == 2 and date <= 8:
			chinese_year = 2004
		elif year == 2005 and month == 1 and date <= 31:
			chinese_year = 2004
			
		elif year == 2006 and month == 1 and date <= 28:
			chinese_year = 2005
			
		elif year == 2007 and month == 2 and date <= 17:
			chinese_year = 2006
		elif year == 2007 and month == 1 and date <= 31:
			chinese_year = 2006
			
		elif year == 2008 and month == 2 and date <= 6:
			chinese_year = 2007
		elif year == 2008 and month == 1 and date <= 31:
			chinese_year = 2007
			
		elif year == 2009 and month == 1 and date <= 25:
			chinese_year = 2008
		
		elif year == 2010 and month == 2 and date <= 13:
			chinese_year = 2009
		elif year == 2010 and month == 1 and date <= 31:
			chinese_year = 2009
			
		elif year == 2011 and month == 2 and date <= 2:
			chinese_year = 2010
		elif year == 2011 and month == 1 and date <= 31:
			chinese_year = 2010
			
		elif year == 2012 and month == 1 and date <= 22:
			chinese_year = 2011
			
		elif year == 2013 and month == 2 and date <= 9:
			chinese_year = 2012
		elif year == 2013 and month == 1 and date <= 31:
			chinese_year = 2012
			
		elif year == 2014 and month == 1 and date <= 30:
			chinese_year = 2013
			
		elif year == 2015 and month == 2 and date <= 18:
			chinese_year = 2014
		elif year == 2015 and month == 1 and date <= 31:
			chinese_year = 2014
			
		elif year == 2016 and month == 2 and date <= 7:
			chinese_year = 2015
		elif year == 2016 and month == 1 and date <= 31:
			chinese_year = 2015
			
		elif year == 2017 and month == 1 and date <= 27:
			chinese_year = 2016
			
		elif year == 2018 and month == 2 and date <= 15:
			chinese_year = 2017
		elif year == 2018 and month == 1 and date <= 31:
			chinese_year = 2017
			
		elif year == 2019 and month == 2 and date <= 4:
			chinese_year = 2018
		elif year == 2019 and month == 1 and date <= 31:
			chinese_year = 2018
			
		elif year == 2020 and month == 1 and date <= 24:
			chinese_year = 2019
		
		elif year == 2021 and month == 2 and date <= 11:
			chinese_year = 2020
		elif year == 2021 and month == 1 and date <= 31:
			chinese_year = 2020
			
		elif year == 2022 and month == 1 and date <= 31:
			chinese_year = 2021
		
		elif year == 2023 and month == 1 and date <= 21:
			chinese_year = 2022
		
	return chinese_year



def find_zodiac(year):
	
	zodiac_list = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake',  #Data collection 2
	'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']
	zodiac =''
	
	"""The oldest year the calculator takes is 1924, which has most of the dates for the rat zodiac. 1924 % 100 % 12 is equal to 0.
	The rat is zodiac_list[0], so this calculation works nicely to find zodiacs from 1924 to 1999 because the remainders going to be
	inbetween 0 and 11. But it doesn't work for the year 2000 and after. """

	if year <= 1999:						
		for i in range(len(zodiac_list)):
			if ((year % 100) % 12) == i:
				zodiac = zodiac_list[i]
				
	"""Because 2000 % 100 % 12 is 0, the index for that is the rat zodiac. The calculation doesnt match the animal zodiac that 
	falls on most of the dates in 2000. Since 1999 has most for the rabbit zodiac and is zodiac_list[3], 2000 will be zodiac_list[4].
	To fix the issue with the year 2000 and after, we just added 4 to the original calculation and then mod divided it by 12."""

	if year > 1999:						
		for j in range(len(zodiac_list)):
			if ((((year % 100) % 12)+4)%12) == j:
				zodiac = zodiac_list[j]
	return zodiac

def make_zodiac_file(person_values_list):   #A function that makes a file that lists people who have used the zodiac calculator
	with open('ZodiacFile.csv', 'w',newline='') as csvfile:
		zodiac_writer = csv.writer(csvfile)
		
		row1 = ['Name', 'Zodiac', 'Element']
		zodiac_writer.writerow(row1)
		
		for i in person_values_list:	
			zodiac_writer.writerow(i)
