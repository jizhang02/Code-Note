#ifndef LIBHELPER_C
#define LIBHELPER_C

#include "libhelper.h"

#include <stdio.h>


// Binary search function to find the index where 'x' should be inserted in the sorted array 'arr'
int searchSorted(float arr[], int n, float x) {
    int left = 0;
    int right = n;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] < x) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
}


#endif