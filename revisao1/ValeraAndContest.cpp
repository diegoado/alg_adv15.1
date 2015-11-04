/*
 * University Federal of Campina Grande
 * Student: Diego Adolfo Silva de Araújo
 * Registry: 113210090
 * Discipline: Algoritmos Avançados
 *
 * Code forces
 * Problem: 369B - B. Valera and Contest
 * Time limit per test: 1 second
 * Memory limit per test: 256 megabytes
 * Input: standard input
 * Output: standard output
 */


#include <iostream>

using namespace std;

/**
 * Number n is the total of students in the team
 * Number k is the total of members in the team that scored the most points
 * Number l is the minimum points scored each member in the team
 * Number r is the maximum points scored each member in the team
 * Number total is all points scored of a team
 * Number most is equal to exactly the k members of the team that scored the maximum points
 */

int n, k, l, r;
long total, most;

int main() {
    cin >> n >> k >> l >> r >> total >> most;

    int points[n];
    int average = most / k, mod = most % k;

    for(int i = 0; i < k; i++)
    {
        points[i] = average;
        if(i < mod)
            points[i]++;
    }
    if(total - most)
    {
        average = (total-most) / (n-k), mod = (total-most) % (n-k);
        for(int i = k; i < n; i++)
        {
            points[i] = average;
            if(i-k < mod)
                points[i]++;
        }
    }
    for(int i = 0; i < n; i++)
    {
        cout << points[i] << " ";
    }
    cout << endl;
    return 0;
}