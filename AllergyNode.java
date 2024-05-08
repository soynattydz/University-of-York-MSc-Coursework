public class AllergyNode {
    String allergyType;
    String recommendedVaccineType;
    int patientCount;
    AllergyNode left, right;

    // Default Constructor
     public AllergyNode() {
        this.allergyType = null;
        this.recommendedVaccineType = null;
        this.patientCount = 0;
        this.left = this.right = null;
    }

    // Parameterized Constructor
    public AllergyNode(String allergyType, String recommendedVaccineType) {
        this.allergyType = allergyType;
        this.recommendedVaccineType = recommendedVaccineType;
        this.patientCount = 1; // Initialize patient count to 1 for the first occurrence
        this.left = this.right = null;
    }

    // Add a getter method for the patientCount field
    public int getPatientCount() {
        return patientCount;
    }

    // Add a setter method for the patientCount field
    public void setPatientCount(int patientCount) {
        this.patientCount = patientCount;
    }

    // Add a getter method for the allergyType field
    public String getAllergyType() {
        return allergyType;
    }

    // Add a getter method for the recommendedVaccineType field
    public String getRecommendedVaccineType() {
        return recommendedVaccineType;
    }

     // Update patient count based on the recommended vaccine type
     public void updateCount(String recommendedVaccineType) {
        if ("AstraZeneca".equalsIgnoreCase(recommendedVaccineType) || "Pfizer".equalsIgnoreCase(recommendedVaccineType)) {
            patientCount++;
        }
     }
    }