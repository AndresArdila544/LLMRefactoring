s = input()
print("{}:{:02d}:{:05.2f}".format(int(s//360), int(s%60), s*100 % 60)) # This one-liner converts the given time to hours, minutes and seconds format with two decimal places of precision in seconds.

Explanation:

The input() function takes user's input from stdin (standard input) and stores it in a variable s. 
The // operator is used for integer division which returns the floor value of the quotient of s divided by 360, so that the hours are obtained.
% operator is used to get the remainder after dividing s by 360. This remainder value represents minutes.
The % operator is again used to get the seconds in this case.

The format() method is called on a string with "{}:{:02d}:{:05.2f}" as its argument, where {} represents the integer part of s//360 (hours), {:02d} represents two digits for minutes and {:05.2f} represents the seconds in two decimal places.
The last argument is a string representation of s*100%60 to get only the fractional part of the seconds with precision 2, which gives the required output format.

The result is printed using print statement with the formatted string.