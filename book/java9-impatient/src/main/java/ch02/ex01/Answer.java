// Change the calendar printing program so it starts on week on a
// Sunday. Also make it print a newline at the end (but only one).

// Note:
//   pretty simple to change. Update prefix blank loop to start at 0
//   instead of 1, change LABEL. The rest remained the same.

package ch02.ex01;

import java.time.DayOfWeek;
import java.time.LocalDate;

public class Answer {

    static final String[] LABEL = {
       "Sun",
       "Mon",
       "Tue",
       "Wed",
       "Thu",
       "Fri",
       "Sat",
    };

    public static void main(String[] args) {
        // get today's date
        final LocalDate date = LocalDate.now();
        if (args.length > 0) {
            // print specified month for this year
            printMonth(date.getYear(), Integer.parseInt(args[0]));
        } else {
            // print this month's calendar
            printMonth(date.getYear(), date.getMonthValue());
        }
    }

    static void printHeader() {
        System.out.println(String.join(" ", LABEL));
    }

    static void printMonth(int year, int month) {
        // get the first day of the month
        LocalDate start = LocalDate.of(year, month, 1);
        // print header
        printHeader();
        // what day of week is it?
        DayOfWeek weekday = start.getDayOfWeek();
        int value = weekday.getValue();
        // print initial blanks
        int printed = 0;
        for (int i = 0; i < value; i++) {  // start at 0 for sunday
            System.out.print("    ");
            printed++;
        }
        while (start.getMonthValue() == month) {
            System.out.printf("%3d ", start.getDayOfMonth());
            start = start.plusDays(1);
            printed++;
            if (printed >= 7) {
                System.out.println("");
                printed = 0;
            }
        }
        if (printed > 0) {
            System.out.println("");
        }

    }
}
