#include <iostream>
#include <string>

class Book {
    public:
        std::string isbn;
        std::string title;
        std::string author;
        int yearPublished;
        
        Book(std::string isbn, std::string title, std::string author, int yearPublished) {
            this->isbn = isbn;
            this->title = title;
            this->author = author;
            this->yearPublished = yearPublished;
        }
        
        std::string bookInfo(){
            return isbn + '\n' + title + '\n' + author + '\n' + std::to_string(yearPublished);
        }
        
};

int main()
{
    Book book("1111111111111", "Jackass", "Jack", 2019);
    
    std::cout << book.bookInfo() << std::endl;

    return 0;
}
