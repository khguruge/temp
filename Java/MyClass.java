public class MyClass {
    public static void main(String[] args) {
      double myDouble = 9.78;
      int myInt = (int) myDouble; // Manual casting: double to int
  
      System.out.println(myDouble);   // Outputs 9.78
      System.out.println(myInt);      // Outputs 9
      String txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
      System.out.println("The length of the txt string is: " + txt.length());


      int x = 10;
      System.out.println(x);

      System.out.println(txt);
      String firstName = "John";
      String lastName = "Doe";
      System.out.println(firstName + " " + lastName);

      String first= "John ";
      String last = "Doe";
      System.out.println(first.concat(last));
      System.out.println(10 > 9); 
      int time = 20;
      if (time < 18) {
        System.out.println("Good day.");
      } else {
        System.out.println("Good evening.");
      }

      String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
      cars[0] = "Opel";
      for (int i = 0; i < cars.length; i++) {
        System.out.println(cars[i]);
      }

      try {
      int[] myNumbers = {1, 2, 3};
      System.out.println(myNumbers[1]);
    } catch (Exception e) {
      System.out.println("Something went wrong.");
    } finally {
      System.out.println("The 'try catch' is finished.");
    }
    }
  }