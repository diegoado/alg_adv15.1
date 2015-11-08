/*
 * University Federal of Campina Grande
 * Student: Diego Adolfo Silva de Araújo
 * Registry: 113210090
 * Discipline: Algoritmos Avançados
 *
 * Code forces
 * Problem: 366B - B. Dima and To-do List
 * Time limit per test: 1 second
 * Memory limit per test: 256 megabytes
 * Input: standard input
 * Output: standard output
 */

#include <iostream>
#include <limits>
#include <vector>

using namespace std;

vector<int> tasks;
int min_power = numeric_limits<int>::max();

int main() {
    int n, k;
    cin >> n >> k;
    for(int i=0; i<n; i++)
    {
        int task;
        cin >> task;
        tasks.push_back(task);
    }
    int min_task = 0;
    for(int i=0; i<k; i++)
    {
        int next = i, sum = 0;
        while(next < n)
        {
            sum += tasks[next];
            next += k;
        }
        if(sum < min_power)
        {
            min_power = sum;
            min_task = i + 1;

        }

    }
    cout << min_task << endl;
    return 0;
}