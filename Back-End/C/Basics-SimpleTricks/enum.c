// SYNTAX
// enum flag {const1, const2, ..., constN};

// Changing default values of enum constants
enum suit {
    club = 0,
    diamonds = 10,
    hearts = 20,
    spades = 3,
};

// Enumerated Type Declaration
enum boolean {false, true};
enum boolean check; // declaring an enum variable
// Variation 
enum boolean {false, true} check;

// Example: Enumeration Type
#include <stdio.h>

enum week {Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday};

int main()
{
    // creating today variable of enum week type
    enum week today;
    today = Wednesday;
    printf("Day %d",today+1);
    return 0;
}

// Other Example
#include <stdio.h>

enum suit {
    club = 0,
    diamonds = 10,
    hearts = 20,
    spades = 3
} card;

int main() 
{
    card = club;
	printf("Size of enum variable = %d bytes", sizeof(card));	
	return 0;
}


// ======= < FLAGS > ======= \\

#include <stdio.h>

enum designFlags {
	BOLD = 1,
	ITALICS = 2,
	UNDERLINE = 4
};

int main() {
	int myDesign = BOLD | UNDERLINE; 

        //    00000001
        //  | 00000100
        //  ___________
        //    00000101

	printf("%d", myDesign);

	return 0;
}


// ======= < switch-case statements > =======//

enum weather {
    sunny,
    windy,
    cloudy,
    rain,
} weather_outside;

// ...


void myFunc(void) 
{
    
        switch (weather_outside) {
    case sunny:
        wear_sunglasses();
        break;
    case windy:
        wear_windbreaker();
        break;
    case cloudy:
        get_umbrella();
        break;
    case rain:
        get_umbrella();
        wear_raincoat();
        break;
    }
}
