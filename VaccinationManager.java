import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;

public class VaccinationManager {
    // Constants for menu options
    private static final int MENU_OPTION_EXIT = 8;

    // Global variables
    private static HashMap<Integer, Patient> patientsMap = new HashMap<>();
    private static HashMap<Integer, AllergyNode> allergiesMap = new HashMap<>();

    // Main
    public static void main(String[] args) {
        initializeSampleData();

        // Start the program
        Scanner scanner = new Scanner(System.in);

        int choice;
        do {
            System.out.println("Welcome to the Vaccination Manager!");
            displayMenu();
            // Get user choice with error handling
            choice = getIntegerInput(scanner);

            switch (choice) {
                case 1:
                    storeNewPatientData();
                    break;
                case 2:
                    generateReport();
                    break;
                case 3:
                    storeAllergyData();
                    break;
                case 4:
                    nextVaccinationAppointment();
                    break;
                case 5:
                    countPatientsByAllergy();
                    break;
                case 6:
                    patientsWithThreeDoses();
                    break;
                case 7:
                    elderlyPatientsLessThanThreeDoses();
                    break;
                case MENU_OPTION_EXIT:
                    System.out.println("Exiting the program. Goodbye!");
                    break;
                default:
                    System.out.println("Invalid choice. Please enter a valid option.");
            }

        } while (choice != MENU_OPTION_EXIT);

        scanner.close();
    }
 
    // Methods
    private static void displayMenu() {
        // Display menu
            System.out.println("1. Store collected user input data");
            System.out.println("2. Generate sample report to show how many patients are given each vaccination type");
            System.out.println("3. Store sample data on different allergies and recommended vaccine types");
            System.out.println("4. Next Vaccination Appointment");
            System.out.println("5. Count Patients for Each Allergy Type");
            System.out.println("6. Patients with Three Doses");
            System.out.println("7. Elderly Patients with Less Than Three Doses");
            System.out.println("8. Exit");
            System.out.print("Enter your choice: ");
    }

    private static void initializeSampleData() {
        // Part 1: Store collected patient and allergy data
        // Initialize sample patient and allergy data
        patientsMap.put(1, new Patient(1, "Georgia", "Roberts", 23, "Gelatin", "Pfizer", "06/15/2021", 1));
        patientsMap.put(2, new Patient(2, "Charlie", "Smith", 40, "Gelatin", "Pfizer", "06/15/2021", 1));
        patientsMap.put(3, new Patient(3, "Mariam", "Dawson", 27, "Gelatin", "Pfizer", "06/17/2021", 3));
        patientsMap.put(4, new Patient(4, "Emmett", "Miller", 30, "Gelatin", "Pfizer", "06/20/2021", 2));
        patientsMap.put(5, new Patient(5, "Lily", "Taylor", 18, "PEG", "AstraZeneca", "06/21/2021", 1));
        patientsMap.put(6, new Patient(6, "Bill", "Harley", 70, "PS80", "AstraZeneca", "07/21/2021", 1));

        allergiesMap.put(1, new AllergyNode("PEG", "AstraZeneca"));
        allergiesMap.put(2, new AllergyNode("PS80", "AstraZeneca"));
        allergiesMap.put(3, new AllergyNode("Gelatin", "Pfizer"));
    }

    private static void storeNewPatientData() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter patient ID: ");
        int patientID = getIntegerInput(scanner);

        // Check if patient ID already exists
        if (patientsMap.containsKey(patientID)) {
            System.out.println("Patient ID already exists. Please enter a unique ID.");
            return;
        }

        System.out.print("Enter first name: ");
        String firstName = scanner.next();

        System.out.print("Enter last name: ");
        String lastName = scanner.next();

        System.out.print("Enter age: ");
        int age = getIntegerInput(scanner);

        System.out.print("Enter allergy: ");
        String allergy = scanner.next();

        if (allergy.isEmpty()) {
            System.out.println("Allergy cannot be empty. Please enter a valid allergy.");
            return;
        }

        System.out.print("Enter vaccine type: ");
        String vaccineType = scanner.next();

        if (!vaccineType.equalsIgnoreCase("AstraZeneca") && !vaccineType.equalsIgnoreCase("Pfizer")) {
            System.out.println("Invalid vaccine type. Please enter AstraZeneca or Pfizer. This is case sensitive.");
            return;
        }

        System.out.print("Enter date: ");
        String date = scanner.next();

        Date parsedDate = parseDate(date);

        if (parsedDate == null) {
            System.out.println("Invalid date format. Please enter date in MM/dd/yyyy format.");
            return;
        }

        System.out.print("Enter dose: ");
        int dose = getIntegerInput(scanner);

