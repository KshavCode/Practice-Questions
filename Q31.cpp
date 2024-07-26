#include <iostream>
#include <fstream>
using namespace std;


int main() {
    string a;
    ifstream read("Q31read.txt");
    ofstream write("Q31write.txt");
    getline(read, a);
    for (int i=0; i<a.length(); i++) {
        if (a[i] != ' ') {
            write << a[i];
        }
    }
    cout << "Done!";
}