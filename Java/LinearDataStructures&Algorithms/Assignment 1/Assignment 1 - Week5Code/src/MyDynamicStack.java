// Corey Lynch
/**
* ADT MyStack: Private Part<br>. 
* The class implements all the operations available in MyStack<br>
*/
public class MyDynamicStack implements MyStack {

	//--------------------------------------------------
	// Attributes
	//--------------------------------------------------
	private MyNode head;
	private int numItems;
	//-------------------------------------------------------------------
	// Basic Operation --> Check if MyStack is empty: myCreateEmpty
	//-------------------------------------------------------------------	
	//public myStack myCreateEmpty(){}
	
	public MyDynamicStack(){//TO-COMPLETE 
		this.head = new MyNode(0, null;
		this.numItems = 0;
	}

	//-------------------------------------------------------------------
	// Basic Operation --> Check if MyStack is empty: isEmpty
	//-------------------------------------------------------------------	

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
		
		//Rule 1: STACK IS EMPTY
		if(this.numItems == 0) {
			scenario = 1;
		}
		//Rule 2: STACK IS NOT EMPTY
		else {
			scenario = 2;
		}
		
		//-----------------------------
		// II. SCENARIO IMPLEMENTATION 
		//-----------------------------
		//Rule 1: STACK EMPTY
		switch(scenario) {
			case 1:
				res = true;
				break;
			
		//Rule 2: STACK IS NOT EMPTY
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
	// Basic Operation (Partial) --> Get first element from the top of MyStack and removes it: pop
	//-------------------------------------------------------------------

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
		
		//Rule 1: NO ITEMS TO POP FROM STACK
		if(numItems < 0) {
			scenario = 1;
		}
		//Rule 2: ITEMS TO POP FROM STACK
		else {
			scenario = 2;
		}
		//-----------------------------
		// II. SCENARIO IMPLEMENTATION 
		//-----------------------------
		switch(scenario) {
		//Rule 1: NO ITEMS TO POP FROM STACK
		case 1:
			System.out.println("Stack is EMPTY!");
			break;
		//SUCCESSFUL POP
		case 2:
			head = head.getNext();
			this.numItems = this.numItems - 1;
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
	
	public void push(int element){//TO-COMPLETE 
		//-----------------------------
		//SET OF OPS
		//-----------------------------
	
		//-----------------------------
		// I. SCENARIO IDENTIFICATION
		//-----------------------------
		int scenario = 0;
		
		//Rule 1: SUCCESSFULLY PUSHED ITEM FROM STACK
		if (numItems >= 0) {
			scenario = 1;
		}
		
		//-----------------------------
		// II. SCENARIO IMPLEMENTATION 
		//-----------------------------
		
		switch(scenario) {
		//Rule 1: Successful push
		case 1:
			MyNode newNode = new MyNode(element, this.head.getNext());
			this.head.setNext(newNode);
			this.numItems = this.numItems + 1;
			break;
		}
	}
	
	//-------------------------------------------------------------------
	// Basic Operation (Partial) --> prints all the elements from MyStack: print
	//-------------------------------------------------------------------
	
	public void print(){//TO-COMPLETE 
		//-----------------------------
		//SET OF OPS
		//-----------------------------

		//-----------------------------
		// I. SCENARIO IDENTIFICATION
		//-----------------------------
		
		//-----------------------------
		// II. SCENARIO IMPLEMENTATION 
		//----------------------------
		MyNode currentNode = this.head;
		System.out.println(this.head);
		for(int i = numItems; i < 0; i--){
			MyNode current = currentNode.getNext();
			System.out.println(current.getInfo());
			currentNode = current;
			
		}
		
	}
	
	
}
