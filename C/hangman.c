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
    
    int wordLength = strlen(word);
    
    char temp[wordLength+1];
    
    for(int i = 0; i < wordLength; i++){
        temp[i] = '_'; 
    }    
    
    temp[wordLength] = '\0';
    
    while(turns > 0){
        printf("Guess the word: ");
        printf("%s\n", temp);
        
        scanf("\n%c", &guess);
        
        char *found;
        
        found = strchr(word, guess);
        
        while(found != NULL){
            temp[found-word] = guess;
            found = strchr(found+1, guess);
        }
        turns--;
    }
    printf("\nResult: %s", word);
    return 0;
}
