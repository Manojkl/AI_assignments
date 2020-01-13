#include<iostream>
//fstream reads file from the terminal
#include<fstream>
#include<cstdlib>
using namespace std;

int main()
{   
    // creating a file reading variable
   char file[10];
    // Need to create a object to hold the file or read a file
    ifstream manoj;
    // allow the user to enter the filename and stored in "file"
    cin.getline(file,10);
    // open it using the manoj object
    manoj.open(file);

    // check if the file is open. if not close it immediately
    if(!manoj.is_open()){
        exit(EXIT_FAILURE);
    }
    // If the file opne do something

    char word[50];
    manoj >> word;
    // manoj >> noskipws;
    //This checks for until the end of the file 
    while (manoj.good())
    {
        // we add empty space because whenever we read from the word it omits the spaces
        cout << word << " ";
        manoj >> word;
    }
    int x;
    cin >> x;
    cout<< x<<endl;
    return 0;
}