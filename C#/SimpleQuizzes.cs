using System;

class SimpleQuizzes {
  static void Main() {
      Console.WriteLine("What's your name? ");
      string name = Console.ReadLine();
      
      Console.WriteLine("Hi there " + name + ", can you do mental math? ");
      string answer = Console.ReadLine();
      
      if(answer=="Yes" || answer=="y" || answer=="yes" || answer == "Y" || answer == "sure" || answer == "Sure"){
          Console.WriteLine("Ok then, let's play");
      }
      
      else{
          Console.WriteLine("Maybe next time then");
      }
  }
}
