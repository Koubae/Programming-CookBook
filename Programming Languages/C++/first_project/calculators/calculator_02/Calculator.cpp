#include <iostream>
#include <vector>
#include <algorithm>

#include "Calculator.h"


// Initialize the calculator with some default values
Calculator::Calculator() : result(0.0), mem(0.0) {} // todo: improve, there isn't a better way???


/**
 * @brief Check if value in a vector
 * 
 * @credit: https://stackoverflow.com/a/20303915/13903942
 * 
 * @param value 
 * @param array 
 * @return true 
 * @return false 
 */
bool inArray(const std::string &value, const std::vector<std::string> &array) 
{
    return std::find(array.begin(), array.end(), value) != array.end();
}

// ----------------------
//  Methods
// ----------------------

/// Calculator Methods
void Calculator::run(const std::string& input)
{
    // -------------------
    // CONSTANTS   TODO: Check how to do it properly in c++
    // -------------------
    const std::vector<std::string> INPUTS_ADD{ "+", "add", "addition", "sum"};
    const std::vector<std::string> INPUTS_SUBTRACT{"-", "sub", "subtraction", "minus"};
    const std::vector<std::string> INPUTS_DIVIDE{"/", "divide", "div"};
    const std::vector<std::string> INPUTS_MULTIPLY{"*", "mul", "multiply", "times"};
    const std::vector<std::string> INPUTS_SQRT{"sqrt"};
    const std::vector<std::string> INPUTS_SETMEM{"setmem"};
    const std::vector<std::string> INPUTS_PRINTMEM{"printmem"};


    if (inArray(input, INPUTS_ADD))
    {
        result = add();
    }
    else if (inArray(input, INPUTS_SUBTRACT))
    {
        subtract();
    }
    else if (inArray(input, INPUTS_SUBTRACT))
    {
        divide();
    }
    else if (inArray(input, INPUTS_DIVIDE))
    {
        multiply();
    }
    else if (inArray(input, INPUTS_MULTIPLY))
    {
        sqrt();
    }
    else if (inArray(input, INPUTS_SQRT))
    {
        square();
    }
    else if (inArray(input, INPUTS_SETMEM))
    {
        setMem();
    }
    else if (inArray(input, INPUTS_PRINTMEM))
    {
        printMem();
    } 
    else 
    {
        std::cout << "Invalid Input\n";
    }
}

double Calculator::add()
{
    std::string x;
    std::string y;

    std::cout << "$ ";
    std::cin >> x;
    std::cout << "+ \n";
    std::cin >> y;

    result = parseInput(x) + parseInput(y);
    return result;

}
void Calculator::subtract()
{
    std::string x;
    std::string y;
    std::cout << "subtract\n";
}

void Calculator::multiply()
{
    std::string x;
    std::string y;
    std::cout << "multiply\n";
}

void Calculator::divide()
{
    std::string x;
    std::string y;
    std::cout << "divide\n";
}

void Calculator::square()
{
    std::string x;
    std::string y;
    std::cout << "square\n";
}

void Calculator::sqrt()
{
    std::string x;
    std::string y;
    std::cout << "sqrt\n";
}

void Calculator::setMem()
{
    std::string x;
    std::string y;
    std::cout << "setMem\n";
}

void Calculator::printMem() const
{
    std::string x;
    std::string y;
    std::cout << "TprintMemODO" << std::endl;
}


/// Helpers 
void Calculator::printPrompt()
{
    std::cout << "\n\nEnter an operation (+, -, /, *, sqrt, square, change, setmem, printmem) or exit\n"
        << ">>> ";
}


/// subs in number value when strings result or mem are entered
double Calculator::parseInput(const std::string& input) const
{
    if (input == "result")
    {
        return result;
    }
    else if (input == "mem")
    {
        return mem;
    }
    else
    {
        return std::stod(input);
    }
}


double Calculator::getResult()
{
    return result;
}