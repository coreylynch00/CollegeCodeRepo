// Corey Lynch - R00154863 - SD2-A

import java.util.ArrayList;
import java.util.Arrays;

public class Patients extends Person {

	//Constructor
	public Patients(Name name, String id, String phone) {
		super(name, id, phone);
	}
	
	//Create visits array
	ArrayList<Visits> visits = new ArrayList<Visits>();
	
	//Variables
	String illness;
	enum Level {
		LOW,
		MEDIUM,
		HIGH
	}
	
	//Get methods
	public String getIllness() {
		return illness;
	}
	
	//Set methods
	public void setIllness(String newIllness) {
		this.illness = newIllness;
	}
	
	//Add patient visit
	public void addVisit(int i, Visits e) {
		visits.add(e);
	}
	
	//Show all visits
	public ArrayList<Visits> showVisists() {
		System.out.println(Arrays.toString(visits.toArray()));
		return visits;
	}
}
