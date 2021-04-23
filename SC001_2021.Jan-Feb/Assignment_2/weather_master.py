"""
File: weather_master.py
Name: DiCheng
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# enter EXIT_CODE to exit while loop
EXIT_CODE = -100


def main():
	"""
	pre-cond: User can enter series of temperatures, using hint number to quit enter.
	post-cond: stanCode "Weather Master 4.0" will give you highest, lowest, average temperatures
				and the count of cold days among given numbers.
	"""
	print("stanCode \"Weather Master 4.0\"!")
	# define variables
	data = int(input("Next Temperature: (or " + str(EXIT_CODE) + " to quit)? "))
	data_highest = data
	data_lowest = data
	data_sum = 0
	data_count = 0
	cold_days_count = 0
	while data != EXIT_CODE:
		# calculate count of data and summary of data.
		data_count += 1
		data_sum += data
		# compare data with current data_highest and data_lowest, then reassign variables if True.
		if data > data_highest:
			data_highest = data
		if data < data_lowest:
			data_lowest = data
		# count the number of data which is under 16.
		if data < 16:
			cold_days_count += 1
		data = int(input("Next Temperature: (or " + str(EXIT_CODE) + " to quit)? "))
	# EXIT entering input, print the outcomes.
	if data_count != 0:
		print("Highest temperature = " + str(data_highest))
		print("Lowest temperature = " + str(data_lowest))
		print("Average = " + str(data_sum/data_count))
		print(str(cold_days_count) + " cold day(s)")
	else:
		print("No temperatures were entered.")


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
