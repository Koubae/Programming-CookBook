#include <iostream>
#include <vector>
#include <algorithm>

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


int main()
{

    const std::vector<std::string> INPUTS_ADD{ "+", "add", "addition", "sum"};

    if (inArray("add", INPUTS_ADD))
    {
        std::cout << "OOK OK OK" << std::endl;
    }
    return 0;
}