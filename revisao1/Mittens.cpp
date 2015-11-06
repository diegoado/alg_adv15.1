/*
 * University Federal of Campina Grande
 * Student: Diego Adolfo Silva de Araújo
 * Registry: 113210090
 * Discipline: Algoritmos Avançados
 *
 * Code forces
 * Problem: 372C - C. Mittens
 * Time limit per test: 1 second
 * Memory limit per test: 256 megabytes
 * Input: standard input
 * Output: standard output
 */


#include<iostream>
#include<algorithm>

using namespace std;

int colors[5000];

int main()
{
    int n, m;
    cin >> n >> m;
    for(int i = 0; i < n; i++)
    {
        cin >> colors[i];
    }

    int cnt = 0;
    sort(colors, colors + n);
    for (int i = 0; i < n; i++)
    {
        cnt += (colors[i] != colors[(i + n/2) % n]);
    }

    cout << cnt << endl;
    for (int i = 0; i < n; i++)
    {
        cout << colors[i] << ' ' << colors[(i + n/2) % n] << endl;
    }
    return 0;
}