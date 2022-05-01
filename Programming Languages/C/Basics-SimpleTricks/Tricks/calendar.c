#include <stdio.h>
#include <conio.h>
#include <windows.h>

// ============= STRUCTS ================== //

struct Date 
{
	int day;
	int month;
	int year;
};
struct Date date;

struct Remainder{
    int day;
    int month;
    char note[50];
};
struct Remainder R;


// ================== < CONSOLE > ================== //

COORD xy = {0, 0};

void gotoxy(int x, int y)
{
	xy.X = x; xy.Y = y;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), xy);
}


void InitConsole(int ForgC, int BackC)
{
	WORD wColor = ((BackC & 0x0F) << 4) + (ForgC & 0x0F);
	HANDLE handleConsole = GetStdHandle(STD_OUTPUT_HANDLE); /* Handle to current output buffer*/
	COORD coord = {0, 0};  /*Cursor to top-left*/
	DWORD count;

	CONSOLE_SCREEN_BUFFER_INFO consoleBuffer;  /*Console info- find size of console*/

	SetConsoleTextAttribute(handleConsole, wColor);  /*Set the current color*/

	if(GetConsoleScreenBufferInfo(handleConsole, &consoleBuffer)) {
		FillConsoleOutputCharacter(handleConsole, (TCHAR) 32, consoleBuffer.dwSize.X * consoleBuffer.dwSize.Y, coord, &count); /*Fills Bugger with given char (32 spaces)*/

		FillConsoleOutputAttribute(handleConsole, consoleBuffer.wAttributes, consoleBuffer.dwSize.X * consoleBuffer.dwSize.Y, coord, &count ); /* fill background*/
		SetConsoleCursorPosition(handleConsole, coord);  /*Set Cursor position to next print statement*/
	}
	return;
}

void setColorAndBackground(int ForgC, int BackC)
{
	WORD wColor = ((BackC & 0x0F) << 4 ) + (ForgC & 0x0F);
	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), wColor);
	return;
}

void setColor(int ForgC) /* forground color for printing in a console window. */
{
	WORD wColor;

	HANDLE handleConsole = GetStdHandle(STD_OUTPUT_HANDLE);
	CONSOLE_SCREEN_BUFFER_INFO consoleBuffer;

	if (GetConsoleScreenBufferInfo(handleConsole, &consoleBuffer)) {
		//Mask out all but the background attribute, and add in the forgournd color
    	wColor = (consoleBuffer.wAttributes & 0xF0) + (ForgC & 0x0F);
      	SetConsoleTextAttribute(handleConsole, wColor);  
	}
	return;
}

void clearColor()
{
	setColor(15);
}


// ============= CALENDAR FUNCTIONS ================== //

char *getName(int day) //returns the name of the day
{
	switch(day) {
		case 0 : return("Sunday");
		case 1 : return("Monday");
		case 2 : return("Tuesday");
		case 3 : return("Wednesday");
		case 4 : return("Thursday");
		case 5 : return("Friday");
		case 6 : return("Saturday");
		default : return("Error in getName() module.Invalid argument passed");
	}
}

void printDate(int month, int year)
{
	printf("---------------------------\n");
    gotoxy(25,6);
    switch(month){
        case 1  : printf("January"); break;
        case 2  : printf("February"); break;
        case 3  : printf("March"); break;
        case 4  : printf("April"); break;
        case 5  : printf("May"); break;
        case 6  : printf("June"); break;
        case 7  : printf("July"); break;
        case 8  : printf("August"); break;
        case 9  : printf("September"); break;
        case 10 : printf("October"); break;
        case 11 : printf("November"); break;
        case 12 : printf("December"); break;
    }
    printf(" , %d", year);
    gotoxy(20, 7);
    printf("---------------------------");
}

int checkLeapYear(int year)
{
	if (year % 400 == 0 || (year % 100!=0 && year % 4 == 0))
		return 1;
	return 0;
}

void increaseMonth(int *month, int *year) /* NOTE: Increase month by 1 */
{
	++*month;
	if (*month > 12) {		
		++*year; /* Increase Year every 12 months */
		*month = *month - 12; /* Set Month counter back to 1;*/
	} 
}


