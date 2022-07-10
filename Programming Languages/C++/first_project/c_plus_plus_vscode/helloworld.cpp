/*
@source: https://code.visualstudio.com/docs/cpp/config-linux

*/

#include <iostream> 
#include <vector>
#include <string>

using namespace std;

int main()
{
    vector<string> msg {"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};

    for (const string& word : msg)
    {
        cout << word << " \n";
    }
    cout << endl;
    cout << "----------------------------- " << endl;
}