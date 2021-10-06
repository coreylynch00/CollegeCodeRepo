// Corey Lynch - R00154863 - SD2-A

public class Name {
	String firstName;
	String lastName;

// Constructor
	public Name(String firstName, String lastName) {
		this.firstName = firstName;
		this.lastName = lastName;
	}

// Get Methods
	public String getFirstName() {
		return firstName;
	}
	public String getLastName() {
		return lastName;
	}

// Set Methods
	public void setFirstName(String newFirstName) {
		this.firstName = newFirstName;
	}
	public void setLastName(String newLastName) {
		this.lastName = newLastName;
	}

// toString Method
	public String toString() {
		return firstName+" "+lastName;
	}

// Equals Method
	public boolean equals(Name otherName) {
		if (otherName.firstName.equals(firstName) && otherName.lastName.equals(lastName))
			return true;
		else
			return false;
	}
	
}