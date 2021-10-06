package Controller;


import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

import Model.Contact;
import Model.ContactList;
import Model.PositiveContact;
import Model.PositiveList;
import javafx.scene.control.TextArea;
import java.lang.StringIndexOutOfBoundsException;

public class Controller {
	
	private ContactList contactList;
	private PositiveList positiveList;
	
	//Create new contact list
	public Controller() {
		contactList = new ContactList();
		positiveList = new PositiveList();
	}
	
	//Create contact and add to list
	void addContactToList(String fName, String lName, String id, String phoneNumber) 
	{
		Contact c = new Contact(fName, lName, id, phoneNumber);
		contactList.addContact(c);
	}
	
	//Create positive contact and add to list
	void addPositiveToList(String fName, String lName, String date, String time) {
		PositiveContact pc = new PositiveContact(fName, lName, date, time);
		positiveList.addPositiveContact(pc);
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
	
	//Remove positive contact from list
		void removePositiveContactFromList() {
			try {
			positiveList.removePositiveContact(positiveList.getPositiveSize() - 1);
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
	
	//Display positive contact list
		public String getPositiveContactList() {
			String allPositiveContacts = "\0";
			for (int i=0; i<positiveList.getPositiveSize(); i++) {
				allPositiveContacts = allPositiveContacts + positiveList.getPositiveContact(i) + "\n\n";
			}
			return allPositiveContacts;
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
			String string = "\0";
			
			while (scanner.hasNextLine()) {
				String fileContent = scanner.nextLine();
				string = string + fileContent + "\n";
				closeContactsTextArea.setText(string);
			}
			scanner.close();
		}
		catch (FileNotFoundException fileNotFoundExeption) {
			System.exit(1);
		}
	}
	
	//Load files
	public void loadPositiveFile(TextArea positiveContactsTextArea) {
		System.out.println("Loading file...");
		positiveContactsTextArea.clear();
		try {
			File loadFile = new File("covidPositiveContacts.txt");
			Scanner scanner = new Scanner(loadFile);
			String string = "\0";
			
			while (scanner.hasNextLine()) {
				String fileContent = scanner.nextLine();
				string = string + fileContent + "\n";
				positiveContactsTextArea.setText(string);
			}
			scanner.close();
		}
		catch (FileNotFoundException fileNotFoundExeption) {
			System.exit(1);
		}
	}
	
	//Save positive contacts to file
	public void savePositiveContacts(String fileName, String positiveContactsTextArea) {
		System.out.println("Saving positive contacts...");
		try {
			BufferedWriter file = new BufferedWriter(new FileWriter(fileName, true));
			file.write(positiveContactsTextArea);
			file.close();
		}
		catch (IOException IOE) {
			System.exit(1);
		}
	}
	
	//Exit the contact application
	void exitApplication() {
		System.out.println("Stay Safe & Positive. We're all in this togther.");
		System.exit(0);
	}
	
	//Get fName and lName for comboBox
	public ArrayList<String> comboBoxArray() {
		ArrayList<String> comboArray = new ArrayList<String>();
		for (int i=0; i<contactList.getSize(); i++) {
			Contact comboBoxName = contactList.getContact(i);
			String comboBoxString = comboBoxName.getFirstName() + " " + comboBoxName.getLastName();
			comboArray.add(comboBoxString);
		}
		return comboArray;
	}
}
