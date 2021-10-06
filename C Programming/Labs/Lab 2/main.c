/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
C#, VB, Perl, Swift, Prolog, Javascript, Pascal, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main()
{
    // EXERCISE 1.1
    /* 
    char keyinput;
    printf("Please input character from keyboard, followed by Enter\n");
    keyinput = (char) getchar();
    getchar(); 
    
    printf("Character entered %d\n", keyinput);
    printf("Character entered %c\n", keyinput);
    */
    
    //EXERCISE 1.2
    /*
    char letterX = 'X';
    putchar(letterX);
    */
    
    //EXERCISE 1.3 - 1.5
    /*
    char firstName;
    char lastName;
    
    printf("Please enter your first name initial, followed by Enter.\n");
    firstName = getchar();
    // firstName = firstName + 1;   INCREMENT INTIAL BY 1
    getchar();
    
    if (firstName > 91){
        firstName = firstName - 32;
    }
    
    
    printf("Please enter your last name initial, followed by Enter.\n");
    lastName = getchar();
    // lastName = lastName + 1; INCREMENT INTIAL BY 1
    getchar();
        
     if (lastName > 91){
        lastName = lastName - 32;
    }
    
    printf("Your initials are: ");
    putchar(firstName);
    putchar('.');
    putchar(lastName);
    putchar('.');
    printf("\n");
    
    printf("Your initials are: %c.%c.\n", firstName, lastName);
    */
    
    char initials[5]; // allocates an array of 5 bytes
    
    initials[0] = 'R';
    initials[1] = '.';
    initials[2] = 'D';
    initials[3] = '.';
    initials[4] = '\0'; //  \0 or null char is used to indicate the end of an array. 
                        //   Terminates the process of reading memory slots once \0 is reached.
    
    printf("%s\n", initials);
    printf("Index 4 of our string is %d\n", initials[4]);
    
    char newInitials[] = "R.D.";
    
    printf("%s\n", newInitials);
    printf("Index 4 of our string is %d\n", newInitials[4]);
    
    char word[5];
    word[0] = 'c';
    word[1] = 'a';
    word[2] = 't';
    word[3] = 's';
    word[4] = '\0';
    
    printf("The word is: %s\n", word);
    
    char name[] = "Corey";
    printf("Bytes allocated to name array: %d\n", sizeof(name));
    
    int num[] = {3, 6, 9, 12, 15};
    printf("Bytes allocated to numbers array: %d\n", sizeof(num));
    
    int numbers[4];
    numbers[0] = 1;
    numbers[1] = 12;
    numbers[2] = 123;
    numbers[3] = 1234;
    printf("Bytes allocated to numbers array: %d\n", sizeof(numbers));
    
    
    return 0;
}


