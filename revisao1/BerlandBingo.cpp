/*
 * University Federal of Campina Grande
 * Student: Diego Adolfo Silva de Araújo
 * Registry: 113210090
 * Discipline: Algoritmos Avançados
 *
 * Code forces
 * Problem: 370B - B. Berland Bing
 * Time limit per test: 1 second
 * Memory limit per test: 256 megabytes
 * Input: standard input
 * Output: standard output
 */

#include <iostream>
#include <string.h>

using namespace std;

const int MAX_C = 100;

int main() {
    int n; // The number of the players
    cin >> n;
    int bing[n][MAX_C];
    memset(bing, 0, sizeof(bing));

    for(int i = 0; i < n; i++)
    {
        int numbers;
        cin >> numbers;
        for(int j = 0; j < numbers; j++)
        {
            int number;
            cin >> number;
            bing[i][number-1] = 1;
        }
    }
    for(int i = 0; i < n; i++)
    {
        bool canWin = true;
        for(int j = 0; j < n; j++)
        {
            if(i == j)
                continue;

            int it;
            for(it = 0; it < MAX_C; it++)
            {
                if(bing[i][it] == 0 && bing[j][it] == 1)
                    break;
            }
            if(it == MAX_C)
                canWin = false;
        }
        if(canWin)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}


