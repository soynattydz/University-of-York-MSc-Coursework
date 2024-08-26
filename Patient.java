public class Patient 
{
    int patientID;
    String firstName;
    String lastName;
    int age;
    String allergyType;
    String vaccineType;
    String date;
    int dose;

    public Patient(int patientID, String firstName, String lastName, int age, String allergyType, String vaccineType, String date, int dose) 
    {
        this.patientID = patientID;
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        this.allergyType = allergyType;
        this.vaccineType = vaccineType;
        this.date = date;
        this.dose = dose;
    }

    // Add a getter method for the patientID field  
    public int getPatientID() 
    {
        return this.patientID;
    }

 // Add a getter method for the firstName field
    public String getFirstName() 
    {
        return this.firstName;
    }

 // Add a getter method for the lastName field
    public String getLastName() 
    {
        return this.lastName;
    }

 // Add a getter method for the age field
    public int getAge() 
    {
        return this.age;
    }

    // Add a getter method for the allergy field
    public String getAllergy() 
    {
        return this.allergyType;
    }

 // Add a getter method for the vaccineType field
    public String getVaccineType() 
    {
        return this.vaccineType;
    }

 // Add a getter method for the date field
 public String getDate() 
 {
     return this.date;
 }

 // Add a getter method for the dose field
 public int getDose() {
     return this.dose;
 }

 // Add a setter method for the dose field
 public void setDose(int dose) {
     this.dose = dose;
 }
}