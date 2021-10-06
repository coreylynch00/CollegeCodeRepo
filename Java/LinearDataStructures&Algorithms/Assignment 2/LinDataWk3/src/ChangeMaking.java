/**
* Classical Change making problem with an unlimited amount of coins of each type. <br> 
* Version 2: Selection function with more elaborated policy: First biggest-coin.<br> 
* Depending on the type of coins, it can lead to an optimal solution.<br>
* The class encapsulates all the functions of the Greedy schema<br>
*/

public class ChangeMaking {

	//---------------------------------------
	//	Constructor
	//---------------------------------------
	/**
	 * Constructor of the class. Do not edit it.
	 */
	public ChangeMaking(){}

	
	// -------------------------------------------------------------------
	// 1. selectionFunctionFirstCandidate--> It selects the first candidate 
	// -------------------------------------------------------------------
	/**
	 * Given a current solution that is not a final solution, this function
	 * selects the new candidate to be added to it.<br>
	 * The policy followed is very simple: Just pick the first unused item.
	 * 
	 * @param candidates:
	 *            The MyList stating whether a candidate has been selected so
	 *            far or not.
	 * @return: The index of first candidate to be selected.
	 */
	public int selectionFunctionFirstCandidate(MyList<Integer> candidates) {//no limit to the amount of times you can choose a coin; all candidates can be considered at all times.

		//TO-DO
		return candidates.getElement(0);
	}

		
	//-------------------------------------------------------------------
	// 1. selectionFunction --> It selects the next candidate to be considered.  
	//-------------------------------------------------------------------	
	/**
	 * Given a current solution that is not a final solution, this function selects the new candidate to be added to it.<br> 
	 * The policy followed is more elaborated: Pick the best (largest) coin according to the objective function of minimizing the number
	 * of coins that make the change of the amount. 
	 * @param candidates: List of candidates
	 * @return: The index of candidate to be selected.
	 */	
	public int selectionFunctionBestCandidate(MyList<Integer> coinValues, MyList<Integer> candidates ){//no limit to the amount of times you can choose a coin; all candidates can be considered at all times.
		
			//TO-DO
		MyList<Integer> m1 = new MyDynamicList<Integer>();
        int res = 0;
        for(int i = 0; i < coinValues.length(); i++){
           if(res < coinValues.getElement(i)){
               res = coinValues.getElement(i);
           }
        }
        return res;
	}
	
	//-------------------------------------------------------------------
	// 2. feasibilityTest --> It selects if a candidate can be added to the solution.  
	//-------------------------------------------------------------------	
	/**
	 * Given a current solution and a selected candidate, this function 
	 * states whether the candidate must be added to the solution or discarded.<br> 
	 * @param candidateValue: The value of the candidate coin selected. 
	 * @param amount: The amount of change we want to generate.
	 * @param changeGenerated: The quantity of change we have generated so far. 
		 * @return: Whether the candidate fits or not into the solution.
	 */	

	public boolean feasibilityTest(int candidateValue, int amount, int changeGenerated){
		
			//TO-DO
		return true;
	}
	
	// -------------------------------------------------------------------
	// 5. solutionTest --> It selects if the current solution is the final
	// solution
	// -------------------------------------------------------------------
	/**
	 * Given a current solution, this function states whether it is a final
	 * solution or it can still be improved.<br>
	 * To determine it, it checks whether there is (at least) one item not
	 * picked before that fits into the knapsack.
	 * 
	 * @param nbCandidates:
	 *            number of candidates that have not been yet selected by the
	 *            selection function
	 * @return: Whether the current solution is the final solution.
	 */
	public boolean solutionTest(MyList<Integer> candidates) {

			//TO-DO
		if(candidates.length()!=0)
        	return false;
	}


	//-------------------------------------------------------------------
	// 4. objectiveFunction --> This function computes the value of the final solution.  
	//-------------------------------------------------------------------	
	/**
	 * Given the final solution to the problem, this function 
	 * computes its objective function value according to:<br>
	 * How many coins are used in the solution.<br>
	 * @param sol: The MyList containing the solution to the problem. 
	 * @return: The objective function value of such solution.
	 */	
	public int  objectiveFunction(MyList<Integer> sol){
		
			//TO-DO
		if(sol.length()>5){
            return 0;
        }
        else
            return 1;
	}
	
	//-------------------------------------------------------------------
	// 5. solve --> This function solves the problem using a greedy algorithm.  
	//-------------------------------------------------------------------	
	/**
	 * Given an instance of the GP1 problem, this function solves it using 
	 * a greedy algorithm.<br> 
	 * @param typeSelectFunc:
	 *            Type of selection function to choose.
	 * @param coinValues: A MyList containing the value of each type of coin supported. 
	 * @param amount: The amount of change we want to generate.
	 * @return: A MyList containing the amount of coins of each type being selected.
	 */	
	public MyList<Integer> solve(int typeSelectFunc, MyList<Integer> coinValues, int amount){
			//TO-DO
        MyList<Integer> m1 = new MyDynamicList<Integer>();
        
        if(coinValues.length() == 0){
            System.out.println("Null");
        }
        
        else
        int x = 0;
        int sec = 0;
        int amount = 0;
        int z = 0;
            while(amount>0){
            	if(selectionFunctionBestCandidate(coinValues) < amount){
                     amount = amount - selectionFunctionBestCandidate(coinValues);
                     m1.addElement(z, selectionFunctionBestCandidate(coinValues));
                     z++;
                }
                 else
                    for(int x = (coinValues.length()-1); x >= 0; x--){
                      if(coinValues.getElement(x)<amount){
                         amount = amount + selectionFunctionBestCandidate(coinValues);
                         m1.addElement(z, coinValues.getElement(x));
                         z++;
                            }
                       }
        break;             
        }                          
        }
        for(int i=0;i<m1.length();i++){
            
            System.out.println(m1.getElement(i));
        }   
             
return m1;
	}	
}
