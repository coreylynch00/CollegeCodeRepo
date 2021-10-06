// Corey Lynch - R00154863 - SD2-A

import java.util.ArrayList;
import java.util.Arrays;

public class Consultant extends Person {
	
	//Constructor
	public Consultant(Name name, String id, String phone) {
		super(name, id, phone);
	}
	
	//Create patients array
	ArrayList<Patients> patients = new ArrayList<Patients>();
	
	//Variables
	String expertise;
	
	//Get methods
	public String getExpertise() {
		return expertise;
	}
	
	//Set methods
	public void setExpertise(String newExpertise) {
		this.expertise = newExpertise;
	}
	
	//Add patient
	public void addPatient(int i, Patients e) {
		patients.add(e);
	}
	
	//Show all patients
	public ArrayList<Patients> showPatients() {
		System.out.println(Arrays.toString(patients.toArray()));
		return patients;
	}
	
}