package Model;


import java.util.ArrayList;

public class ContactList{
	private ArrayList <Contact> contacts;
	
	//Create contact list
	public ContactList() {
		contacts = new ArrayList<Contact>();
	}
	
	//Return contact list
	public ArrayList<Contact> getList(){
		return contacts;
	}
	
	//Add contact to list
	public void addContact(Contact c) {
		contacts.add(c);
	}
	
	//Get contact
	public Contact getContact(int i) {
		if ((i >-1 && i<contacts.size()))
			return contacts.get(i);
		return null;
	}
	
	//Remove contact from list
	public void removeContact(int i) {
		if ((i>-1 && i<contacts.size()))
			contacts.remove(i);
	}
	
	//Return size of contacts list
	public int getSize() {
		return contacts.size();
	}
}
