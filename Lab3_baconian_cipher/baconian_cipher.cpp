#include <bits/stdc++.h>
#include <string.h>
using namespace std;

void binary(int n, int bin[])
{
  int count = 4;
  int ans = 0;
  int e = 1;
  while (n)
  {
    int rem = n % 2;
    bin[count] = rem;
    count--;
    n /= 2;
  }
}

void encrypt(string a, string &en)
{
  int arr[20];
  int count = 0;
  for (int i = 0; i < a.length(); i++)
  {
    if (a[i] >= 97 && a[i] <= 122)
    {
      arr[count] = a[i] - 96;
      count++;
    }
    else if (a[i] >= 65 && a[i] <= 90)
    {
      arr[count] = a[i] - 64;
      count++;
    }
  }

  for (int i = 0; i < count; i++)
  {
    int bin[5] = {0};
    binary(arr[i], bin);
    for (int i = 0; i < 5; i++)
    {
      if (bin[i] == 0)
        en.push_back('a');
      else
        en.push_back('b');
    }
  }
}

void decryption(string &de, int arr[])
{
  int n = 0;
  int mul = 1;
  for (int i = 4; i >= 0; i--)
  {
    n += arr[i] * mul;
    mul *= 2;
  }
  de.push_back(64 + n);
}

void decrypt(string en, string &de)
{
  int l = en.length();
  int count = 0;
  int arr[5] = {0};
  for (int i = 0; i < l;)
  {
    count = 0;
    for (int j = i; j < i + 5; j++)
    {
      if (en[j] == 'a')
        arr[count] = 0;
      else
        arr[count] = 1;
      count++;
    }
    decryption(de, arr);
    i += 5;
  }
}

int main()
{
  string a, en, de;

  while (1)
  {
    int n, l;
    cout << "\n1. Enter the Message" << endl;
    cout << "2. Encrypting" << endl;
    cout << "3. Decrypting" << endl;
    cout << "4. Exit" << endl;
    cout << "Enter you choice : ";
    cin >> n;

    switch (n)
    {
    case 1:
      cout << "\nEnter Your message : ";
      cin.get();
      getline(cin, a);
      cout << endl;
      break;

    case 2:
      encrypt(a, en);
      cout << "\nEncrypted message : " << en << endl;
      break;

    case 3:
      decrypt(en, de);
      cout << "\nDecrypted message : " << de << endl;
      break;

    case 4:
      exit(0);
      break;

    default:
      cout << "Invalid Input" << endl;
    }
  }
}
