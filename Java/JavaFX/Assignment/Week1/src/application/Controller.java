package application;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;
import javafx.scene.control.TextArea;
import java.lang.StringIndexOutOfBoundsException;

public class Controller {
	
	private ContactList contactList;
	
	//Create new contact list
	public Controller() {
		contactList = new ContactList();
	}
	
	//Create contact and add to list
	void addContactToList(String fName, String lName, String id, String phoneNumber) 
	{
		Contact c = new Contact(fName, lName, id, phoneNumber);
		contactList.addContact(c);
	}
	
	//Remove contact from list
	void removeContactFromList() {
		try {
		contactList.removeContact(contactList.getSize() - 1);
		}
		catch (StringIndexOutOfBoundsException stringIndexOOB) {
			System.out.println("List is empty!");
			System.exit(1);
		}
	}
	
	//Display contact list
	public String getContactList() {
		String allContacts = "\0";
		for (int i=0; i<contactList.getSize(); i++) {
			allContacts = allContacts + contactList.getContact(i) + "\n\n";
		}
		return allContacts;
	}
	
	//Save file			
	public void saveFile(String fileName, String closeContactsTextArea) {
		System.out.println("Saving files...");
		try {
			BufferedWriter file = new BufferedWriter(new FileWriter(fileName, true));
			file.write(closeContactsTextArea);
			file.close();
		}
		catch (IOException IOE) {
			System.exit(1);
		}
	}
	
	//Load files
	public void loadFile(TextArea closeContactsTextArea) {
		System.out.println("Loading file...");
		closeContactsTextArea.clear();
		try {
			File loadFile = new File("covidContacts.txt");
			Scanner scanner = new Scanner(loadFile);
			String str = "\0";
			
			while (scanner.hasNextLine()) {
				String fileContent = scanner.nextLine();
				str = str + fileContent + "\n";
				closeContactsTextArea.setText(str);
			}
			scanner.close();
		}
		catch (FileNotFoundException fileNotFoundExeption) {
			System.exit(1);
		}
	}
	
	//Exit the contact application
	void exitApplication() {
		System.out.println("Stay Safe & Positive. We're all in this togther.");
		System.exit(0);
	}
}
