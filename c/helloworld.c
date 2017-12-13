#include <stdlib.h>
#include <stdio.h>

int
main(int argc, char **argv)
{

    printf("%c[%d;%dmHello World%c[%dm\n",27,1,33,27,0);
	return EXIT_SUCCESS;
}
