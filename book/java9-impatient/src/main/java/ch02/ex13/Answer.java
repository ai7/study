// Download the JAR file from OpenCSV from
// http://opencsv.sourceforge.net. Write a class with a main method
// that reads a CSV file of your choice and prints some of the
// content. There is sample code on the OpenCSV website. Your haven't
// yet learned to deal with exceptions. Just use the following headers
// for the main method:
//   public static void main(String[] args) throws Exception
// The point of this exercise is not to do anything useful with CSV
// files, but to practice using library that is delivered as a JAR
// file.

// Note:
//   added to gradle with: compile 'com.opencsv:opencsv:4.5'

package ch02.ex13;

import java.io.FileReader;
import java.io.IOException;
import java.util.Map;

import com.opencsv.CSVReaderHeaderAware;

public class Answer {

    public static void main(String[] args) throws IOException {
        if (args.length <= 0) {
            System.out.println("Usage: <csv file>");
        }
        String input = args[0];
        Map<String, String> values = new CSVReaderHeaderAware(
                new FileReader(input)).readMap();
    }
}
