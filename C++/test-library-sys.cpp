#include <iostream>
#include <string>

typedef struct { 
    std::string isbn;
    std::string title;
    std::string author;
    int yearPublished;
} Book; 


void printBookInfo(Book book) {
    std::cout << book.title + "\n" + "ISBN: " + book.isbn + "\nBy: " + book.author + "\n" + std::to_string(book.yearPublished) << std::endl;
}

int main()
{
    Book book = {"9780060194994", "To kill a mocking bird", "Harper Lee", 1960};
    
    printBookInfo(book);

    return 0;
}
