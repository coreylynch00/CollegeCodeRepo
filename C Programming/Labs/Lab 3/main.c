#include <stdio.h>
#include <limits.h>

int main(){
    
    // Exercise 1
    /*
    int num1;
    num1 = 0xFFFF;
    
    printf("num1 has a value of %d: %x\n", (num1), (num1));
    
    int bytes = sizeof(num1);
    int bits = sizeof(num1)*8;
    printf("num1 uses %d bytes: %d bits\n", (bytes), (bits));
    
   int max_value = INT_MAX;
   int min_value = INT_MIN;
    printf("Max/Min value in num1 is %d / %d\n", INT_MAX, INT_MIN);
    */
    
    // Exercise 2
    /*
    // Capitalize lower case letter
    char keyinput;
    printf("Please enter a key input:\n");
    keyinput = (char) getchar();
    getchar();
    
    putchar(toupper(keyinput));
    */
    
    /*
    printf("Please enter a key input:\n");
    char keyinput;
    
    while(1){
        keyinput = (char) getchar();
        
        if (keyinput == '\n'){
            break;
        }
        
        else if (keyinput >= 'A' && keyinput <= 'Z'){
            keyinput = keyinput + 32;
            printf("%c", keyinput);
        }
        
        else if (keyinput >= 'a' && keyinput <= 'z'){
         keyinput = keyinput - 32;  
         printf("%c", keyinput);
        }
        
        else{
            putchar(keyinput);
        }
    }
    */
    
    int array[5][5];
    int row, col;
    int i = 0;
    
    for (row = 0; row < 5; row++){
        for (col = 0; col < 5; col++){
            array[row][col] = 0;
        }
    }
    
    char x, y, value;
    while(1){
        
        printf("What is x location?");
        x = getchar() - '0';
        getchar();
        
        printf("What is y location?");
        y = getchar() - '0';
        getchar();
        
        printf("What value do you want to assign?");
        value = getchar() - '0';
        getchar();
        
        array[y-1][x-1] = value;
        
        printf("Do you want to continue? y or n?\n");
        if (getchar() == 'n'){
            break;
        }
        getchar();
    }
    
    printf("\n");
    for(row=0; row<5; row++){
        for(col=0; col<5;col++){
            printf("%02d ", array[row][col]);
        }
        printf("\n");
    }
    
    
    return 0;
}


