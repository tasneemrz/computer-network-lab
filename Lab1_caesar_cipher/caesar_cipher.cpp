#include <bits/stdc++.h>
using namespace std;

string encrypt(string msg, int key)
{
    string res = "";
    for (auto &i : msg) {
        res += (((i - 'a' + key) % 26) + 'a');
    }
    return res;
}

string decrypt(string msg, int key)
{
    string res = "";
    for (auto &i : msg){
        res += ('a' + ((i - 'a' - key + 26) % 26));
    }
    return res;
}

int main()
{
    string msg;
    int key;

    cout << "Enter text : ";
    cin >> msg;

    cout << "Enter Key : ";
    cin >> key;

    string encrypt_msg = encrypt(msg, key);
    cout << "Cipher Text : " << encrypt_msg << "\n";

    string decrypt_msg = decrypt(encrypt_msg, key);
    cout << "Deciphered Text : " << decrypt_msg << "\n";
}