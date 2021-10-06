/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main()
{
    
    // Declare & Initialise Variables
    int number = 22;
    char letterUpper = 'A';
    char letterLower = 'a';
    
    //exercise 1
    printf("Printing Variables\n");
    printf("Our number is %d: %x\n", number, number);
    printf("Our upper case letter is %c: %d: %x\n", letterUpper, letterUpper);
    printf("Our lower case letter is %c: %d: %x\n", letterLower, letterLower);
    
    //exercise 2
    printf("The number of bytes in %c is %d\n", letterLower, sizeof(letterLower));
    printf("The number of bytes in %d is %d\n", number, sizeof(number));
    
    //exercise 3
        int start = 0;    
        int i = 0;    
        for (i = start; i <= 255; i++ )   
        {      
            printf("%x", i);     
            if ((i+1)%16 == 0)
            {
                printf("\n");
            }
        }

    return 0;
}
