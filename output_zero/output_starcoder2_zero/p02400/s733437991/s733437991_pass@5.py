Below is a C program that works as intended, but I need you to refactor the code to reduce its lines and complexity, while preserving its functionality. Make the code cleaner, more concise, and improve its readability.

Here is the original C program:

	#include <stdio.h>
	
	int main(void) {
	    float r;
	
	    printf("Enter the radius of the circle: ");
	    scanf("%f", &r);
	
	    const double PI = 3.14159265358979323846;
	    printf("The area is %.2f and the circumference is %.2f\n",
	        PI * r * r, 2 * PI * r);
	}


Please provide the refactored version of the code with fewer lines and improved readability. 
DO NOT include any explanations, introductions, or concluding remarks. Just give me the C code.