#include <iostream>
#include <string>

class Book {
    private:
        std::string isbn;
        std::string title;
        std::string author;
        int yearPublished;
    
    public:
        Book();
        
        Book(std::string isbn, std::string title, std::string author, int yearPublished) {
            this->isbn = isbn;
            this->title = title;
            this->author = author;
            this->yearPublished = yearPublished;
        };
        
        void setTitle(std::string isbn, std::string title){
            this->title = title;
        };
        
        void setAuthor(std::string isbn, std::string author){
            this->author = author;
        };
        
        void setYearPublished(std::string isbn, int yearPublished){
            this->yearPublished = yearPublished;
        };
    
        std::string getTitle(){
            return title;
        }
        
        std::string getAuthor(){
            return author;
        }
        
        int getYearPublished(){
            return yearPublished;
        }
    
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
    
};

int main()
{
    // Book book1;
    
    // std::cout << book1.bookInfo() << std::endl;
    
    Book book2("11111111", "Jackass", "Jack", 1234);
    
    book2.setYearPublished("11111111",2024);
    
    std::cout << book2.bookInfo() << std::endl;

    return 0;
}
