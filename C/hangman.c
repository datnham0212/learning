#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int uniqueChar(char *word){
    int ucount = 0;
    for(int i = 0; i < strlen(word); i++){
        int flag = 0;
        for(int j = 0; j < i; j++){
            if(word[i] == word[j]){
                flag = 1;
                break;
            }
        }
        if(flag == 0){
            ucount++;
        }
    }
    return ucount;
}

int main()
{
    printf("Hangman\n");
    
    char word[] = "programming";
    
    char guess;
    
    int turns = uniqueChar(word);
    
    printf("%d", turns);
    printf("Guess the word: ");
    while(turns > 0){
        scanf("%c", &guess);
        
        char *found;
        
        found = strchr(word, guess);
        for(int i = 0; i < sizeof(word); i++){
            if(found != NULL){
                printf("%c at %ld\n", guess, found-word+1);
                found = strchr(found+1, guess);
            }
        }    
    }
    return 0;
}
