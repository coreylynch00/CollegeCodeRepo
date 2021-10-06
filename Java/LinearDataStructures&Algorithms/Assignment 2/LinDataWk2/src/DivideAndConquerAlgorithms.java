
/**
 * The class contains the Divide and Conquer-based Algorithms we are using. 
 */
public class DivideAndConquerAlgorithms {

	//----------------------------------------------
	// Class constructor
	//----------------------------------------------	
	/**
	 * Constructor of the class. Do not edit it.
	 */
	public DivideAndConquerAlgorithms(){}
		
	//-------------------------------------------------------------------
	// 0. iterativeDisplayElements --> Displays all elements of a MyList 
	//-------------------------------------------------------------------	
	/**
	 * Given a concrete MyList, this iterative algorithm displays its elements by screen (if any).
	 * @param m: The MyList we want to display its elements.	  
	 */	
	public void iterativeDisplayElements(MyList<Integer> m){
		//-----------------------------
		//SET OF OPS
		//-----------------------------

		//-----------------------------
		// I. SCENARIO IDENTIFICATION
		//-----------------------------
		int scenario = 0; 
		
		//Rule 1. MyList is empty
		if (m.length() == 0) 
			scenario = 1;
		//Rule 2. MyList is non-empty
		else
			scenario = 2;

		//-----------------------------
		// II. SCENARIO IMPLEMENTATION 
		//-----------------------------
		switch(scenario){	
				
		//Rule 1. MyList is empty
		case 1: 
			//1. We print the empty message
			System.out.println("Empty MyList");
			
			break;
			
		//Rule 2. MyList is non-empty
		case 2: 
			//1. We print the initial message
			int size = m.length();
			System.out.println("MyList Contains the following " + size + " items: ");
			
			//2. We traverse the items
			for (int i = 0; i < size; i++)
				System.out.println("Item " + i + ": " + m.getElement(i));
			
			break;
	
		}
		
	}

	//-------------------------------------------------------------------
	// 1. recursiveDisplayElements --> Displays all elements of a MyList  
	//-------------------------------------------------------------------	
	/**
	 * Given a concrete MyList, this recursive algorithm displays its elements by screen (if any).
	 * @param m: The MyList we want to display its elements.	  
	 */	
	public void recursiveDisplayElements(MyList<Integer> m){
		int x = 0;
		//-----------------------------
		// I. SCENARIO IDENTIFICATION
		//-----------------------------
		int scenario = 0; 	
		
		//Rule 1:
		if (m.length() == 0) {
			scenario = 1;
		}
		
		//Rule 2 
		else 
			scenario = 2;
	
		//-----------------------------
		// II. SCENARIO IMPLEMENTATION 
		//-----------------------------
		switch(scenario){	
		case 1:
			System.out.println("List is empty!");
			break;
		
		case 2:
			if (x < m.length()) {
				System.out.println(m.getElement(x));
				x = x + 1;
				recursiveDisplayElements(m);
				}
			else
				x = 0;
			break;
			}
		}			

	//-------------------------------------------------------------------
	// 2. smallerMyList --> Filters all elements in MyList smaller than e
	//-------------------------------------------------------------------	
	/**
	 * The function filters all elements of MyList being smaller than 'e'  
	 * @param m: The MyList we want to check.
	 * @param e: The number 'e' we want to compare each element of MyList to.
	 * @return: The new MyList containing just the elements being smaller than 'e'  
	 */	
	public MyList<Integer> smallerMyList(MyList<Integer> m, int e){
		//-----------------------------
		//Output Variable --> InitialValue
		//-----------------------------
		MyList<Integer> res = null;

		//-----------------------------
		//SET OF OPS
		//-----------------------------

		//-----------------------------
		// I. SCENARIO IDENTIFICATION
		//-----------------------------
		int scenario = 0; 	
		
		//Rule 1: Empty
		if(m.length()==0){
            scenario =1;
        }
		
		//Rule 2: Not empty
        else{
            scenario =2;
        }
		
		//-----------------------------
		// II. SCENARIO IMPLEMENTATION 
		//-----------------------------
		switch(scenario){	
        case 1:
            break;
        case 2:
                int x = 0;
                for (int i = 0; i < m.length() ;i++){
                    if (m.getElement(i) < e){
                        res.addElement(x, m.getElement(i));
                        x++;
                    }
                }
            
            break;
}
		
		//-----------------------------
		//Output Variable --> Return FinalValue
		//-----------------------------		
		return res;	
	}

	//-------------------------------------------------------------------
	// 3. biggerMyList --> Filters all elements in MyList bigger than e
	//-------------------------------------------------------------------	
	/**
	 * The function filters all elements of MyList being bigger than 'e'  
	 * @param m: The MyList we want to check.
	 * @param e: The number 'e' we want to compare each element of MyList to.
	 * @return: The new MyList containing just the elements being bigger or equal than 'e'  
	 */	
	public MyList<Integer> biggerEqualMyList(MyList<Integer> m, int e){
		//-----------------------------
		//Output Variable --> InitialValue
		//-----------------------------
		MyList<Integer> res = null;

		//-----------------------------
		//SET OF OPS
		//-----------------------------

		//-----------------------------
		// I. SCENARIO IDENTIFICATION
		//-----------------------------
		int scenario = 0; 			
		
		//-----------------------------
		// II. SCENARIO IMPLEMENTATION 
		//-----------------------------
		switch(scenario){	
		case 1:
            break;
        case 2:
            int x = 0;
            for (int i=0; i < m.length(); i++){
                if (m.getElement(i) >= e){
                    res.addElement(x, m.getElement(i));
                    x++;
                }
            }
            break;
		}
		
		//-----------------------------
		//Output Variable --> Return FinalValue
		//-----------------------------		
		return res;	
	}
		
	//-------------------------------------------------------------------
	// 4. concatenate --> It concatenates 2 MyList   
	//-------------------------------------------------------------------	
	/**
	 * The function concatenates the content of 2 MyList.   
	 * @param m1: The first MyList.
	 * @param m2: The second MyList.
	 * @return: The new MyList resulting of concatenate the other 2 MyList
	 */	
	public MyList<Integer> concatenate(MyList<Integer> m1, MyList<Integer> m2){
		//-----------------------------
		//Output Variable --> InitialValue
		//-----------------------------
		MyList<Integer> res = null;

		//-----------------------------
		//SET OF OPS
		//-----------------------------

		//-----------------------------
		// I. SCENARIO IDENTIFICATION
		//-----------------------------
		int scenario = 0; 		
		
		//Rule 1
		if(m1.length() == 0 && m2.length() == 0){
            scenario=1;
        }
		
        else{
            scenario=2;
        }
		//-----------------------------
		// II. SCENARIO IMPLEMENTATION 
		//-----------------------------
			
		switch(scenario){	
		case 1:
			break;
		
		case 2:
			
		}
			
		//-----------------------------
		//Output Variable --> Return FinalValue
		//-----------------------------		
		return res;	
	}}
	
