// Make a file HelloWorld.java that declares a class HelloWorld in a
// package ch01.sec01. Put it into some directory, but _not_ in a
// ch01/sec01 subdirectory. From that directory, run javac
// HelloWorld.java, Do you get a class file? Where? Then run java
// HelloWorld. What happens? Why? (Hint: run javap HelloWorld and
// study the warning message.) Finally, try javac -d .
// HelloWorld.java. Why is that better?

// Note:
//   javac: .class file is produced in current directory.
//   java: can't load class, error is:
//     java.lang.NoClassDefFoundError: ch01/sec01/Exercise12 (wrong name: Exercise12)
//     javap is a Java class file disassembler:
//       Warning: File ./Exercise12.class does not contain class Exercise12
//       public class ch01.sec01.Exercise12 {
//         public ch01.sec01.Exercise12();
//         public static void main(java.lang.String[]);
//       }
//     javac -d . Exercise12.java
//       this produces the required directory structure "ch01/sec02/Exercise12.class"

// package ch01.sec01;  // for exercise
package ch02.ex12;           // for gradle

public class Answer {

    public static void main(String[] args) {
        System.out.println("Hello, world.");
    }

}
