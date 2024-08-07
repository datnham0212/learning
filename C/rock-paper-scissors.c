#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int theirMove(){
    srand(time(NULL));
    int r = (rand() % 3) + 1;
    return r;
}

void playerRock(int opponentMove){
    if(opponentMove == 3){
        printf("You win");
    }
    else if(opponentMove == 2){
        printf("You lose");
    }
    else{
        printf("Draw");
    }
}

void playerPaper(int opponentMove){
    if(opponentMove == 1){
        printf("You win");
    }
    else if(opponentMove == 3){
        printf("You lose");
    }
    else{
        printf("Draw");
    }
}

void playerScissor(int opponentMove){
    if(opponentMove == 2){
        printf("You win");
    }
    else if(opponentMove == 1){
        printf("You lose");
    }
    else{
        printf("Draw");
    }
}

void game(){
    
    int opponentMove = theirMove();

    int playerMove;
    scanf("%d", &playerMove);
    
    switch(playerMove){
        case 1:
            playerRock(opponentMove);
            break;
        
        case 2:
            playerPaper(opponentMove);
            break;
        
        case 3:
            playerScissor(opponentMove);
            break;
        
        default:
            printf("Not acceptable");
            break;
    }
    printf("\nOpponent move: %d\n", opponentMove);
}

int main(){
    
    int rounds = 3;    
    while(rounds > 0){
        game();
        rounds--;
    }
    
    return 0;
}
