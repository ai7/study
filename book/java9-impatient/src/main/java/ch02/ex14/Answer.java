// Compile the Network class. Note that the inner class file is named
// Network$Member.class. Use the javap program to spy on the generated
// code. The command
//   javap -private Classname
// displays the methods and instance variables. Where do you see the
// reference to the enclosing class? (In Linux/Mac OS, you need to put
// a \ before the $ symbol when running javap.)

// Note:
//   each .class file contains one and only one class. inner/nested
//   classes are generated with a $ in its name from outer$class.
//
// $ javap -private Exercise14\$Network\$Member.class
//   Compiled from "Exercise14.java"
//   public class ch02.Exercise14$Network$Member {
//     private java.lang.String name;
//     private java.util.ArrayList<ch02.Exercise14$Network$Member> friends;
//     final ch02.Exercise14$Network this$0;
//     public ch02.Exercise14$Network$Member(ch02.Exercise14$Network, java.lang.String);
//   }

package ch02.ex14;

import java.util.ArrayList;

public class Answer {

    public static class Network {
        public class Member {
            private String name;
            private ArrayList<Member> friends;

            public Member(String name) {
                this.name = name;
                friends = new ArrayList<>();
            }
        }

        private ArrayList<Member> members = new ArrayList<>();
    }

    public static void main(String[] args) {
        System.out.println("Hello, world");
    }
}