        patientsMap.put(patientID, new Patient(patientID, firstName, lastName, age, allergy, vaccineType, date, dose));

        System.out.println("Patient data stored successfully.");

        if (ShowMenuAgain(scanner)) 
        {
            displayMenu();
        }
    }

    private static void generateReport() {
        Scanner scanner = new Scanner(System.in);
        // Part 2: Generate the sample report to show how many patients are given each vaccination type
        int countAstraZeneca = 0;
        int countPfizer = 0;

        for (Patient patient : patientsMap.values()) {
            if ("AstraZeneca".equalsIgnoreCase(patient.getVaccineType())) {
                countAstraZeneca++;
            } else if ("Pfizer".equalsIgnoreCase(patient.getVaccineType())) {
                countPfizer++;
            }
        }

        System.out.println("Sample Report:");
        System.out.println("Number of patients given each vaccination type:");
        System.out.println("AstraZeneca: " + countAstraZeneca + " patients");
        System.out.println("Pfizer: " + countPfizer + " patients");

        if (ShowMenuAgain(scanner)) {
            displayMenu();
        }
    }

    private static void storeAllergyData() {
        Scanner scanner = new Scanner(System.in);
    
        // Part 3: Store sample data on different allergies and recommended vaccine types
        System.out.print("Enter vaccine type (AstraZeneca or Pfizer): ");
        String vaccineType = scanner.next();
    
        if (!vaccineType.equalsIgnoreCase("AstraZeneca") && !vaccineType.equalsIgnoreCase("Pfizer")) {
            System.out.println("Invalid vaccine type. Please enter AstraZeneca or Pfizer.");
            scanner.close(); // Close the scanner before returning
            return;
        }
    
        // Display the patients who have the specified vaccine type in a table
        System.out.printf("%-15s%-15s%-5s%-15s%-15s%-15s%-15s%n",
                "Patient ID", "First Name", "Last Name", "Age", "Allergy", "Vaccine Type", "Date");
    
        for (Patient patient : patientsMap.values()) {
            if (patient.getVaccineType().equalsIgnoreCase(vaccineType)) {
                displayPatientInfoInTable(patient);
            }
        }
    
        // Show menu again or exit
        if (ShowMenuAgain(scanner)) 
        {
        displayMenu();    
        }
    }
    
    private static <T> void mergeSort(List<T> list, Comparator<T> comparator) {
        if (list.size() > 1) {
            int mid = list.size() / 2;
            List<T> left = new ArrayList<>(list.subList(0, mid));
            List<T> right = new ArrayList<>(list.subList(mid, list.size()));
    
            mergeSort(left, comparator);
            mergeSort(right, comparator);
    
            int i = 0, j = 0, k = 0;
    
            while (i < left.size() && j < right.size()) {
                if (comparator.compare(left.get(i), right.get(j)) < 0) {
                    list.set(k++, left.get(i++));
                } else {
                    list.set(k++, right.get(j++));
                }
            }
    
            while (i < left.size()) {
                list.set(k++, left.get(i++));
            }
    
            while (j < right.size()) {
                list.set(k++, right.get(j++));
            }
        }
    }
    
    // Modify nextVaccinationAppointment to call mergeSortByAge
    private static void nextVaccinationAppointment() {
        Scanner scanner = new Scanner(System.in);

        // Part 4: Next Vaccination Appointment
        System.out.println("Patients in Age Descending Order for Next Vaccination Priority:");
        System.out.printf("%-15s%-15s%-5s%-15s%-15s%-15s%-15s%n",
                "Patient ID", "First Name", "Last Name", "Age", "Allergy", "Vaccine Type", "Date");

        List<Patient> patientList = new ArrayList<>(patientsMap.values());
        mergeSort(patientList, Comparator.comparingInt(Patient::getAge).reversed());

        for (Patient patient : patientList) {
            displayPatientInfoInTable(patient); // Ensure this method is properly defined
        }

        // Ask the user if they want to see the menu again
        if (ShowMenuAgain(scanner)) {
            displayMenu();
        }
    }
    
    private static void countPatientsByAllergy() 
    {
         Scanner scanner = new Scanner(System.in);
        // Part 5: Count the number of patients given for each allergy type
        AllergyBST allergyBST = new AllergyBST(); // Create an instance of AllergyBST
        
        // Insert patient data into the BST
        for (Patient patient : patientsMap.values()) 
        {
            if (patient.getAllergy() != null && !patient.getAllergy().isEmpty()) 
            {
                allergyBST.insertOrUpdatePatient(patient.getAllergy(), patient.getVaccineType());
            }
        }

        // Display the patient count by allergy type and vaccine type
        System.out.println("Patients count by allergy type and vaccine type:");
        allergyBST.inOrderTraversal();

        if (ShowMenuAgain(scanner)) {
            displayMenu();
        }
    }

    private static void patientsWithThreeDoses() {
        Scanner scanner = new Scanner(System.in);
    
        // Part 6: Search, identify, and list those patients who have completed three doses of vaccine
        System.out.println("Patients with Three Doses:");
        System.out.printf("%-15s%-15s%-5s%-15s%-15s%-15s%-15s%n",
                "Patient ID", "First Name", "Last Name", "Age", "Allergy", "Vaccine Type", "Date");
    
        // Loop through the list of patients
        for (Patient patient : patientsMap.values()) {
            if (patient.getDose() == 3) {
                displayPatientInfoInTable(patient);
            }
        }
    
        // Ask the user if they want to see the menu again
        if (ShowMenuAgain(scanner)) {
            displayMenu();
        }
    }

    private static void elderlyPatientsLessThanThreeDoses() {
        Scanner scanner = new Scanner(System.in);
    
        // Part 7: Search, identify, and list the elderly patients (i.e., aged 70 or above) who were given fewer than three doses
        System.out.println("Elderly Patients with Less Than Three Doses:");
        System.out.printf("%-15s%-15s%-5s%-15s%-15s%-15s%-15s%n",
                "Patient ID", "First Name", "Last Name", "Age", "Allergy", "Vaccine Type", "Date");
    
        // Loop through the list of patients
        for (Patient patient : patientsMap.values()) {
            if (patient.getAge() >= 70 && patient.getDose() < 3) {
                displayPatientInfoInTable(patient);
            }
        }
    
        // Ask the user if they want to see the menu again
        if (ShowMenuAgain(scanner)) {
            displayMenu();
        }
    }  

    private static int getIntegerInput(Scanner scanner) { // Helper method to get integer input
        while (true) {
            System.out.print("Enter an integer: ");
            try {
                return Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a valid integer.");
            }
        }
    }

    private static Date parseDate(String date) { 
        SimpleDateFormat dateFormat = new SimpleDateFormat("mm/dd/yyyy"); // Set the format of the date
        dateFormat.setLenient(false);

        try {
            return dateFormat.parse(date);
        } catch (ParseException e) {
            return null;
        }
    }

    private static boolean ShowMenuAgain(Scanner scanner) {
        System.out.print("Do you want to see the menu again? (Y/N): ");
        String input = scanner.next().trim();

        // Check if the input is 'Y' or 'N'
        if (input.equalsIgnoreCase("Y")) {
            return true;
        } else if (input.equalsIgnoreCase("N")) {
            System.out.println("Thank you for using Vaccination Manager!");
            return false;
        } else {
            System.out.println("Invalid input. Please enter 'Y' or 'N'.");
            return ShowMenuAgain(scanner);  // Recursively ask for valid input
        }
    }

    private static void displayPatientInfoInTable(Patient patient) 
    {
    System.out.printf("%-15d%-15s%-15s%-5d%-15s%-15s%-15s%n",
            patient.getPatientID(), patient.getFirstName(), patient.getLastName(),
            patient.getAge(), patient.getAllergy(), patient.getVaccineType(), patient.getDate());
    }
}

