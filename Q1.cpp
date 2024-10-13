#include <iostream>
using namespace std;

int main() {
    int k = 10;
    int array[k] = {1, 1, 0, 0, 1, 0, 1, 1, 1, 1};
    int c = 0, highest = 0;
    for (int i=0; i<k; i++) {
        if (array[i]==1) {
            c += 1;
            if (c>highest) {
                highest = c;
            }
        }
        else {c = 0;}
    }
    cout << highest;
}