/*
@credit: https://docs.microsoft.com/en-us/cpp/cpp/storage-classes-cpp?view=msvc-170

*/
#include <iostream>

using namespace std; 

// Define class

class CMyClass {

public: 
    static int m_i; 
};


// Initialize and cunsume the class
int CMyClass::m_i = 0;

CMyClass obj1; 
CMyClass obj2; 

int main() {    

    cout << obj1.m_i << endl;
    cout << obj2.m_i << endl;

    obj1.m_i = 1;
    cout << obj1.m_i << endl;
    cout << obj2.m_i << endl;

    obj2.m_i = 2;
    cout << obj1.m_i << endl;
    cout << obj2.m_i << endl;

    CMyClass::m_i = 3;
    cout << obj1.m_i << endl;
    cout << obj2.m_i << endl;
    

    return 0;
}
/*
Output: 


0
0
1
1
2
2
3
3

*/