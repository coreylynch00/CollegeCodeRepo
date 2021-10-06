package application;

public class PositiveContact {
	private String fName;
	private String lName;
	private String date;
	private String time;
	
	//
	public PositiveContact (String fName, String lName, String date, String time) {
		this.fName = fName;
		this.lName = lName;
		this.date = date;
		this.time = time;
	}
	
	//Get methods 
	public String getFirstName() {
		return fName;
	}
	
	public String getLastName() {
		return lName;
	}
	
	public String getDate() {
		return date;
	}
	
	public String getTime() {
		return time;
	}
	
	//Set methods 
	public void setFirstName(String newFName) {
		this.fName = newFName;
	}
	
	public void setLastName(String newLName) {
		this.lName = newLName;
	}
	
	public void setDate(String newDate) {
		this.date = newDate;
	}
	
	public void setTime(String newTime) {
		this.time = newTime;
	}
	
	//toString method
	public String toString() {
		String p = "NAMES: " + fName + ", " + lName + "\n" + "DATE: " + date + "\n" + "TIME: " + time;
		return p;
	}
}
