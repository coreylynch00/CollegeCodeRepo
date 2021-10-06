// Corey Lynch - R00154863 - SD2-A

public class Test {

	public static void main(String[] args) {
		
		//Create practice object
		Practice pract = new Practice();
		
		//CREATE CONSULTANTS
		//Create consultant c1
		Name n1 = new Name("Elaine", "Murphy");
		Consultant c1 = new Consultant(n1, "R01", "021 435 0011");
		
		//Create consultant c2
		Name n2 = new Name("Ted", "Murphy");
		Consultant c2 = new Consultant(n2, "R02", "021 435 0022");
		
		//Create consultant c3
		Name n3 = new Name("Ian", "Murphy");
		Consultant c3 = new Consultant(n3, "R03", "021 435 0033");
		
		//Add consultants to array
		pract.addConsultant(0, c1);
		pract.addConsultant(1, c2);
		pract.addConsultant(2, c3);
		
		//CREATE PATIENTS
		//Create patients p1
		Name m1 = new Name("Corey", "Lynch");
		Patients p1 = new Patients(m1, "P01", "086 000 1111");
		
		//Create patients p2
		Name m2 = new Name("Jake", "Sisk");
		Patients p2 = new Patients(m2, "P02", "086 001 2222");
		
		//Create patients p3
		Name m3 = new Name("Ber", "McCarthy");
		Patients p3 = new Patients(m3, "P02", "086 001 2222");
		
		//Create patients p4
		Name m4 = new Name("Marie", "O'Mahony");
		Patients p4 = new Patients(m4, "P02", "086 001 2222");
		
		//Create patients p5
		Name m5 = new Name("Sean", "O'Sullivan");
		Patients p5 = new Patients(m5, "P02", "086 001 2222");
		
		//Add patients to consultant c1
		c1.addPatient(0, p1);
		c1.addPatient(1, p2);
		
		//Add patients to consultant c2
		c2.addPatient(0, p3);
		c2.addPatient(1, p4);
		
		//Add patients to consultant c3
		c3.addPatient(0, p5);
		
		//Create patients Visits
		Visits v1 = new Visits("09/12/2020", "Checkup O.K."); 
		Visits v2 = new Visits("09/12/2020", "Abdominal pain, no temperature.");
		Visits v3 = new Visits("10/12/2020", "High termperature, prescribed antibiotics.");
		Visits v4 = new Visits("11/12/2020", "Checkup O.K.");
		Visits v5 = new Visits("05/01/2021", "Flu symptoms, sent for Covid test.");
		Visits v6 = new Visits("09/01/2021", "Covid test Negative, anitbiotic prescribed.");
		
		//Assign visits to p1
		p1.addVisit(0, v1);
		
		//Assign visits to p2
		p2.addVisit(0, v2);
		
		//Assign visits to p3
		p3.addVisit(0, v3);
		
		//Assign visits to p4
		p4.addVisit(0, v4);
		
		//Assign visits to p5
		p5.addVisit(0, v5);
		p5.addVisit(1, v6);
		
		//DISPLAY
		//Display Consultants
		System.out.println("Consultants:");
		pract.showConsultants();
		
		//Display c1 patients
		System.out.println("\nConsultant 1 Patients:");
		c1.showPatients();
		
		//Display c2 patients
		System.out.println("\nConsultant 2 Patients:");
		c2.showPatients();
		
		//Display c3 patients
		System.out.println("\nConsultant 3 Patients:");
		c3.showPatients();
		
		//DISPLAY VISIT DETAILS
		//Display patient 1 visit details
		System.out.println("\nPatient 1 Visit Details:");
		p1.showVisists();
		
		//Display patient 2 visit details
		System.out.println("\nPatient 2 Visit Details:");
		p2.showVisists();
		
		//Display patient 3 visit details
		System.out.println("\nPatient 3 Visit Details:");
		p3.showVisists();
		
		//Display patient 4 visit details
		System.out.println("\nPatient 4 Visit Details:");
		p4.showVisists();
		
		//Display patient 5 visit details
		System.out.println("\nPatient 5 Visit Details:");
		p5.showVisists();
		
	}
}
