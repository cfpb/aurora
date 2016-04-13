#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
  if (argc == 2) {
    int seconds = atoi(argv[1]);
    if (seconds != 0) {
      while (1) {
        printf("Hello world!\n");
        sleep(seconds);
      }
    } else {
      printf("Seconds must be an integer greater than zero.\n");
      return 1;
    }
  } else {
    printf("Must supply the number of seconds to sleep, and nothing else.\n");
    return 1;
  }
  return 0;
}
