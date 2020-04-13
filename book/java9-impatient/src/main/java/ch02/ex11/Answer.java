// Rewrite the Cal class to use static imports for the System and
// LocalDate classes.

// Note:
//   "import static" can only import static methods and variables. So
//   can only import the now() and of() method of LocalDate, not very
//   useful here. Still need the regular import of LocalDate since we
//   need to declare variables of that type (unless we are using
//   java11's 'var').

package ch02.ex11;

import static java.time.LocalDate.now;
import static java.time.LocalDate.of;

import java.time.DayOfWeek;
import java.time.LocalDate;

public class Answer {

    private static final String[] LABEL = {
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
        final LocalDate date = now();
        if (args.length > 0) {
            // print specified month for this year
            printMonth(date.getYear(), Integer.parseInt(args[0]));
        } else {
            // print this month's calendar
            printMonth(date.getYear(), date.getMonthValue());
        }
    }

    private static void printHeader() {
        System.out.println(String.join(" ", LABEL));
    }

    private static void printMonth(int year, int month) {
        // get the first day of the month
        LocalDate start = of(year, month, 1);
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
