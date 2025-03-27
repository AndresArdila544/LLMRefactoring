The original program works as follows:

If the user inputs a “-” (a dash, not an equal sign), the program ends its loop. 
Else, if the user has not entered any dashes yet, it reads in the text string and saves it to C (for "Character").
Then it reads in the number of iterations m and then for each iteration i from 0 to m - 1, it prints out a substring of C starting at index i with length C's length. 
The updated value of C is saved again as C, so that we can continue cycling through the string.