/*
 * University Federal of Campina Grande
 * Student: Diego Adolfo Silva de Araújo
 * Registry: 113210090
 * Discipline: Algoritmos Avançados
 *
 * Code forces
 * Problem: 369C - C. Valera and Elections
 * Time limit per test: 1 second
 * Memory limit per test: 256 megabytes
 * Input: standard input
 * Output: standard output
 */

#include <iostream>
#include <cstring>
#include <vector>

#define MAX_N 100001

using namespace std;

int n, rnt;
int vis[MAX_N], subset[MAX_N];

vector<int> adj[MAX_N];

int dfs(int i, int flag)
{
    int j, s = 0;
    vis[i] = 1;
    for(j = 0; j < adj[i].size(); j += 2)
    {
        if(vis[adj[i][j]])
            continue;
        if(adj[i][j + 1] == 2)
            s += dfs(adj[i][j], 1);
        else
            s += dfs(adj[i][j], 0);
    }
    if(flag && !s)
    {
        subset[rnt++] = i;
        return 1;
    }
    return s;
}

int main()
{
    rnt = 0;
    int a, b, t;

    cin >> n;

    memset(vis, 0, sizeof(vis));
    memset(subset, 0, sizeof(subset));
    for(int i = 1; i <= n; i++)
        adj[i].clear();
    for(int i = 0; i < n - 1; i++)
    {
        cin >> a >> b >> t;

        adj[a].push_back(b);
        adj[a].push_back(t);
        adj[b].push_back(a);
        adj[b].push_back(t);
    }

    dfs(1, 0);
    cout << rnt << endl;

    for(int i = 0; i < rnt; i++)
    {
        cout << subset[i] << " ";
    }
    cout << endl;
    return 0;
}