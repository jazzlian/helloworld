#include <stdlib.h>
#include <stdio.h>

#define BRIGHT 1
#define RED 31
#define BG_BLACK 40

int
main(int argc, char **argv)
{

    printf("%c[%d;%d;%dm Hello World", 0x1B, BRIGHT,RED,BG_BLACK);
	return EXIT_SUCCESS;
}
