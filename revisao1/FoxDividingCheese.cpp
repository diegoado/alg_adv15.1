/*
 * University Federal of Campina Grande
 * Student: Diego Adolfo Silva de Araújo
 * Registry: 113210090
 * Discipline: Algoritmos Avançados
 *
 * Code forces
 * Problem: 371B - B. Fox Dividing Cheese
 * Time limit per test: 1 second
 * Memory limit per test: 256 megabytes
 * Input: standard input
 * Output: standard output
 */

#include <cmath>
#include <iostream>

using namespace std;

int aux_calc(int &x, int div) {
	int count = 0;
	while(x % div == 0) {
		x /= div;
		count++;
	}
	return count;
}

void calc(int &a, int &b, int &step) {
	step += abs(aux_calc(a, 2) - aux_calc(b, 2)) +
			abs(aux_calc(a, 3) - aux_calc(b, 3)) +
			abs(aux_calc(a, 5) - aux_calc(b, 5));
}

int main() {
	int a, b;
	cin >> a >> b;

	if(a == b)
	{
		cout << 0 << endl;
	} else
	{
		int step = 0;
		calc(a, b, step);
		if(a == b)
		{
			cout << step << endl;
		}
		else
		{
			cout << -1 << endl;
		}
	}
	return 0;
}

