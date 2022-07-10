/*
@credit: https://docs.microsoft.com/en-us/cpp/cpp/storage-classes-cpp?view=msvc-170

*/

#include <iostream>

using namespace std;


void showStat( int curr ) {
    static int nStatic;  // Value of nStatic is retained between each function call

    nStatic += curr; 
    cout << "nStatic is " << nStatic << endl; 

}

int main()
{
    int times = 5;

    for (int i = 0; i < times; i++) 
        showStat(i);
    
    return 0;
}
