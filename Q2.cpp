#include <iostream>
using namespace std;

int main() {
    int array[6] = {1, 2, 4, 5, 8, 9};
    int target = 7;
    if (target >= array[5]) {
        cout << array[5];
    }
    else {
        int low = 0;
        int high = 6;
        int mid;
        while (low<=high) {
            mid = (low+high)/2;
            if ((array[mid]< target) && (target < array[mid+1])) {
                if (abs(target-array[mid]) > abs(target-array[mid+1])) {
                    cout << array[mid+1];
                }
                else {
                    cout << array[mid];
                }
                break;
            }
            else if ((array[mid-1]< target) && (target < array[mid])) {
                if (abs(target-array[mid-1]) > abs(target-array[mid])) {
                    cout << array[mid];
                }
                else {
                    cout << array[mid-1];
                }
                break;
            }
            else if (array[mid]==target) {
                cout << array[mid];
            }
            else {
                if (target > array[mid]) {
                    low = mid;
                }
                else {
                    high = mid+1;
                }
            }
        }
    }
}