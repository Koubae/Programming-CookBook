#include <stdio.h>               //contains printf,scanf etc
#include <stdlib.h>
#include <string.h>             //contains strcmp(),strcpy(),strlen(),etc
#include <windows.h>
#include <conio.h>             //contains delay(),getch(),gotoxy(),etc.
#include <ctype.h>            //contains toupper(), tolower(),etc
// #include <direct.h>
#include <time.h>


#define RETURNTIME 15


/* ========== < STRUCT> ==========*/

struct MeroDate
{
	int day;
	int month;
	int year;
};

struct Books
{
	char stname[20];
	char name[20];
	char author[20];
	char *cat;

	int id;
	int quantity;
	int count;
	int rackno;

	float price;
		
	struct MeroDate issued;
	struct MeroDate duedate;
};
struct Books book;


/* ========== < FUNCTION PROTOTYPES > ==========*/

void returnFunc(void);
void mainMenu(void);
void addBooks(void);
void deleteBooks(void);
void editBooks(void);
void searchBooks(void);
void issueBooks(void);
void viewBooks(void);
void closeApplication(void);

int getData();
int checkId(int);
int getTime(void); // QST:??? What is this?

void Password();
void issueRecord();
void loadEranim();

 
/* ========== < GLOBAL VARIABLES > ==========*/


char categories[][15] = {"Computer","Electronics","Electrical","Civil","Mechnnical","Architecture"};
char findbook;
char password[12] = {"federico"};

int s;

// Global Files 
FILE *fp, *ft, *fs;


/* ========== < WINDOWS.H CONSTANTS > ==========*/


COORD coord = {0, 0};
COORD max_res, cursor_zize;

