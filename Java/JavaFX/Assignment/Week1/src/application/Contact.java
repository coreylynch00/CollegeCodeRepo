package application;

public class Contact {
	private String fName;
	private String lName;
	private String id;
	private String phoneNumber;
	
	//
	public Contact (String fName, String lName, String id, String phoneNumber) {
		this.fName = fName;
		this.lName = lName;
		this.id = id;
		this.phoneNumber = phoneNumber;
	}
	
	//Get methods 
	public String getFirstName() {
		return fName;
	}
	
	public String getLastName() {
		return lName;
	}
	
	public String getID() {
		return id;
	}
	
	public String getPhoneNumber() {
		return phoneNumber;
	}
	
	//Set methods 
	public void setFirstName(String newFName) {
		this.fName = newFName;
	}
	
	public void setLastName(String newLName) {
		this.lName = newLName;
	}
	
	public void setID(String newid) {
		this.id = newid;
	}
	
	public void setPhoneNumber(String newPhoneNumber) {
		this.phoneNumber = newPhoneNumber;
	}
	
	public String toString() {
		String s = "NAME: " + fName.toUpperCase() + " " + lName.toUpperCase() + "\n" + "UNIQUE ID: " + id + "\n" + "PHONE NO: " + phoneNumber;
		return s;
	}
}
