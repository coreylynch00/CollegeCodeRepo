// Corey Lynch - R00154863 - SD2-A

//I imported the java date library below. However when I used the date data type in the constructor and called the constructor in the Test class
//and gave the argument within the parameters, it was being read in as a type int and was expecting type date. I assume I was using the incorrect date format so it did not
//recognise it was a date. I couldn't find any date format that would work so was forced to change the data type to String.

//import java.util.Date;

public class Visits {
	
	//Variables
	String visitDate;
	String notes;
	
	//Constructor
	public Visits(String visitDate, String notes) {
		this.visitDate = visitDate;
		this.notes = notes;
	}

	//Get methods
	public String getVisitDate() {
		return visitDate;
	}
	
	public String getNotes() {
		return notes;
	}
	
	//Set methods
	public void setVisitDate(String newVisitDate) {
		this.visitDate = newVisitDate;
	}
	
	public void setNotes(String newNotes) {
		this.notes = newNotes;
	}
	
	// toString Method
		public String toString() {
			return visitDate+" "+notes;
		}
	
}
