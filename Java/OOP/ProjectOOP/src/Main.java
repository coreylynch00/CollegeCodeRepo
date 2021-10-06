// Corey Lynch - R00154863 - SD2-A

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws FileNotFoundException, IOException {
		
		//Create new scanner
		Scanner input = new Scanner(System.in);
		
		//Display user menu
		System.out.println("Welcome to MyGP Consultancy App.");
		System.out.println("\nPlease select one of the options from the list below:");
		System.out.println("\n1. Display Patients");
		System.out.println("2. Display Consultants");
		System.out.println("3. Record Visit");
		System.out.println("4. Load Information from Text File");
		System.out.println("5. Quit");
		int menuInput = input.nextInt();
		
		//Display patients
		if (menuInput == 1) {
			System.out.println("Consultant 1 Patients:");
			//c1.showPatients();
			System.out.println("Consultant 2 Patients:");
			//c2.showPatients();
			System.out.println("Consultant 3 Patients:");
			//c3.showPatients();
		}
		
		//Display consultants
		else if (menuInput == 2) {
			System.out.println("Consultants:");
			//pract.showConsultants();
		}
		
		//Record a patients visit
		else if (menuInput == 3) {
			System.out.println("Record Visit:");
			
			//Create the patients name
			System.out.println("Enter patients first name:");
			String fName = input.next();
			System.out.println("Enter patients last name:");
			String lName = input.next();
			Name m0 = new Name(fName, lName);
			
			//Create patient details
			System.out.println("Enter the patients ID:");
			String id = input.next();
			System.out.println("Enter the patients phone number:");
			String phone = input.next();
			Patients p0 = new Patients(m0, id, phone);
			
			//Record patient visit details
			System.out.println("Enter the date of the visit:");
			String date = input.next();
			System.out.println("Additional notes:");
			String notes = input.next();
			Visits v0 = new Visits(date, notes);
			
			//Assign patient to visit
			p0.addVisit(0, v0);	
		}
		
		//Load info from .txt file
		else if (menuInput == 4) {
			try (BufferedReader br = new BufferedReader(new FileReader("Practice.txt"))) {
				   String line;
				   while ((line = br.readLine()) != null) {
				       System.out.println(line);
				   }
				}
		}
		
		//Quit the application
		else if (menuInput == 5) {
			System.out.println("Thank you for using MyGP! Goodbye!");
		}
		
		//Error handling
		else {
			System.out.println("Please choose between options [1 - 4]");
		}
	}
}
