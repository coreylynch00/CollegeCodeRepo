// Corey Lynch - R00154863 - SD2-A

public class Person {
	Name name;
	String id;
	String phone;

// Constructor 
	public Person(Name name, String id, String phone) {
		this.name = name;
		this.id = id;
		this.phone = phone;
	}
	
// Get Methods
	public Name getName() {
		return name;
	}
	public String getID() {
		return id;
	}
	public String getPhone() {
		return phone;
	}
	
// Set Methods
	public void setName(Name newName) {
		this.name = newName;
	}
	public void setID(String newID) {
		this.id = newID;
	}
	public void setPhone(String newPhone) {
		this.phone = newPhone;
	}
	
// toString Method
	public String toString() {
        return name+", "+id+", "+phone;
	}
	
// Equals method
	public boolean equals(Person otherPerson) {
		if (otherPerson.name.equals(name) && otherPerson.id.equals(id) && otherPerson.phone.equals(phone))
			return true;
		else
			return false;
	}
	
}
