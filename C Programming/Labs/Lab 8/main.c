
#include <stdio.h>


/*Exercise 1
struct student{
    char name[10];
    int grade;
};

int change_grade(struct student *s, int new_grade){
    if (s == NULL) return 1;
    s->grade = new_grade;
    return 0;
}

int main()
{
    struct student s;
    printf("Name: ");
    scanf("%s", s.name);
    change_grade(&s, 90);
    
    printf("%s --> %d%%\n", s.name, s.grade);

    return 0;
}*/

//Exercise 2 
struct letter_analysis{
    char letter;
    int count;
};

void letter_count(const char text[], struct letter_analysis array_of_letter[]){
    
    //go through text and count occurances of letters
    int i = 0;
    for (i=0;text[i] != '\0'; i++){
       //go through each letter until we see a null char
       if('a' <= text[i] && 'z' >= text[i]){
           array_of_letter[text[i]-'a'].count++;
       }
       else if('A' <= text[i] && 'Z' >= text[i]){
           array_of_letter[text[i]-'A'].count++;
       }
    }
}

int main(){
    
    struct letter_analysis alphabet[26];
    char text[100];
    char input;
    char i;
    int idx = 0;
    
    for (i='a';i<='z';i++){
        alphabet[i-'a'].letter = i;
        alphabet[i-'a'].count = 0;
    }
    
    //read in a line of text from the user 
    while(1){
        input = getchar();
        if (input == '\n') break;
        
        text[idx] = input;
        idx++;
    }
    text[idx] = '\0';
    
    //call function to analyse the user text
    letter_count(text, alphabet);
    
    for (i = 'a';i<='z';i++){
        printf("%c -> %d\n", alphabet[i-'a'].letter, alphabet[i-'a'].count);
    
    }
    
    return 0;
}

