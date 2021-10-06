//Corey Lynch - R00154863 - SD2-A

import java.util.Collections;

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
	// 1. maxInt --> Computes the maximum item of MyList 
	//-------------------------------------------------------------------	
	/**
	 * The function computes the maximum item of m (-1 if m is empty). 
	 * @param m: The MyList we want to compute its maximum item.
	 * @return: The maximum item of MyList	  
	 */	
	public int maxInt(MyList<Integer> m){
			 // TO-DO
		int res = -1;
		
		//SCENARIOS
		int scenario = 0;
		
		//Rule 1: MyList is empty
		if (m.length() == 0)
			scenario = 1;
		
		//Rule 2: MyList is not empty
		else
			scenario = 2;
		
		//SCENARIO IMPLEMENTATION
		switch(scenario) {
		
		//Rule 1:
		case 1:
			return res;	
		
		//Rule 2:
		case 2:
		    int max = Integer.MIN_VALUE;
		    for(int i = 0; i < m.length(); i++){
		        if(m.getElement(i) > max){
		            max = m.getElement(i);
		        }
		    }
		    return max;
		}
		return scenario;
	}

	//-------------------------------------------------------------------
	// 2. isReverse --> Computes if MyList is sorted in decreasing order 
	//-------------------------------------------------------------------	
	/**
	 * The function computes whether m is sorted in decreasing order or not.  
	 * @param m: The MyList we want to check.
	 * @return: Whether m is sorted in decreasing order or not.  
	 */	
	public boolean isReverse(MyList<Integer> m){
			 // TO-DO
		boolean res = true;
		
		//SCENARIOS
		int scenario = 0;
		
		//Rule 1: MyList is empty
		if (m.length() == 0)
			scenario = 1;
		
		//Rule 2: MyList is not empty
		else
			scenario = 2;
		
		//SCENARIO IMPLEMENTATION
		switch(scenario) {
		
		//Rule 1:
		case 1:
			res = false;
			break;
		
		//Rule 2:
		case 2:
			int e0 = m.getElement(0);
			int e1 = m.getElement(1);
			
			if (e0 <= e1) {
				res = false;
		}
			else
				res = true;
		}
		return res;
	}
	
	/*
	 * public static boolean isSorted(MyList<Integer> m, int index) {
			    if (index < 2) {
			        return true;
			    } else if (m.getElement(index - 2).compareTo(m.getElement(index - 1)) > 0) {
			        return false;
			    } else {
			        return isSorted(m, index - 1);
	 */

	//-------------------------------------------------------------------
	// 3. getNumAppearances --> Computes the amount of times that integer appears in MyList  
	//-------------------------------------------------------------------	
	/**
	 * The function computes the amount of times that the integer n appears in m.   
	 * @param m: The MyList we want to use.
	 * @param n: The number we want to compute its appearances for.
	 * @return: The amount of appearances of n into m  
	 */	
	public int getNumAppearances(MyList<Integer> m, int n){
			 // TO-DO
		int res = -1;
		
		//SCENARIOS
		
		int scenario = 0;
		
		//Rule 1: MyList is empty
		if (m.length() == 0)
			scenario = 1;
		
		//Rule 2: MyList not empty
		else
			scenario = 2;
		
		//SCENARIO IMPLEMENTATION
		switch(scenario) {
		
		//Rule 1:
		case 1:
			res = -1;
			break;
		
		//Rule 2:
		case 2:
			for (int i=0; i < m.length(); i++) {
				if (m.getElement(i) == n) {
					res++;
				}
			}
		}	
		
		return res;
	}
	
	//-------------------------------------------------------------------
	// 4. power --> Computes the m-est power of n
	//-------------------------------------------------------------------	
	/**
	 * The function computes n to the power of m.
	 * @param n: The base number.
	 * @param m: The power of n we want to compute
	 * @return: n to the power of m.  
	 */	

	public int power(int n, int m){
		 // TO-DO
		//Not sure how I can use switch statements for this function so I left them out...
		
		int x = 1;	//Assign initial value of 1
		for (int i = 1; i <= m; i++) {
			x = x * n;
		}
		
		return x;
		
	}
	
	//-------------------------------------------------------------------
	// 5. lucas --> Computes the n-est term of the Lucas series
	//-------------------------------------------------------------------	
	/**
	 * The function computes the n-est term of the Lucas series
	 * @param n: The n-est term of the series we want to compute
	 * @return: The term being computed 
	 */	
	public int lucas(int n){
		 // TO-DO
		
		if (n == 0) {
			return 2;
		}
		else if(n == 1) {
			return 1;
		}
		else
			return lucas(n-1) + lucas(n-2);
	}

	//-------------------------------------------------------------------
	// 6. drawImage --> Prints a pattern of a given length
	//-------------------------------------------------------------------	
	/**
	 * The function prints prints a pattern of a given length.
	 * *
	 * **
	 * ***
	 * ... 
	 * @param n: The length of the desired pattern
	 */	
	public void drawImage(int n){
			 // TO-DO
		for(int i = 0; i < n; i++) {
			for (int x = 0; x < i; x++) {
				System.out.print("*");
			}
		}
	}
		
}
