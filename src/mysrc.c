//The .c file with the functions themselves.
#include "mysrc.h"

#include <stdio.h>

void mybasic(void){
  printf("mybasic() called\n");
  return;
}

int myprint(char*message){
  return printf("%s\n",message);
}

double myadd(double x, double y){
  return x+y;
}
