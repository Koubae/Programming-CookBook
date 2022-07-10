#include <iostream>
#include "Cardgame.h"


using namespace std; 

// Set CardGame Default values
int CardGame::totalPartecipants = 0;

// Constructor
CardGame::CardGame(int players) : players(players)
{
    totalPartecipants += players; 
    cout << players << " players have started a new game.  There are now "
        << totalPartecipants << " players in total." << endl;
}

// Deconstructor
CardGame::~CardGame()
{

}