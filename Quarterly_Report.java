import java.text.NumberFormat;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Locale;

public class Quarterly_Report {

    // Constants
    static final int totalQuarters = 2; // 2 quarters of 3 months each
    static final String[] departments = {"Electrical", "Kitchen", "Bathroom", "Soft Furnishing", "Accessories"};

    // Initialise number format to format currency later in the code
    static NumberFormat currencyFormat = NumberFormat.getCurrencyInstance(Locale.UK);

    // 3D Array initialisation to store sales data
    static int[][][] monthlySales = 
    {
        // First quarter (3 months: April, May, June)
        {
            // Electrical department
            {67, 65, 63},
            // Kitchen department
            {65, 67, 56},
            // Bathroom department
            {63, 63, 65},
            // Soft Furnishing department
            {18, 24, 22},
            // Accessories department
            {16, 23, 21}
            },
        // Second quarter (3 months: July, August, September)
        {
            // Electrical department
            {78, 78, 104},
            // Kitchen department
            {56, 45, 56},
            // Bathroom department
            {65, 71, 73},
            // Soft Furnishing department
            {22, 19, 17},
            // Accessories department
            {19, 20, 19}
        }
    };

    // 2D and 1D Arrays to store calculated data
    static int[][] totalSales = new int [totalQuarters][departments.length];
    static double [] taxForQuarter = new double [totalQuarters];

    // Main method, starts the program, and calls other methods
    // From the main method, one can understand the flow of the program
    public static void main(String[] args) 
    {
            // Calculate total sales for each department per quarter
            calculateTotalSales(monthlySales, departments, totalQuarters);
    
            // Calculate tax on total sales with rate 17%
            calculateTaxOnTotalSales(totalSales, totalQuarters);
    
            // Calculate new sales target with a 12% increase
            calculateNewSalesTarget(monthlySales, departments);
    
            // Display results
            displayResults();
        }
    
    

    // Calculate total sales for each department per quarter 
    static void calculateTotalSales(int[][][] monthlySales, String[] departments, int totalQuarters) 
    {
        for (int q = 0; q < totalQuarters; q++) {
            for (int d = 0; d < departments.length; d++) {
                // Get the number of months for the current department
                int numMonths = monthlySales[q][d].length; // Get the actual number of months for the current department
                for (int m = 0; m < numMonths; m++) {
                    totalSales [q][d] += monthlySales[q][d][m];
                }
            }
        }
    }
    

    // Calculate tax on total sales with rate 17%
    static void calculateTaxOnTotalSales(int[][] totalSales, int totalQuarters) {
        double taxRate = 0.17; // 17%

        for (int q = 0; q < totalQuarters; q++) {
            // Check if total sales for the first department is non-zero before calculating tax
            if (totalSales[q][0] != 0) { // Check if total sales for the first department is non-zero, if the condition is true, calculate tax
                taxForQuarter[q] = totalSales[q][0] * taxRate; // tax is calculated on the total sales of the first department
            } else {
                // Handle the case where total sales is zero to avoid division by zero, print warning message
                System.out.println("Warning: Total sales for this department is zero for this quarter " + (q + 1));
                taxForQuarter[q] = 0; // Set tax to zero or handle it according to your application's logic
            } 
        }
    }

    // Calculate new sales target with a 12% increase
static void calculateNewSalesTarget(int[][][] monthlySales, String[] departments) {
    for (int d = 0; d < departments.length; d++) {
        double averageSales = calculateAverageSales(monthlySales, d);

        try {
            BigDecimal newSalesTarget = BigDecimal.valueOf(averageSales * 1.12); // 12% increase
            newSalesTarget = newSalesTarget.setScale(2, RoundingMode.HALF_UP); // Round to 2 decimal places
            System.out.println("New Sales Target for " + departments[d] + ": " + currencyFormat.format(newSalesTarget.multiply(BigDecimal.valueOf(1000))));
        
            // Add a space after the last "New Sales Target" output
            if (d == departments.length - 1) {
                System.out.println();
        }
        } catch (ArithmeticException e) {
            // Handle the case where there's an arithmetic exception (e.g., division by zero)
            System.err.println("Error calculating new sales target for department " + departments[d] + ": " + e.getMessage());
        }
    }
}


    // Method to calculate average sales for each department
    static double calculateAverageSales(int[][][] monthlySales, int departmentIndex) {
        int totalMonths = monthlySales[0][departmentIndex].length;
        int totalQuarters = monthlySales.length;
        int totalSales = 0;

        for (int q = 0; q < totalQuarters; q++) {
            totalSales += monthlySales[q][departmentIndex][totalMonths - 1]; // Last month of the quarter
        }

        return (double) totalSales / totalQuarters;
    }

    // Display results
    static void displayResults() {
        NumberFormat currencyFormat = NumberFormat.getCurrencyInstance(Locale.UK);
        currencyFormat.setMaximumFractionDigits(2);
    
        for (int q = 0; q < totalQuarters; q++) {
            for (int d = 0; d < departments.length; d++) {
                System.out.println("Quarter " + (q + 1) + " total sales for " + departments[d] + ": " +
                        currencyFormat.format(totalSales[q][d] * 1000));
            }
    
            System.out.println("Tax for Quarter " + (q + 1) + ": " +
                    currencyFormat.format(taxForQuarter[q] * 1000));
            System.out.println();
        }
    }
}