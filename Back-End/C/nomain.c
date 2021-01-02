/*
 * Compile and run program without main()
 * 
 * NOTE: Use command gcc -nostartfiles nomain.c 
* /*/


_Noreturn void nomain(void)
{
	printf("Hello World\n");
	printf("Successfully run without main...\n");
	exit(0);
}