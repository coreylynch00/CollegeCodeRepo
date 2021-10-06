//Corey Lynch - R00154863 - SD2-A

import java.util.ArrayList;
import java.util.Arrays;

public class Practice {
	
	//Create consultants array
	ArrayList<Consultant> consultants = new ArrayList<Consultant>();
	
	//Variables
	private int length;
	
	//Add consultant
	public void addConsultant(int i, Consultant e) {
		consultants.add(e);
	}
	
	//Remove consultant
	public void removeConsultant(int i, Consultant e) {
		consultants.remove(e);
	}
	
	//Show consultants
	public ArrayList<Consultant> showConsultants() {
		System.out.println(Arrays.toString(consultants.toArray()));
		return consultants;
	}
	
	//Find consultant
	public boolean findConsultant() {
		for (int i = 0; i < this.length; i++) {
			String p = null;
			if (consultants.get(i).equals(p)) {
				return true;
			}
		}
		return false;
	}
	
	//Show consultant details
	public ArrayList<Consultant> consultantDetails() {
		System.out.println(Arrays.toString(consultants.toArray()));
		return consultants;
	}
}

