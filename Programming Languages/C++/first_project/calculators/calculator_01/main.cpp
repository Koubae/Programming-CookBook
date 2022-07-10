/*

# Build main
/usr/bin/g++-10 -fdiagnostics-color=always -g  -o main.o -c main.cpp -std=c++20
# BUild Calculator .cpp
/usr/bin/g++-10 -fdiagnostics-color=always -g  -o Calculator.o -c Calculator.cpp -std=c++20
# Build Final App
/usr/bin/g++-10 -fdiagnostics-color=always  main.o Calculator.o -o calculator
# Run 
./calculator

# Now all of this in one go
/usr/bin/g++-10 -fdiagnostics-color=always -g -std=c++20 main.cpp Calculator.cpp -o calculator

# Build and run 
/usr/bin/g++-10 -fdiagnostics-color=always -g -std=c++20 main.cpp Calculator.cpp -o calculator && ./calculator

*/
#include <iostream>
// #include "pch.h"
#include "Calculator.h"

using namespace std; 

int main()
{
    // Default vars
    double x = 0.00;
    double y = 0.00; 
    double result = 0.00;
    char oper = '+';


    cout << "Calculator Console Application" << endl << endl;
    cout << "Please enter the operation to perform. Format: a+b | a-b | a*b | a/b" << endl;

    Calculator calculator;

    // Main App Loop 
    while (true) 
    {
        cin >> x >> oper >> y;
        if (oper == '/' && y == 0)
        {
            cout << "Division by 0 exception" << endl;
            continue;
        }
        else if (oper == 'e')
        { 
            break;

        }
        
        else
        {
            result = calculator.Calculate(x, oper, y);
        }
        cout << "Result is: " << result << endl;
        
    }

    cout << "Goodbye :) " << endl;

    return 0;
}