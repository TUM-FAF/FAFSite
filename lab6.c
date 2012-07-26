#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <string.h>
void sorting(char **tab, int l);
main()
{
  char ** tab = NULL, str[200];
  char * pch = NULL;
  int i,n=0;
printf("Introdueti string-ul");
  gets(str);
  pch = strtok(str, " ,.;:?!");
  tab = (char**)malloc(n*sizeof(char));
  while(pch != NULL)
  {
            tab = (char**)realloc(tab, (n+1)*sizeof(*tab));
            tab[n]= (char*)malloc(strlen(pch)*sizeof(char));
  tab[n]=pch;
  pch = strtok(NULL, " ,.;:?!");
  n++;  
            }                  
  sorting(tab, n);
            for(i=0; i<n; i++){
                     printf("%s ", tab[i]);
                    }
getch();
}


void sorting(char **tab, int l){
     int i,j;
     char *tmp;
     for(i=0; i<l; i++){
              for(j=i+1; j<l; j++){
                         tmp=tab[j];
                         if((i<j && strcmp(tab[i],tmp)<0) || (i>j && strcmp(tab[i],tmp)>0)){
                                                  tab[j]=tab[i];
                                                  tab[i]=tmp;
                                                  }
                         }
              }
   
     }
