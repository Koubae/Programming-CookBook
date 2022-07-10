/*
@source: https://docs.microsoft.com/en-us/cpp/ide/walkthrough-working-with-projects-and-solutions-cpp?view=msvc-170

# Build and run 

/usr/bin/g++-10 -fdiagnostics-color=always -g -std=c++20 main.cpp Cardgame.cpp -o cards && ./cards
   


*/

#include <iostream>
#include "Cardgame.h"

using namespace std; 


void Play()
{
    CardGame bridge(4);
    CardGame blackjack(8);
    CardGame solitaire(1);
    CardGame poker(5);
}

int main()
{
    Play();
    return 0;
}