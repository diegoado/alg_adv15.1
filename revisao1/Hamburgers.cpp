/*
 * University Federal of Campina Grande
 * Student: Diego Adolfo Silva de Araújo
 * Registry: 113210090
 * Discipline: Algoritmos Avançados
 *
 * Code forces
 * Problem: 371C - C. Hamburgers
 * Time limit per test: 1 second
 * Memory limit per test: 256 megabytes
 * Input: standard input
 * Output: standard output
 */

#include <iostream>

using namespace std;

int main() {
    string recipe;
    long long rubles;
    int bread, sausage, cheese;
    int p_bread, p_sausage, p_cheese;

    cin >> recipe;
    cin >> bread >> sausage >> cheese;
    cin >> p_bread >> p_sausage >> p_cheese;
    cin >> rubles;

    int countB = 0, countC = 0, countS = 0;
    for(int i=0; i<recipe.size(); i++)
    {
        if(recipe[i] == 'B')
            countB++;
        else if(recipe[i] == 'C')
            countC++;
        else
            countS++;
    }

    long long min = 0, max = 1e13;

    while(min + 1 < max)
    {
        long long mid = (min + max) / 2;

        long long costB = p_bread * ((countB * mid > bread) ? (countB * mid - bread) : 0);
        long long costC = p_cheese * ((countC * mid > cheese) ? (countC * mid - cheese) : 0);
        long long costS = p_sausage * ((countS * mid > sausage) ? (countS * mid - sausage) : 0);
        long long cost = costB + costC + costS;

        if(cost <= rubles)
            min = mid;
        else
            max = mid;
    }
    cout << min << endl;
    return 0;
}