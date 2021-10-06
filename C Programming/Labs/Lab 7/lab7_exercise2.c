#include <stdio.h>

int counting_vowels(const char array[], int vowel_counts[]){

    
    if (array == NULL || vowel_counts == NULL){
        // return an error code
        return 1;
    }
    
    int i;
    for (i=0;i<5;i++){
        // initialising the vowel counts to 0
        vowel_counts[i] = 0;
    }
    
    for (i=0; array[i]!='\0'; i++){
        
        switch(array[i]){
            case 'A':
                // no break means we move on to the next body
            case 'a': 
                vowel_counts[0] ++; break;
            case 'E':
            case 'e':
                vowel_counts[1] ++; break;
            case 'I':
            case 'i':
                vowel_counts[2] ++; break;
            case 'o':
            case 'O':
                vowel_counts[3] ++; break;
            case 'u':
            case 'U':
                vowel_counts[4] ++; break;
            default:
                break;
        }
    }
    
    return 0;
}


void main(){
    
    char text[200];
    char input;
    int i = 0;
    int vowel_counts[] = {0, 0, 0, 0, 0};
    
    while(1){
        input = getchar();
        if (input=='\n') break;
        
        text[i] = input;
        i++;
    }
    text[i] = '\0';
    counting_vowels(text, vowel_counts);
    
    char vowel_chars[] = {'a', 'e', 'i', 'o', 'u'};
    
    printf("You entered:\n%s\n", text);
    printf("Vowel count:\n");
    for (i=0;i<5;i++){
        switch(i){
            case 0: printf("a -> %d\n", vowel_counts[0]);break;
            case 1: printf("e -> %d\n", vowel_counts[1]);break;
            case 2: printf("i -> %d\n", vowel_counts[2]);break;
            case 3: printf("o -> %d\n", vowel_counts[3]);break;
            case 4: printf("u -> %d\n", vowel_counts[4]);break;
        }
    }
    
    //for (i=0;i<5;i++){
    //    printf("%c -> %d\n", vowel_chars[i], vowel_counts[i]);
    //}
    
}





