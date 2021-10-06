// Corey Lynch
/**
* ADT MyStack: Private Part<br>. 
* The class implements all the operations available in MyStack<br>
*/
public class MyStaticStack implements MyStack {

	//--------------------------------------------------
	// Attributes
	//--------------------------------------------------

	private int items[]; 
	private int numItems;
	private int maxItems;

	//-------------------------------------------------------------------
	//-------------------------------------------------------------------	
	//public myStack myCreateEmpty(){}
	
	/**
	 * The constructor creates 1 instance (1 object) of the class MyStaticStack<br>
	 * @param m: The maximum number of items MyStack can contain.
	 */	 
	public MyStaticStack(int m){//TO-COMPLETE 
		this.numItems = 0;
		this.maxItems = m;
		this.items = new int[this.maxItems];
	}

	//-------------------------------------------------------------------
	// Basic Operation --> Check if MyStack is empty: isEmpty
	//-------------------------------------------------------------------	
	/**
	 * Given a concrete MyStack, it returns whether it is empty or not.<br>
	 * @return: Whether MyStack is empty or not.
	 */	
	public boolean isEmpty(){//TO-COMPLETE 
		//-----------------------------
		//Output Variable --> InitialValue
		//-----------------------------
		boolean res = true;

		//-----------------------------
		//SET OF OPS
		//-----------------------------
		
		//-----------------------------
		// I. SCENARIO IDENTIFICATION
		//-----------------------------
		int scenario = 0;
		
		//Rule 1: STACK EMPTY
		if(this.numItems == 0) {
			scenario = 1;
		}
		
		//Rule 2: STACK NOT EMPTY
		else {
			scenario = 2;
		}
		//-----------------------------
		// II. SCENARIO IMPLEMENTATION 
		//-----------------------------
		switch(scenario) {
		//Rule 1: STACK EMPTY
			case 1:
				res = true;
				break;
		
		//Rule 2: STACK NOT EMPTY
			case 2:
				res = false;
				break;
		}
		//-----------------------------
		//Output Variable --> Return FinalValue
		//-----------------------------
		return res;
	}
	
	//-------------------------------------------------------------------
	// Basic Operation (Partial) --> Get and remove first element from top of MyStack: pop
	//-------------------------------------------------------------------
	/**
	 * Given a concrete MyStack, it returns its head element (if any).<br>
	 * @return: Head element from MyStack (ERROR if there are no items in MyStack).
	 */	
	public int pop(){//TO-COMPLETE 
		//-----------------------------
		//Output Variable --> InitialValue
		//-----------------------------
		int res = -1;
		
		//-----------------------------
		//SET OF OPS
		//-----------------------------

		//-----------------------------
		// I. SCENARIO IDENTIFICATION
		//-----------------------------
		int scenario = 0;
		
		// Rule 1: ELEMENT TO POP FROM STACK
		if(numItems > 1 && numItems <= maxItems) {
			scenario = 1;
		}
		
		// Rule 2: LAST ELEMENT TO POP IN STACK
		else if (numItems == 1) {
			scenario = 2;
		}
		
		// Rule 3: NO ELEMENT TO POP FROM STACK
		else if (numItems == 0) {
			scenario = 3;
		}
		
		//-----------------------------
		// II. SCENARIO IMPLEMENTATION 
		//-----------------------------
		switch(scenario) {
		//Rule 1: SUCCESSFUL POP
		case 1:
			res = items[0];
			for(int i = 1; i < numItems; i++) {
				items[i - 1] = items[i];
				items[i] = 0;
			}
			numItems--;
			break;
			
		//Rule 2: 1 item in stack
		case 2:
			res = items[0];
			items[0] = 0;
			
		// Rule 3: INVALID POP
		case 3:
			System.out.println("Stack is EMPTY!");
			break;
		}
		//-----------------------------
		//Output Variable --> Return FinalValue
		//-----------------------------
		return res;
	}

		
	//-------------------------------------------------------------------
	// Basic Operation (Partial) --> Add element to the top of MyStack: push
	//-------------------------------------------------------------------
	/**
	 * Given a concrete MyStack, add an item by its head.<br>
	 * @param element: New item to be added to MyStack.	 
	 */	
	public void push(int element){//TO-COMPLETE 
		//-----------------------------
		//SET OF OPS
		//-----------------------------
	
		//-----------------------------
		// I. SCENARIO IDENTIFICATION
		//-----------------------------
		int scenario = 0;
				
		//Rule 1: STACK IS EMPTY
		if (numItems == 0) {
			scenario = 1;
		}
		
		//Rule 2: STACK IS NOT EMPTY, STACK IS NOT FULL
		else if (numItems < maxItems) {
			scenario = 2;
		}
		
		// STACK IS FULL
		else {
			scenario = 3;
		}
		
		//-----------------------------
		// II. SCENARIO IMPLEMENTATION 
		//-----------------------------
		switch(scenario) {
		//Rule 1: EMPTY
		case 1:
			items[0] = element;
			
		//Rule 2: NOT EMPTY NOT FULL
		case 2:
			for(int i = numItems-1; i >= 0; i--) {
				items[i + 1] = items[i];
			}
			items[0] = element;
			numItems++;
			System.out.println("Sucessfully pushed the item --- " + element);
			break;
			
		//Rule 3: FULL
		case 3:
			System.out.println("Stack is FULL!");
			break;
		}
	}
	//-------------------------------------------------------------------
	// Basic Operation (Partial) --> prints all the elements from MyStack: print
	//-------------------------------------------------------------------
	/**
	 * Given a concrete MyStack, prints all the elements (if any).<br>
	 * 
	 */	
	public void print(){//TO-COMPLETE 
		String res = "";
		//-----------------------------
		//SET OF OPS
		//-----------------------------
		
		//-----------------------------
		// I. SCENARIO IDENTIFICATION
		//-----------------------------
		
		//-----------------------------
		// II. SCENARIO IMPLEMENTATION 
		//-----------------------------
		
		for(int i = 0; i < maxItems; i++) {
			String stringVar = String.valueOf(items[i]);
			res += stringVar + " ";
			//System.out.println(stringVar);
		}
		System.out.println(res);
		
}
}