void decreaseMonth(int *month, int *year) /* NOTE: Decrease month by 1 */
{
	--*month; 
	if (*month < 1) {
		--*year; /* Decrease year */
		if (*year < 1600) {
			printf("No Record available for the previous years");
			return;
		}
		*month = *month +12; /* Set counter back to 12 */
	}
}

int getNumberOfDays(int month, int year) 
{
	switch(month){
		case 1 : return(31);
		case 2 : 
			if(checkLeapYear(year)==1)
				return(29);
			else
				return(28);
		case 3 : return(31);
		case 4 : return(30);
		case 5 : return(31);
		case 6 : return(30);
		case 7 : return(31);
		case 8 : return(31);
		case 9 : return(30);
		case 10: return(31);
		case 11: return(30);
		case 12: return(31);
		default: return(-1);
	}
}


int getDayNumber(int day,int mon,int year){ //retuns the day number
    int result = 0, t1, t2, y = year;
    year = year - 1600;

    while(year >= 100){
        result = result + 5;
        year = year - 100;
    }

    result = (result % 7);
    t1 = ((year - 1) / 4);
    t2 = (year-1)-t1;
    t1 = (t1*2)+t2;
    t1 = (t1%7);

    result = result + t1;
    result = result%7;

    t2 = 0;
    for(t1 = 1;t1 < mon; t1++){
        t2 += getNumberOfDays(t1,y);
    }

    t2 = t2 + day;
    t2 = t2 % 7;

    result = result + t2;
    result = result % 7;

    if(y > 2000)
        result = result + 1;
    result = result % 7;

    return result;
}

char *getDay(int day, int month, int year)
{
	int day_;
	if (!(month >= 1 && month <= 12)) 
		return("Invalid month value");
	if (!(day >= 1 && day <=getNumberOfDays(month, year)))
		return ("Invalid date");
	if (year >= 1600) {
		day_ = getDayNumber(day, month, year);
		day_ = day_ % 7;
		return (getName(day_));
	} 
	else 
		return("Please enter year higher than 1600");
}

int checkNote(int day, int month)
{
	FILE *fp;
	fp = fopen("note.dat", "rb");

	if (fp == NULL) 
		printf("Error in Opening the file...");

	while (fread(&R, sizeof(R), 1, fp) == 1) {
		if (R.day == day && R.month == month) {
			fclose(fp);
			return 1;
		}
	}
	fclose(fp);
	return 0;
}

void printMonth(int month, int year, int x, int y)
{
	int nod, day, cnt, d = 1, x1 = x, y1 = y, isNote = 0;

	// Validations check
	if (!(month >= 1 && month <=12)) {
		printf("INVALID MONTH");
		getch();
		return;
	}
	if (!(year >= 1600)) {
		printf("INVALID YEAR");
		getch();
		return;
	}
	// -----------------------------------------

	gotoxy(20, y);
	printDate(month, year);

	y += 3;
	gotoxy(x, y);
	printf("S   M   T   W   T   F   S   ");
	y++;

	nod = getNumberOfDays(month, year);
	day = getDayNumber(d, month, year);

	switch(day) { //locates the starting day in calender
		case 0 :
            x=x;
            cnt=1;
            break;
        case 1 :
            x=x+4;
            cnt=2;
            break;
        case 2 :
            x=x+8;
            cnt=3;
            break;
        case 3 :
            x=x+12;
            cnt=4;
            break;
        case 4 :
            x=x+16;
            cnt=5;
            break;
        case 5 :
            x=x+20;
            cnt=6;
            break;
        case 6 :
            x=x+24;
            cnt=7;
            break;
        default :
            printf("INVALID DATA FROM THE getOddNumber()MODULE");
            return;
	}
	gotoxy(x, y);

	if (cnt== 1)
		setColor(12);
	if (checkNote(d, month) == 1)
		setColorAndBackground(15, 12);

	printf("%02d",d);
	setColorAndBackground(15,1);

	for (d=2; d<nod; d++) {
		if (cnt % 7== 0) {
			y++;
			cnt = 0;
			x = x1 - 4;
		}

		x = x+4;
		cnt++;
		gotoxy(x, y);

		if (cnt == 1)
			setColor(12);
		else 
			clearColor();

		if (checkNote(d, month) == 1)
			setColorAndBackground(15, 12);

		printf("%02d",d);
        setColorAndBackground(15,1);
	}
	gotoxy(8, y+2);
    setColor(14);
    printf("Press 'n'  to Next, Press 'p' to Previous and 'q' to Quit");
    gotoxy(8,y+3);
    printf("Red Background indicates the NOTE, Press 's' to see note: ");
    clearColor();
}



	
// ================== < NOTES > ================== //

