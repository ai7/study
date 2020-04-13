// Fully implement the Invoice class in Section 2.6.1, "Static Nested
// Classes" (page 85). Provide a method that prints the invoice and a
// demo program that constructs and prints a sample invoice.

// Note: pretty straightforward.

package ch02.ex15;

import java.util.ArrayList;

public class Answer {

    public static class Invoice {
        private ArrayList<Item> items = new ArrayList<>();

        public void addItem(String description, int quantity, double unitPrice) {
            Item newItem = new Item(description, quantity, unitPrice);
            items.add(newItem);
        }

        public void printInvoice() {
            for (Item x: items) {
                System.out.println(x);
            }
        }

        public static class Item {
            private String description;
            private int quantity;
            private double unitPrice;

            public Item(String description, int quantity, double unitPrice) {
                this.description = description;
                this.quantity = quantity;
                this.unitPrice = unitPrice;
            }

            public double price() {
                return quantity * unitPrice;
            }

            @Override
            public String toString() {
                return "Item{" +
                        "description='" + description + '\'' +
                        ", quantity=" + quantity +
                        ", unitPrice=" + unitPrice +
                        ", totalPrice=" + price() +
                        '}';
            }
        }
    }

    public static void main(String[] args) {
        Invoice myInvoice = new Invoice();
        myInvoice.addItem("Blackwell Toaster",
                2, 19.95);
        myInvoice.addItem("Banana",
                7, 0.33);
        myInvoice.printInvoice();
    }
}
