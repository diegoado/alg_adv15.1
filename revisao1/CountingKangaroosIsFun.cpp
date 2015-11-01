/*
 * University Federal of Campina Grande
 * Student: Diego Adolfo Silva de Araújo
 * Registry: 113210090
 * Discipline: Algoritmos Avançados
 *
 * Code forces
 * Problem: 372A - A. Counting Kangaroos is Fun (Div. 1)
 * Time limit per test: 1 second
 * Memory limit per test: 256 megabytes
 * Input: standard input
 * Output: standard output
 */

#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

// Function to hidden the Kangaroos
bool hidden(int array[], int to, int size)
{
    int to_occult = size - to;
    for(int i=0; i<to_occult; i++)
    {
        if(2*array[i] > array[size-to_occult+i])
        {
            return false;
        }
    }
    return true;
}

int main()
{
    int n; // The number of Kangaroos
    cin >> n;

    int kangaroos[n]; // List of all Kangaroos
    for(int i=0; i<n; i++)
    {
        cin >> kangaroos[i];
    }
    // Pointers to mark the indexes of Kangaroos in the list
    int roof = n;
    int floor = ceil(n/2.0);

    sort(kangaroos, kangaroos + n);
    while(floor < roof)
    {
        int mid = (floor + roof) / 2;
        if(hidden(kangaroos, mid, n))
            roof = mid;
        else
            floor = mid + 1;

    }
    cout << roof << endl;
    return 0;
}

