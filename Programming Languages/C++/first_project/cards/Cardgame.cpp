#include <iostream>
#include "Cardgame.h"


using namespace std; 

// Set CardGame Default values
int CardGame::totalPartecipants = 0;

// Constructor
CardGame::CardGame(int players) : players(players)  // initialization list. https://stackoverflow.com/questions/2785612/c-what-does-the-colon-after-a-constructor-mean
{
    totalPartecipants += players; 
    cout << players << " players have started a new game.  There are now "
        << totalPartecipants << " players in total." << endl;
}

// Deconstructor
CardGame::~CardGame()
{

}