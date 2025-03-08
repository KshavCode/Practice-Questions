#include <iostream>
using namespace std;

int main() {
    string str = "zxvczbtxyzvy"; 
    int alphabets[26] = {0};
    int order[26];
    int j = 0;
    for (char x: str) {
        alphabets[x-'a'] += 1;
        order[j] = int(x-'a');
        j++;
    }
    for (int i=0; i<26; i++) {
        if (alphabets[order[i]] == 1) {
            cout << char(order[i]+'a') << endl;
            break;
        }
    }
}