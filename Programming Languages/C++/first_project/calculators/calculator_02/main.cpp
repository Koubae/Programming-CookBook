/**
 * @file main.cpp
 * @author christopher-siewert (https://github.com/christopher-siewert/cpp-calculator)
 * @brief 
 * @version 0.1
 * @date 
 * 
 * 
 * @installation 
 * 
 * /usr/bin/g++-10 -fdiagnostics-color=always -g -std=c++20 main.cpp Calculator.cpp -o calculator && ./calculator
 * 
 * make
 */

#include <iostream>
#include <iomanip>
#include <chrono>
#include <thread>

#include "Calculator.h"


#define EXIST_INPUT "exit"



using namespace std; 


void welcome()
{
    cout << "\n\n====================================== < WELCOME > =====================================\n\n"
    << "Welcome to my Calculator App\n\n"
    << "This calculator has 2 modes, normal and scientific.\n"
    << "You can change it using the 'change' keyword.\n\n"
    << "This app has 2 other special keywords, result and mem.\n"
    << "result stores the result of the previous calculation.\n"
    << "mem allows you to store and access a number.\n"
    << "Both can be used instead of numbers during calculations.\n"
    << "They are both local to the mode you are using.\n\n"
    << "===========================================================================\n\n";
}


/**
 * @brief 
 * 
 * @credit for the sleep method  https://stackoverflow.com/a/10613664/13903942
 * 
 */
void goodbye()
{
    cout << "Press exist botton, Calcualtor shutting down....\n\n";
    this_thread::sleep_for(chrono::milliseconds(500));

    cout << "......\n";
    this_thread::sleep_for(chrono::milliseconds(500));
    cout << ".....\n";
    this_thread::sleep_for(chrono::milliseconds(500));
    cout << "....\n";
    this_thread::sleep_for(chrono::milliseconds(500));
    cout << "...\n";
    this_thread::sleep_for(chrono::milliseconds(500));
    cout << "..\n";
    this_thread::sleep_for(chrono::milliseconds(500));
    cout << ".\n";
    this_thread::sleep_for(chrono::milliseconds(500));
    cout << "Goodbye!\n\n";
    cout << "===========================================================================\n\n";

}


int main()
{

    welcome();

    Calculator calculator;

    Calculator* calculatorPointer = &calculator; // QST?? Why need a pointer?

    calculator.printPrompt();

    /// Shows up to 15 places
    cout << setprecision(15); // todo: move inot the Calculator init


    string input = "";

    while (cin >> input && input != EXIST_INPUT) { // todo make regex

        calculatorPointer->run(input);
        std::cout << "The result is " << calculatorPointer->getResult();
        calculator.printPrompt();

    }


    goodbye();
    return 0;
}