//Pseudocode for this project
// 1. Create a class called VaccinationManager
    // Main class
        // Constants for menu options 
            // menu_option_exit = 9
        // Global variables for menu options
            // HashMaps for patients and allergies 
        // Main method
        // Task A.1
            // Initialize sample data
                    // Store sample data on the 3 different allergies and 2 recommended vaccine types for 6 patients
                // Ability to store new patient data
            // Start the program
            // Display menu 
                // Get user choice (integer) with error handling
                // Use switch statement to execute different actions based on user choice
                // Ask if user wants to see menu again

        // Task A.2
            // Generate sample report to show how many patients are given each vaccination type
                // Initialize counter variables for each vaccine type
                // Loop through the list of patients
                    // If the vaccine type is AstraZeneca or Pfizer, increment the corresponding counter variable
                // Display the sample report
        
        // Task A.3
            //procedure storeAllergyData()
    //scanner = new Scanner(System.in)
    
    // Store sample data on different allergies and recommended vaccine types
    //print("Enter vaccine type (AstraZeneca or Pfizer): ")
    //vaccineType = scanner.next()
    
    //if not (vaccineType.equalsIgnoreCase("AstraZeneca") or vaccineType.equalsIgnoreCase("Pfizer")) then
        //print("Invalid vaccine type. Please enter AstraZeneca or Pfizer.")
        //scanner.close() // Close the scanner before returning
        //return
    //end if
    
    // Display the patients who have the specified vaccine type in a table
    //printFormattedTableHeader("Patient ID", "First Name", "Last Name", "Age", "Allergy", "Vaccine Type", "Date")
    
    //for each patient in patientsMap.values()
        //if patient.getVaccineType().equalsIgnoreCase(vaccineType) then
            //displayPatientInfoInTable(patient)
        //end if
    //end for
    
    // Show menu again or exit
    //if ShowMenuAgain(scanner) then
        //displayMenu()
    //end if


