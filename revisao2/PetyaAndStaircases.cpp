/*
 * University Federal of Campina Grande
 * Student: Diego Adolfo Silva de Araújo
 * Registry: 113210090
 * Discipline: Algoritmos Avançados
 *
 * Code forces
 * Problem: 362B - B. Petya and Staircases
 * Time limit per test: 1 second
 * Memory limit per test: 256 megabytes
 * Input: standard input
 * Output: standard output
 */

#include <algorithm>
#include <iostream>

using namespace std;

int main() {
    int m;
    unsigned long n;

    cin >> n >> m;

    long stair;
    vector<long> dirties;

    for(int i=0; i<m; i++)
    {
        cin >> stair;
        dirties.push_back(stair);
    }

    bool isPossible = true;
    sort(dirties.begin(), dirties.end());
    if(m == 0)
    {
    }
    else if(dirties.front() == 1 || dirties.back() == n)
    {
        isPossible = false;
    }
    else
    {
        long last = -1, count = 0;
        for(int i=0; i<m; i++)
        {
            if(dirties[i] - 1 == last)
            {
                count++;
                last = dirties[i];
            }
            else
            {
                count = 0;
                last = dirties[i];
            }
            if(count > 1)
            {
                isPossible = false;
                break;
            }
        }
    }

    if(isPossible)
    {
        cout << "YES" << endl;
    } else
    {
        cout << "NO" << endl;
    }
    return 0;
}
