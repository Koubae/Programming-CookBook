#pragma once 

class CardGame
{
    int players;
    static int totalPartecipants;


public: 
    CardGame(int players);
    ~CardGame();

    static int getParticipants() { return totalPartecipants; }


};