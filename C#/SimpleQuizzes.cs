using System;


class mathQuestion {
    int a = 1;
    int b = 2;
    
    public void question(){
        Console.WriteLine("What's 1 + 2? ");
        int userAnswer = Convert.ToInt32(Console.ReadLine());
        int actualAnswer = a + b;
        
        string result = (userAnswer == actualAnswer) ? "Correct" : "Wrong";
        
        Console.WriteLine(result);
    }
}


class SimpleQuizzes {
  static void Main() {
      Console.WriteLine("What's your name? ");
      string name = Console.ReadLine();
      
      Console.WriteLine("Hi there " + name + ", can you do mental math? ");
      string answer = Console.ReadLine();
      
      if(answer=="Yes" || answer=="y" || answer=="yes" || answer == "Y" || answer == "sure" || answer == "Sure"){
          Console.WriteLine("Ok then, let's play");
          
          mathQuestion mq = new mathQuestion();
          mq.question();
      }
      
      else{
          Console.WriteLine("Maybe next time then");
      }
  }
}