void addNote()
{
	FILE *fp;
	fp = fopen("note.dat", "ab+");
	system("cls");

	gotoxy(5, 7);
	printf("Enter the Date(DD/MM): "); 
	scanf("%d%d", &R.day, &R.month);
	gotoxy(5, 8);
	printf("Enter the Note (50 charactes max): ");
	fflush(stdin);
	scanf("%[^\n]", R.note);

	if (fwrite(&R, sizeof(R), 1, fp)) {
		gotoxy(5, 12);
		puts("Note is saved sucessfully!");
		fclose(fp);
	}
	else {
		gotoxy(5, 12);
		setColor(12);
		puts("\aFail to save :(\a");
		clearColor();
	}

	gotoxy(5, 15);
	printf("Press any key............");
    getch();
    fclose(fp);
}


void showNote(int month) 
{
	FILE *fp;
	int i = 0, is_found = 0;
	system("cls");

	fp = fopen("note.dat", "rb");

	if (fp == NULL)
		printf("Error in openinf the file");

	while (fread(&R, sizeof(R), 1, fp) == 1) {
		if (R.month == month) {
			gotoxy(10, 5+i);
			printf("Note %d Day = %d: %s", i+1, R.day, R.note);
			is_found = 1;
			i++;
		}
	}

	if (is_found == 0) {
		gotoxy(10, 5);
		printf("This Month you don't have any notes yet");
	}
	gotoxy(10, 7+i);
	printf("Press any key to go back");
	getch();
}

// ================== < MAIN > ================== //



int main() 
{
	InitConsole(15, 1);
	SetConsoleTitle("Calender Project Mini Desktop App"); 
	int choice;
	char key_press = "a";
	char ch = 'a';
	while(1){

		system("cls"); /*clean screen*/
		printf("1. Get day of the week by given date.\n");
		printf("2. Get Calendar of month by given month.\n");
		printf("3. Add a Note to a date.\n");
		printf("4. EXIT THE PROGRAMM.\n\n");
		printf("\tENTER A CHOICE : ");
		scanf("%d", &choice);
		system("cls");

		// User inputs
		switch(choice){
			case 1:
				printf("Enter date (DD MM YYYY) : ");
				scanf("%d %d %d", &date.day, &date.month, &date.year);
				printf("\nDay is : %s", getDay(date.day, date.month, date.year));
				printf("\nPress any key to continue....");
				getch();
				break;

			case 2:
				printf("Enter month and year (MM YYYY) : ");
                scanf("%d %d",&date.month,&date.year); 
                system("cls");

                while (ch != 'q') {
                	printMonth(date.month, date.year, 20, 5);
                	ch = getch();

                	if (ch == 'n') {
                		increaseMonth(&date.month, &date.year);
                		system("cls");
                		printMonth(date.month, date.year, 20, 5);
                	}
                	else if (ch == 'p') {
                		decreaseMonth(&date.month, &date.year);
                		system("cls");
                		printMonth(date.month, date.year, 20, 5);
                	}
                	else if (ch == 's') {
                		showNote(date.month);
                		system("cls");
                	}
                }
				break;

			case 3:
				addNote();
				break;

			case 4:
				exit(0);
			default:
				system("cls");
				getch();
				break;
		}
	}

	return 0;

}
