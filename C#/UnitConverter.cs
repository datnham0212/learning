using System;

public class UnitConverter
{
    public static void Main(string[] args)
    {
        bool on = true;
        while(on){
        Console.Write("Input: ");
        double input = Convert.ToDouble(Console.ReadLine());
        
        Console.WriteLine("Select options: ");
        Console.WriteLine("1.Length conversion");
        Console.WriteLine("2. Weight conversion");
        Console.WriteLine("3. Temparature conversion");
        Console.WriteLine("0. Exit");
        
        
        int choice = Convert.ToInt16(Console.ReadLine());
        
        if(choice == 1){
            // Length
            Console.WriteLine("1. From Millimeters to Inches");
            Console.WriteLine("2. From Inches to Millimeters");
            Console.WriteLine("3. From Kilometers to Miles");
            Console.WriteLine("4. From Miles to Kilometers");
            Console.WriteLine("0. Back to main menu");
            
            int lengthChoice = int.Parse(Console.ReadLine());
            switch(lengthChoice){
                case 1:
                    Console.WriteLine("Converted to roughly: {0}" + " inches", input*0.393701);
                    break;
            
                case 2:
                    Console.WriteLine("Converted to roughly: {0}" + " cm", input*2.54);
                    break;
                
                case 3:
                    Console.WriteLine("Converted to roughly: {0}" + " miles", input*0.621371);
                    break;
                case 4:
                    Console.WriteLine("Converted to roughly: {0}" + " meters", input*1.60934);
                    break;
                case 0:
                    continue;
            }
        }
        else if(choice == 2){
            // Weight
            Console.WriteLine("1. From Kilograms to Pounds");
            Console.WriteLine("2. From Pounds to Kilograms");
            Console.WriteLine("3. From Grams to Ounces");
            Console.WriteLine("4. From Ounces to Grams");
            Console.WriteLine("0. Back to main menu");
            
            int weightChoice = int.Parse(Console.ReadLine());
            switch(weightChoice){
                case 1:
                    Console.WriteLine("Converted to roughly: {0}" + " lbs", input*2.20462);
                    break;
                case 2:
                    Console.WriteLine("Converted to roughly: {0}" + " kg", input*0.453592); 
                    break;
                case 3:
                    Console.WriteLine("Converted to roughly: {0}" + " oz", input*0.035274);
                    break;
                case 4: 
                    Console.WriteLine("Converted to roughly: {0}" + " g", input*28.3495);
                    break;
                case 0:
                    continue;
            }
        }
        else if(choice == 3){
            //Temparature
            Console.WriteLine("1. From Celcius to Fahrenheit");
            Console.WriteLine("2. From Fahrenheit to Celcius");
            Console.WriteLine("3. From Celcius to Kelvin");
            Console.WriteLine("4. From Kelvin to Celcius");
            Console.WriteLine("0. Back to main menu");
            
            int temparatureChoice = int.Parse(Console.ReadLine());
            switch(temparatureChoice){
                case 1:
                    Console.WriteLine("Converted to roughly: {0}" + " F", input*(9/5) + 32);
                    break;
                case 2:
                    Console.WriteLine("Converted to roughly: {0}" + " C", (input-32)* 5/9);
                    break;
                case 3:
                    Console.WriteLine("Converted to roughly: {0}" + " K", input + 273.15);
                    break;
                case 4:
                    Console.WriteLine("Converted to roughly: {0}" + " C", input - 273.15);
                    break;
                case 0:
                    continue;
            }
        }
        else if(choice == 0){
            //Exit
            on = false;
            break;
        }
    }
    }
}
