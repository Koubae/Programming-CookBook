#ifndef CALCULATOR_H
#define CALCULATOR_H

#include <string>
#include <array>
#include <cmath>



/**
 * @docs: https://stackoverflow.com/questions/34383516/should-i-default-virtual-destructors
 * @docs: https://stackoverflow.com/questions/827196/virtual-default-destructors-in-c
 * @docs: https://stackoverflow.com/questions/17221668/why-do-we-need-to-use-virtual-a-default-instead-of-virtual-a-in-c1
 */
class Calculator
{



public: 
    Calculator();   /// Constructor
    virtual ~Calculator() = default; /// Virtual destructor to prevent delete errors  @ see https://stackoverflow.com/questions/34383516/should-i-default-virtual-destructors

    // ----------------------
    //  Methods
    // ----------------------

    /// Calculator Methods
    void run(const std::string&); 
    double add();
    void subtract();
    void multiply();
    void divide();
    void square();
    void sqrt();
    void setMem();
    void printMem() const;    


    /// Helpers 

    void printPrompt();
    /// Parse input subs in number value when strings result or mem are entered
    double parseInput(const std::string&) const; 


    double getResult();    
    

private: 
    double result;
    double mem;


};


#endif // CALCULATOR_H