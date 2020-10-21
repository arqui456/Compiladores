#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void recursao (char string[], int tamS, int idx){

    if (idx == tamS){
      return;
    }

    if (string[idx] == '-'){
        printf("%d", idx + 1);
        recursao (string, tamS, idx + 1);
    } else {
        printf("(");
        printf("%d", idx + 1);
        recursao (string, tamS, idx + 1);
        printf(")");
    }
}

int main (){

  char string[105];
  scanf("%[^\n]", string);


  int tamS = strlen(string);
  recursao (string, tamS, 0);
  printf("\n");

  return 0;
}