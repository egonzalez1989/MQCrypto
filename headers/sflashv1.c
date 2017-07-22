#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
	if(argc < 3)
	{
		fprintf(stderr, "Give 2 args!\n");
		exit(-1);
	}

	char *arg1 = argv[1];
	char *arg2 = argv[2];

	int status = system("sage -python ../python/sflashv1_test.py");
	//fprintf(stdout, "You gave: %s, %s\n", arg1, arg2);

	return 0;
}