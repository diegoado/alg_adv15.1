/*
 * University Federal of Campina Grande
 * Student: Diego Adolfo Silva de Araújo
 * Registry: 113210090
 * Discipline: Algoritmos Avançados
 *
 * Code forces
 * Problem: 366C - C. Dima and Salad
 * Time limit per test: 1 second
 * Memory limit per test: 256 megabytes
 * Input: standard input
 * Output: standard output
 */

#include <iostream>
#include <cstring>

using namespace std;

int main() {

    /* Number n is the total of fruits in the fridge
     * Number k is the total caloric ratio of chosen fruits
     */
    int n, k;
    cin >> n >> k;

    /* A is list with the fruits' tastes
     * B is list whit the fruits' calories
     */
    int a[n+1], b[n+1];

    int sum = 0;
    for(int i=1; i<=n; i++)
    {
        cin >> a[i];
        sum += a[i];
    }
    for(int i=1; i<=n; i++)
    {
        cin >> b[i];
        b[i] = b[i] * k;
    }

    int dynamic[n+1][2*sum+1];
    memset(dynamic, -1, sizeof(dynamic));

    dynamic[0][sum] = 0;
    for(int i=1; i<=n; i++)
    {
        int balance = a[i] - b[i];
        for(int j=0; j<=2*sum; j++)
        {
            dynamic[i][j] = max(dynamic[i][j], dynamic[i-1][j]);
            if(j+balance >= 0 && j+balance <= 2*sum && dynamic[i-1][j] != -1)
                dynamic[i][j+balance] = max(dynamic[i][j+balance], dynamic[i-1][j] + a[i]);
        }
    }

    if(dynamic[n][sum] == 0)
    {
        cout << -1 << endl;
    }
    else
    {
        cout << dynamic[n][sum] << endl;
    }
    return 0;
}