#include <bits/stdc++.h>
#include <string.h>
using namespace std;

bool check(string a)
{
	int i = 0;
	while (a[i] != '\0')
	{
		if ((a[i] == 32) || (a[i] >= 65 && a[i] <= 90) || (a[i] >= 97 && a[i] <= 122))
		{
			i++;
			continue;
		}
		else
			return false;
	}
	return true;
}

void encrypt(char mat[][100], string a, int &l, int key, int row)
{
	int count = 0;
	l = 0;
	char c = 66;
	int i, j;
	for (i = 0; i < row; i++)
	{
		for (j = 0; j < key; j++)
		{
			if (count >= a.length())
				mat[i][j] = c++;
			else if (a[count] == ' ')
			{
				count++;
				j--;
				continue;
			}
			else
			{
				mat[i][j] = a[count];
				l++;
			}

			count++;
		}
	}
	cout << "\nEncrypted message : ";
	for (int i = 0; i < key; i++)
	{
		for (int j = 0; j < row; j++)
		{
			cout << mat[j][i];
		}
	}
	cout << endl;
}

void decrypt(char mat[][100], int l, int row, int key)
{
	int count = 0;
	string b;
	for (int i = 0; i < row; i++)
	{
		for (int j = 0; j < key; j++)
		{
			if (count >= l)
			{
				break;
			}
			else
			{
				b.push_back(mat[i][j]);
			}
			if (count >= l)
			{
				break;
			}
			count++;
		}
	}
	cout << "\nDecrypted message : " << b << endl;
}

int main()
{
	string a, b;
	int key, row;
	char mat[100][100];

	while (1)
	{
		int n, count, l;
		char c;

		cout << "\n1. Enter the Message" << endl;
		cout << "2. Encrypting" << endl;
		cout << "3. Decrypting" << endl;
		cout << "4. Exit" << endl;
		cout << "Enter you choice : ";
		cin >> n;

		switch (n)
		{
		case 1:
			cout << "\nEnter key and msg : ";
			cin >> key;
			cin.get();
			getline(cin, a);
			if (check(a))
			{
				cout << a << endl;
				if (a.length() % key == 0)
					row = a.length() / key;
				else
					row = (a.length() / key + 1);
				mat[row][key];
			}
			else
			{
				cout << "Invalid Input" << endl;
			}
			break;

		case 2:
			encrypt(mat, a, l, key, row);
			break;

		case 3:
			decrypt(mat, l, row, key);
			break;

		case 4:
			exit(0);
			break;

		default:
			cout << "Invalid Input" << endl;
		}
	}
}
