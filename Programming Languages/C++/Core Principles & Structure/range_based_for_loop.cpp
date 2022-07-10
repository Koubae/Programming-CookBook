/*
@source https://docs.microsoft.com/en-us/cpp/cpp/welcome-back-to-cpp-modern-cpp?view=msvc-170#range-based-for-loops
*/

#include <iostream>
#include <vector>

int main()
{
    std::vector<int> vector {1, 2, 3};

    std::cout << "----------------- <  C-Style > -----------------" << std::endl;
    // C-Style
    for (int i = 0; i < vector.size(); i++) {
        std::cout << vector[i] << std::endl;
    }

    std::cout << "----------------- <  Modern C++ > -----------------" << std::endl;

    // Modern C++
    for (auto& value : vector) {
        std::cout << value << std::endl;
    }


    return 0;
}