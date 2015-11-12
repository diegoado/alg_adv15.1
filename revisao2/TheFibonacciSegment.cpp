/*
 * University Federal of Campina Grande
 * Student: Diego Adolfo Silva de Araújo
 * Registry: 113210090
 * Discipline: Algoritmos Avançados
 *
 * Code forces
 * Problem: 365B - B. The Fibonacci Segment
 * Time limit per test: 1 second
 * Memory limit per test: 256 megabytes
 * Input: standard input
 * Output: standard output
 */

#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    int segment[n];
    for(int i=0; i<n; i++)
    {
        cin >> segment[i];
    }

    if(n == 1)
    {
        cout << 1 << endl;
    }
    else if (n == 2)
    {
        cout << 2 << endl;
    }
    else
    {
        int curLen = 2, maxLen = curLen;
        for(int i=2; i<n; i++)
        {
            if(segment[i] == segment[i-1] + segment[i-2])
            {
                curLen++;
            }
            else
            {
                if(maxLen < curLen)
                {
                    maxLen = curLen;
                }
                curLen = 2;
            }
        }
        if(maxLen < curLen)
        {
            maxLen = curLen;
        }
        cout << maxLen << endl;
    }
    return 0;
}
