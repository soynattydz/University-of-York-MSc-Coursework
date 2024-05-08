public class AllergyBST {
    private AllergyNode root;
        public void insertOrUpdatePatient(String allergyType, String recommendedVaccineType) {
            root = insertOrUpdatePatient(root, allergyType, recommendedVaccineType);
        }
    
        private AllergyNode insertOrUpdatePatient(AllergyNode node, String allergyType, String recommendedVaccineType) {
            if (node == null) {
                return new AllergyNode(allergyType, recommendedVaccineType);
            }
    
            int compareResult = allergyType.compareToIgnoreCase(node.allergyType);
    
            if (compareResult < 0) {
                node.left = insertOrUpdatePatient(node.left, allergyType, recommendedVaccineType);
            } else if (compareResult > 0) {
                node.right = insertOrUpdatePatient(node.right, allergyType, recommendedVaccineType);
            } else {
                // Allergy already exists, update the count
                node.updateCount(recommendedVaccineType);
            }
    
            return node;
        }
    
        public void inOrderTraversal() {
            inOrderTraversal(root);
        }
    
        private void inOrderTraversal(AllergyNode node) {
            if (node != null) {
                inOrderTraversal(node.left);
                System.out.println("Allergy Type: " + node.getAllergyType() +
                        ", Total No. Of Patients: " + node.getPatientCount());
                inOrderTraversal(node.right);
            }
        }
    }
    