void gotoxy(int x, int y)
{
	coord.X = x; coord.Y = y;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

void delay(unsigned int mseconds)
{
	clock_t goal = mseconds + clock();
	while (goal > clock());
}

/* ========== < MAIN > ==========*/

int main()

{
	Password();
	getch();
	return 0;
}


/* ========== < MAIN MENU > ==========*/

void mainMenu()
{
	system("cls");
	int i;

	// ------------------------ VIEW ---------------------------------
	printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 MAIN MENU \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
	//show_mouse();
	gotoxy(20,5);
	printf("\xDB\xDB\xDB\xDB\xB2 1. Add Books   ");
	gotoxy(20,7);
	printf("\xDB\xDB\xDB\xDB\xB2 2. Delete books");
	gotoxy(20,9);
	printf("\xDB\xDB\xDB\xDB\xB2 3. Search Books");
	gotoxy(20,11);
	printf("\xDB\xDB\xDB\xDB\xB2 4. Issue Books");
	gotoxy(20,13);
	printf("\xDB\xDB\xDB\xDB\xB2 5. View Book list");
	gotoxy(20,15);
	printf("\xDB\xDB\xDB\xDB\xB2 6. Edit Book's Record");
	gotoxy(20,17);
	printf("\xDB\xDB\xDB\xDB\xB2 7. Close Application");
	gotoxy(20,19);
	printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
	gotoxy(20,20);
	// --------------------------------------------------------------
	getTime();  // Shows Date & Time
	gotoxy(20, 21);

	printf("Enter your choice: ");

	switch(getch())
	{
		case '1' :
					addBooks();
					break;
		case '2' :
					deleteBooks();
					break;
		case '3' :
					searchBooks();
					break;
		case '4' :
					issueBooks();
					break;
		case '5' :	
					viewBooks();
					break;
		case '6' :	
					editBooks();
					break;
		case '7' :	
				{
					system("cls");
					gotoxy(16, 3);
					gotoxy(16,4);					
					gotoxy(10,17);
					printf("Exiting in 3 second...........>");
					delay(3000);
					exit(0);
					break;
				}				

		default:
				{
					gotoxy(10,23);
					printf("\aWrong Entry!!Please re-entered correct option");
					if(getch())
						mainMenu();
				}
	}

}

void Password(void)
{
	system("cls");
	char d[25] = "Password Protected";
	char ch, pass[10];
	int i = 0, j;
	gotoxy(10, 4);

	/* DELAY */
	for (j=0; j<20; j++) {  // Left Side
		delay(25);
		printf("*");
	}
	printf(" < ");  // Left separator
	for (j=0; j<20; j++){ // Center
		delay(25);		
		printf("%c", d[j]);
		
	}
	printf(" > ");   // Right separator
 
	for (j=0; j<20; j++) {  // Right;
		delay(25);
		printf("*");
	}

	gotoxy(10, 10);
	gotoxy(15, 7);
	printf("Enter Secret Passwod: ");
	
	while (ch != 13) {

		ch = getch();

		if (ch != 13 && ch != 8) {// NOTE: 13 = carriage return 8: Backspace
			putch('*');
			
			pass[i] = ch;
			i++;
		}
	}

	pass[i] = '\0';

	if (strcmp(pass, password)== 0) {
		gotoxy(15, 9);
		// textcolor(BLINK);
		printf("Password match");
		gotoxy(17,10);
		printf("Press any key to countinue.....");
		getch();
		mainMenu();
	}
}



/* ========== < BOOKS FUNCTIONS DECLARATION > ==========*/

void addBooks(void)
{
	system("cls");
	int i; 

	// ------------------------ VIEW ---------------------------------
	gotoxy(20,5);
	printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2SELECT CATEGOIES\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
	gotoxy(20,7);
	printf("\xDB\xDB\xDB\xDB\xB2 1. Computer");
	gotoxy(20,9);
	printf("\xDB\xDB\xDB\xDB\xB2 2. Electronics");
	gotoxy(20,11);
	printf("\xDB\xDB\xDB\xDB\xB2 3. Electrical");
	gotoxy(20,13);
	printf("\xDB\xDB\xDB\xDB\xB2 4. Civil");
	gotoxy(20,15);
	printf("\xDB\xDB\xDB\xDB\xB2 5. Mechanical");
	gotoxy(20,17);
	printf("\xDB\xDB\xDB\xDB\xB2 6. Architecture");
	gotoxy(20,19);
	printf("\xDB\xDB\xDB\xDB\xB2 7. Back to main menu");
	gotoxy(20,21);
	printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
	gotoxy(20,22);
	printf("Enter your choice:");
	// --------------------------------------------------------------

	scanf("%d",&s);

	if (s == 7)
		mainMenu();

	system("cls");

	fp=fopen("lib.dat", "ab+");

	if (getData() == 1) {
		book.cat = categories[s-1];
		fseek(fp, 0, SEEK_END);
		fwrite(&book, sizeof(book), i, fp);
		fclose(fp);

		gotoxy(21, 14);
		printf("The record is sucessfully saved");	

		gotoxy(21,15);		
		printf("Save any more?(Y / N):");

		if(getch() == 'n')
		    mainMenu();
		else {
			system("cls");
		    addBooks();
		}
		    
	}
}


void deleteBooks()
{
	system("cls");
	int d;
	char another = 'y';

	while (another == 'y') {
		system("cls");
		gotoxy(10, 5);
		printf("Enter the Book ID to  delete:");
		scanf("%d", &d);
		fp=fopen("lib.dat","rb+");
		rewind(fp);

		while (fread(&book, sizeof(book), 1, fp) == 1) {

			if (book.id == d) {

				gotoxy(10, 7);
				printf("The book record is available");

				gotoxy(10, 8);
				printf("Book name is %s", book.name);

				gotoxy(10, 9);
				printf("Rack No. is %d", book.rackno);
				findbook='t';
			}
		}

		if (findbook != 't') {
			gotoxy(10, 10);
			printf("No record is found to modify the search");

			if (getch())
				mainMenu();
		}

		if (findbook == 't') {
			gotoxy(10, 9);
			printf("Do you want to delete it?(Y/N):");

			if (getch() == 'y') {
				ft = fopen("temp.dat", "wb+");  // temp file to delete
				rewind(fp);

				while (fread(&book, sizeof(book), 1, fp) == 1) {
					if (book.id != d) {
						fseek(ft, 0, SEEK_CUR);
						fwrite(&book, sizeof(book), 1, ft); // write in temp file
					}
				}
				fclose(ft);
				fclose(fp);

				remove("lib.dat");
				rename("temp.dat", "lib.dat");  

				fp = fopen("lib.dat", "rb+");

				if (findbook == 't') {
					gotoxy(10, 10);
					printf("The record is sucessfully deleted");
				    gotoxy(10,11);
				    printf("Delete another record?(Y/N)");
				}
			}
			else 
				mainMenu();

			fflush(stdin);
			another = getch();

		}
	}
	gotoxy(10, 15);
    mainMenu();

}


void searchBooks()
{
	system("cls");
	int d;

	// ------------------------ VIEW ---------------------------------
	printf("*****************************Search Books*********************************");
    gotoxy(20, 10);
    printf("\xDB\xDB\xDB\xB2 1. Search By ID");
    gotoxy(20,14);
    printf("\xDB\xDB\xDB\xB2 2. Search By Name");
    gotoxy( 15, 20);
    printf("Enter Your Choice");
    // --------------------------------------------------------------
    fp = fopen("lib.dat", "rb+"); 
    rewind(fp);

    switch(getch())
    {
    	case '1' :
			    	{	
			    		system("cls");
					    gotoxy(25, 4);
					    printf("****Search Books By Id****");
					    gotoxy(20, 5);
					    printf("Enter the book id:");
					    scanf("%d", &d);
					    gotoxy(20, 7);
					    printf("Searching........");
					    while (fread(&book, sizeof (book), 1, fp) == 1) {
					    	if (book.id == d) {
					    		delay(2);
					    		// ------------------------ VIEW ---------------------------------
							    gotoxy(20, 7);
							    printf("The Book is available");

							    gotoxy(20, 8);
							    printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
							    
							    gotoxy(20, 9);
							    printf("\xB2 ID:%d", book.id);
							    gotoxy(47, 9);
							    printf("\xB2");
							    
							    gotoxy(20, 10);
							    printf("\xB2 Name:%s", book.name);
							    gotoxy(47, 10);
							    printf("\xB2");
							    
							    gotoxy(20, 11);
							    printf("\xB2 Author:%s ",book.author);
							    gotoxy(47, 11);
							    printf("\xB2");

							    gotoxy(20, 12);
							    printf("\xB2 Qantity:%d ",book.quantity);
							    gotoxy(47, 12);
							    printf("\xB2"); 
							    gotoxy(47, 11);
							    printf("\xB2");

							    gotoxy(20, 13);
							    printf("\xB2 Price:Rs.%.2f",book.price);
							    gotoxy(47, 13);
							    printf("\xB2");

							    gotoxy(20, 14);
							    printf("\xB2 Rack No:%d ",book.rackno);
							    gotoxy(47, 14);
							    printf("\xB2");

							    gotoxy(20, 15);
							    printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
							    // --------------------------------------------------------------

							    findbook='t';
					    	}
					    }

					    if (findbook != 't') {
					    	gotoxy(20, 8);
						    printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
						    gotoxy(20, 9);
						    printf("\xB2");  
						    gotoxy(38,9);
						    printf("\xB2");
						    gotoxy(20, 10);
						    printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
						    gotoxy(22, 9);
						    printf("\aNo Record Found");
					    }

					    gotoxy(20, 17);
	    				printf("Try another search?(Y/N)");

	    				if(getch() == 'y')
						    searchBooks();
						else
						    mainMenu();
			    		break;
			    	}

		case '2' :
			    	{	

			    		char s[15];
			    		int d= 0;
					    system("cls");
					    gotoxy(25, 4);
					    printf("****Search Books By Name****");
					    gotoxy(20, 5);
					    printf("Enter Book Name:");
					    scanf("%s", s);
					    
					    while (fread(&book, sizeof (book), 1, fp) == 1) {
					    	if (strcmp(book.name, (s)) == 0) {
					    		// ------------------------ VIEW ---------------------------------
					    		gotoxy(20, 7);
							    printf("The Book is available");
							    gotoxy(20, 8);
							    printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
							    
							    gotoxy(20, 9);
							    printf("\xB2 ID:%d",book.id);
							    gotoxy(47, 9);
							    printf("\xB2");

							    gotoxy(20, 10);
							    printf("\xB2 Name:%s",book.name);
							    gotoxy(47, 10);
							    printf("\xB2");

							    gotoxy(20, 11);
							    printf("\xB2 Author:%s",book.author);
							    gotoxy(47, 11);
							    printf("\xB2");

							    gotoxy(20, 12);
							    printf("\xB2 Qantity:%d",book.quantity);
							    gotoxy(47, 12);
							    printf("\xB2");

							    gotoxy(20, 13);
							    printf("\xB2 Price:Rs.%.2f",book.price);
							    gotoxy(47, 13);
							    printf("\xB2");

							    gotoxy(20, 14);
							    printf("\xB2 Rack No:%d ",book.rackno);
							    gotoxy(47, 14);
							    printf("\xB2");
							    gotoxy(20, 15);
							    printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
							    // --------------------------------------------------------------
							    d++;
					    	}
					    }

					    if (d == 0) {
					    	gotoxy(20, 8);
						    printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
						    gotoxy(20, 9);
						    printf("\xB2");  
						    gotoxy(38, 9);
						    printf("\xB2");

						    gotoxy(20, 10);
						    printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
						    gotoxy(22, 9);
						    printf("\aNo Record Found");
					    }
					     	gotoxy(20, 17);
						    printf("Try another search?(Y/N)");

						    if(getch() == 'y')
						    	searchBooks();
						    else
						    	mainMenu();
			    		break;
			    	}

		default  :
					getch();
					searchBooks();
    }
    fclose(fp);

}

void issueBooks(void)
{
	int t;

	system("cls");
	// ------------------------ VIEW ---------------------------------
	printf("********************************ISSUE SECTION**************************");
    gotoxy(10, 5);
    printf("\xDB\xDB\xDB\xDb\xB2 1. Issue a Book");
    gotoxy(10, 7);
    printf("\xDB\xDB\xDB\xDb\xB2 2. View Issued Book");
    gotoxy(10, 9);
    printf("\xDB\xDB\xDB\xDb\xB2 3. Search Issued Book");
    gotoxy(10, 11);
    printf("\xDB\xDB\xDB\xDb\xB2 4. Remove Issued Book");
    gotoxy(10, 14);
    printf("Enter a Choice:");
    // --------------------------------------------------------------

    switch(getch())
    {
    	case '1'  :
			    	{	

			    		system("cls");
						int c = 0;
						char another = 'y';
						while(another == 'y') {
							system("cls");
				    		gotoxy(15, 4);
							printf("***Issue Book section***");
							gotoxy(10, 6);
							printf("Enter the Book Id:");
							scanf("%d", &t);
							fp=fopen("lib.dat","rb");
							fs=fopen("issue.dat","ab+");

							if (checkId(t) == 0) { //issues those which are present in library
								 gotoxy(10, 8);
							     printf("The book record is available");
							     gotoxy(10, 9);
							     printf("There are %d unissued books in library ",book.quantity);
							     gotoxy(10, 10);
							     printf("The name of book is %s",book.name);
							     gotoxy(10, 11);
							     printf("Enter student name:");
							     scanf("%s", book.stname);						   
							     gotoxy(10, 12);
							     printf("Issued date=%d-%d-%d",book.issued.day,book.issued.month,book.issued.year);
							     gotoxy(10, 13);
							     printf("The BOOK of ID %d is issued",book.id);
							     book.duedate.day=book.issued.day+RETURNTIME;   //for return date
							     book.duedate.month=book.issued.month;
							     book.duedate.year=book.issued.year;

							     if (book.duedate.day > 30) {
							     	book.duedate.month += book.duedate.day / 30;
							     	book.duedate.day -= 30;
							     }

							     if (book.duedate.month > 12) {
							     	book.duedate.year += book.duedate.month / 12;
							     	book.duedate.month -= 12;
							     }
							     gotoxy(10,14);
							     printf("To be return:%d-%d-%d",book.duedate.day,book.duedate.month,book.duedate.year);
							     fseek(fs, sizeof(book), SEEK_END);
							     fwrite(&book, sizeof(book), 1, fs);
							     fclose(fs);
							     c=1;
							}

							if (c == 0) {
								gotoxy(10, 11);
								printf("No record found");

							}

							gotoxy(10, 15);
							printf("Issue any more(Y/N):");
							fflush(stdin);
							another = getche();
							fclose(fp);
						}		    		

			    		break;
			    	}

		case '2'  :
			    	{
			    		system("cls");
						int j = 4;
						printf("*******************************Issued book list*******************************\n");
						gotoxy(2, 2);
						printf("STUDENT NAME    CATEGORY    ID    BOOK NAME    ISSUED DATE    RETURN DATE");
					    fs=fopen("issue.dat", "rb");
					    while(fread(&book, sizeof(book), 1, fs) ==1) {
					    	gotoxy(2, j);
							printf("%s",book.stname);
							gotoxy(18, j);
							printf("%s",book.cat);
							gotoxy(30, j);
							printf("%d",book.id);
							gotoxy(36, j);
							printf("%s",book.name);
							gotoxy(51, j);
							printf("%d-%d-%d",book.issued.day,book.issued.month,book.issued.year);
							gotoxy(65, j);
							printf("%d-%d-%d",book.duedate.day,book.duedate.month,book.duedate.year);							
							gotoxy(50, 25);
							j++;
					    }
					    fclose(fs);
						gotoxy(1,25);
						returnFunc();
			    		break;
			    	}


		case '3'  :
			    	{
			    		system("cls");
						gotoxy(10, 6);
						printf("Enter Book ID:");
						int p, c = 0;
						char another = 'y';
						while(another == 'y') {
							scanf("%d", &p);
							fs=fopen("issue.dat","rb");

							while(fread(&book,sizeof(book), 1, fs) == 1) {
								if(book.id == p) {
									issueRecord();
									gotoxy(10, 12);
									printf("Press any key.......");
									getch();
									issueRecord();
									c = 1;
								}							 
									
							}
							fflush(stdin);
							fclose(fs);
							if(c == 0) {
								gotoxy(10,8);
								printf("No Record Found");
							}
							gotoxy(10,13);
							printf("Try Another Search?(Y/N)");
							another=getch();																				
						}
			    		break;
							
			    	}

		case '4'  :
			    	{
			    		system("cls");
						int b;
						FILE *fg;  //declaration of temporary file for delete
						char another = 'y';
						while(another == 'y') {
							gotoxy(10,5);
							printf("Enter book id to remove:");
							scanf("%d",&b);
							fs=fopen("Issue.dat","rb+");
							while(fread(&book,sizeof(book),1,fs)==1) {
								if(book.id==b) {
									issueRecord();
									findbook='t';
								}
								if(findbook=='t') {
									gotoxy(10,12);
									printf("Do You Want to Remove it?(Y/N)");
									if(getch()=='y')
									{
										fg=fopen("record.dat","wb+");
										rewind(fs);
										while(fread(&book,sizeof(book), 1, fs) == 1)
										{
											if(book.id!=b)
											{
											fseek(fs,0,SEEK_CUR);
											fwrite(&book,sizeof(book),1,fg);
											}
										}
										fclose(fs);
										fclose(fg);
										remove("Issue.dat");
										rename("record.dat","Issue.dat");
										gotoxy(10,14);
										printf("The issued book is removed from list");

								       }
								}

								if (findbook != 't') {
									gotoxy(10,15);
									printf("No Record Found");
								}
							}
						}
						gotoxy(10,16);
						printf("Delete any more?(Y/N)");
						another=getch();
			    	}

		default:		
					gotoxy(10, 18);
					printf("\aWrong Entry!!");
				    getch();
					issueBooks();
					break;
    }
    gotoxy(1,30);
    returnFunc();
}

void viewBooks(void)  //show the list of book persists in library
{
    int i = 0, j;
    system("cls");
    gotoxy(1, 1);
    printf("*********************************Book List*****************************");
    gotoxy(2, 2);
    printf(" CATEGORY     ID    BOOK NAME     AUTHOR       QTY     PRICE     RackNo ");
    j= 4;
    fp=fopen("lib.dat","rb");
    while(fread(&book,sizeof(book),1,fp)==1){
		gotoxy(3,j);
		printf("%s",book.cat);
		gotoxy(16,j);
		printf("%d",book.id);
		gotoxy(22,j);
		printf("%s",book.name);
		gotoxy(36,j);
		printf("%s",book.author);
		gotoxy(50,j);
		printf("%d",book.quantity);
		gotoxy(57,j);
		printf("%.2f",book.price);
		gotoxy(69,j);
		printf("%d",book.rackno);
		printf("\n\n");
		j++;
		i=i+book.quantity;
    }
	gotoxy(3,25);
	printf("Total Books =%d",i);
	fclose(fp);
	gotoxy(35,25);
	returnFunc();
}


void editBooks(void)  //edit information about book
{
	system("cls");
	int c = 0;
	int d, e;
	gotoxy(20, 4);
	printf("****Edit Books Section****");
	char another='y';
	while(another=='y'){
		system("cls");
		gotoxy(15, 6);
		printf("Enter Book Id to be edited:");
		scanf("%d", &d);
		fp=fopen("lib.dat","rb+");
		while(fread(&book,sizeof(book), 1, fp) == 1)
		{
			if(checkId(d)==0)
			{
				gotoxy(15,7);
				printf("The book is availble");
				gotoxy(15,8);
				printf("The Book ID:%d",book.id);
				gotoxy(15,9);
				printf("Enter new name:");scanf("%s",book.name);
				gotoxy(15,10);
				printf("Enter new Author:");scanf("%s",book.author);
				gotoxy(15,11);
				printf("Enter new quantity:");scanf("%d",&book.quantity);
				gotoxy(15,12);
				printf("Enter new price:");scanf("%f",&book.price);
				gotoxy(15,13);
				printf("Enter new rackno:");scanf("%d",&book.rackno);
				gotoxy(15,14);
				printf("The record is modified");
				fseek(fp,ftell(fp)- sizeof(book), 0);
				fwrite(&book, sizeof(book), 1, fp);
				fclose(fp);
				c=1;
			}
			if(c==0)
			{
				gotoxy(15,9);
				printf("No record found");
			}
		}
		gotoxy(15, 16);
		printf("Modify another Record?(Y/N)");
		fflush(stdin);
		another = getch();
	}
		returnFunc();
}

void issueRecord()
{
	 system("cls");
	 gotoxy(10,8);
	 printf("The Book has taken by Mr. %s",book.name);
	 gotoxy(10,9);
	 printf("Issued Date:%d-%d-%d",book.issued.day,book.issued.month,book.issued.year);
	 gotoxy(10,10);
	 printf("Returning Date:%d-%d-%d",book.duedate.day,book.duedate.month,book.duedate.year);
}

/* ========== < UTILS > ==========*/


int getData()
{
	int t;

	// ------------------------ VIEW ---------------------------------
	gotoxy(20,3);printf("Enter the Information Below");
	gotoxy(20,4);printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
	gotoxy(20,5);
	printf("\xB2");gotoxy(46,5);printf("\xB2");
	gotoxy(20,6);
	printf("\xB2");gotoxy(46,6);printf("\xB2");
	gotoxy(20,7);
	printf("\xB2");gotoxy(46,7);printf("\xB2");
	gotoxy(20,8);
	printf("\xB2");gotoxy(46,8);printf("\xB2");
	gotoxy(20,9);
	printf("\xB2");gotoxy(46,9);printf("\xB2");
	gotoxy(20,10);
	printf("\xB2");gotoxy(46,10);printf("\xB2");
	gotoxy(20,11);
	printf("\xB2");gotoxy(46,11);printf("\xB2");
	gotoxy(20,12);
	printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
	gotoxy(21,5);
	printf("Category:");
	gotoxy(31,5);
	printf("%s",categories[s-1]); 
	gotoxy(21,6);
	printf("Book ID:\t");
	// --------------------------------------------------------------
	gotoxy(30,6);
	scanf("%d",&t);

	if (checkId(t) == 0) { // if 0 means book exists
		gotoxy(21, 13);
		printf("Book Name: ");
		gotoxy(33, 7);
		scanf("%s", book.name);

		gotoxy(21, 8);		
		printf("Author: ");		
		gotoxy(30, 8);
		scanf("%s", book.author);
		
		gotoxy(21, 9);
		printf("Quantity:");
		gotoxy(31,9);
		scanf("%d", &book.quantity);

		gotoxy(21,10);
		printf("Price:");
		gotoxy(28,10);
		scanf("%f", &book.price);

		gotoxy(21,11);
		printf("Rack No:");
		gotoxy(30,11);
		scanf("%d", &book.rackno);
		return 1;

	}

}

int checkId(int t) //check whether the book is exist in library or not
{
	rewind(fp);

	while (fread(&book, sizeof(book), 1, fp) == 1) {
		if (book.id == t)
			return 0;
		else
			return 1; // Book don't exists
	}
}


int getTime(void)
{
	time_t t;
	time(&t);
	printf("Date and time: %s\n", ctime(&t));

	return 0;
}


void returnFunc(void)
{
	{
		printf(" Press ENTER to return to main menu");
	}
	a:

	if (getch()== 13)
		mainMenu();
	else 
		goto a;
}

