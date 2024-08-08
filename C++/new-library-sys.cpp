#include <iostream>
#include <string>

class Book {
    public:
        std::string isbn;
        std::string title;
        std::string author;
        int yearPublished;
        
        Book();
        
        Book(std::string isbn, std::string title, std::string author, int yearPublished) {
            this->isbn = isbn;
            this->title = title;
            this->author = author;
            this->yearPublished = yearPublished;
        };
        
        std::string bookInfo(){
            return '\n' + isbn + '\n' + title + '\n' + author + '\n' + std::to_string(yearPublished);
        };
        
};

Book::Book(){
    std::cout << "\nISBN? ";
    std::cin >> isbn;
    
    std::cout << "\nWhat's the name of the book? ";
    std::cin >> title;
    
    std::cout << "\nAuthor's name? ";
    std::cin >> author;
    
    std::cout << "\nYear published? ";
    std::cin >> yearPublished;
    
}

int main()
{
    Book book;
    
    std::cout << book.bookInfo() << std::endl;

    return 0;
}