//procedure mergeSort(list, comparator)
    //if list.size() > 1 then
        //mid = list.size() / 2
        //left = new ArrayList<>(list.subList(0, mid))
        //right = new ArrayList<>(list.subList(mid, list.size()))
    
        //mergeSort(left, comparator)
        //mergeSort(right, comparator)
    
        //i = 0
        //j = 0
        //k = 0
    
        //while i < left.size() and j < right.size()
            //if comparator.compare(left.get(i), right.get(j)) < 0 then
                //list.set(k, left.get(i))
                //i = i + 1
            //else
                //list.set(k, right.get(j))
                //j = j + 1
            //end if
            //k = k + 1
        //end while
    
        //while i < left.size()
            //list.set(k, left.get(i))
            //i = i + 1
            //k = k + 1
        //end while
    
        //while j < right.size()
            //list.set(k, right.get(j))
            //j = j + 1
            //k = k + 1
        //end while
    //end if


        
        // Merge Sort to sort the list of patients
            // Create a method to merge two sorted lists
            // Recursive calls to sort left and right halves of list 
            // Merge the sorted halves
            // Copy remaining elements of left and right halves to the original list
        
            // Task A.4
            // Next Vaccination Appointment with age based-priority
                // Create a new scanner to read user input
                // Loop through the list of patients in patientsMap
                    // Print the patients in age descending order for next vaccination priority
                // Create a new patient list from the values of patientsMap
                // Call mergeSortByAge
                // Use comparator to compare the ages of the patients in the list
                // Display the next vaccination appointment in a table
        
                // Task A.5
            // Count Patients for Each Allergy Type
                // Create a new scanner to read user input
                // Create a new instance of AllergyBST
                // Insert patient data into the BST
                    // BST is used to efficiently count the number of patients given for each allergy type and vaccine type
                // Display the patient count by allergy type and vaccine type

        // Task A.6
           //procedure patientsWithThreeDoses()
    //scanner = new Scanner(System.in)
    
    // Search, identify, and list those patients who have completed three doses of vaccine
    // print("Patients with Three Doses:")
    // printFormattedTableHeader("Patient ID", "First Name", "Last Name", "Age", "Allergy", "Vaccine Type", "Date")
    
    // Loop through the list of patients
    //for each patient in patientsMap.values()
        //if patient.getDose() equals 3 then
            //displayPatientInfoInTable(patient)
        //end if conditon
    //end for loop
    
    // Ask the user if they want to see the menu again
    // if ShowMenuAgain(scanner) then
        //displayMenu()
    //end if



        // Task A.7
            // Elderly Patients with Less Than Three Doses
                // Create a new scanner to read user input
                // Loop through the list of patients
                    // If the dose is less than 3 and patient is over 70, display the patient in a table

        // Enter your choice of integer from menu
            // Helper method to get integer input from user 
            // Helper method to check if input is within range of menu option
            // Uses a while true loop to get user input
            // Uses a catch block to handle non-integer inputs for error handling
        // Date Format code - mm/dd/yyyy
            // Helper method to get date input from user
            // Creates a simpleDateFormat object
            // Uses ParseException to handle invalid date format for error handling
        // Display menu again or exit
            // Helper method to prompt the user if they want to see the menu again
                // Uses a Boolean to determine 
            // Case insensitive check for 'Y' or 'N' with error handling
        // Patient table
            // Helper method to display the patient data in a table
            // Uses patient object to display the patient data

// 2. Create a class called Patient
        // Fields
            // private String patientID, firstName, lastName, age, allergy, vaccineType, date, dose;
        // Constructor
        // Getter methods
        // Setter methods

// 3. Create a class called AllergyNode
        // Fields
            // int allergyType, patientCount, vaccineType;
        // Default and Parameterized Constructors
        // Getter methods

// 4. Create a class called AllergyBST
        // Fields
            // private AllergyNode root; 
        // Public method
            // insertOrUpdatePatient 
            // Call private method with root node
        // Private method
            // insertOrUpdatePatient (recursive)
            // base case - if root is null, create a new AllergyNode
            // Compare allergy type with current node's allergy type
            // Recursive cases based on comparison result - left or right subtree
                // Insert or update in the left subtree
                // Insert or update in the right subtree
                // Allergy already exists, update the count 
