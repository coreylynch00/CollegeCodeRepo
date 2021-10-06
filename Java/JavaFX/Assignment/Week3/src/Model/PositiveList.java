package Model;


import java.util.ArrayList;

public class PositiveList{
	private ArrayList <PositiveContact> positive;
	
	//Create contact list
	public PositiveList() {
		positive = new ArrayList<PositiveContact>();
	}
	
	//Return contact list
	public ArrayList<PositiveContact> getPositiveList(){
		return positive;
	}
	
	//Add contact to list
	public void addPositiveContact(PositiveContact pc) {
		positive.add(pc);
	}
	
	//Get contact
	public PositiveContact getPositiveContact(int i) {
		if ((i >-1 && i<positive.size()))
			return positive.get(i);
		return null;
	}
	
	//Remove contact from list
	public void removePositiveContact(int i) {
		if ((i>-1 && i<positive.size()))
			positive.remove(i);
	}
	
	//Return size of contacts list
	public int getPositiveSize() {
		return positive.size();
	}
}