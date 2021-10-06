
/**
* The main class of our project.<br>. 
*/
public class MyMain {
	
	/**
	 * This function is used to test the divide and conquer algorithms.
	 */
	public static void test(){
		//1. We create extra variables for the tests
		
		// m1 = []
		MyList<Integer> m1 = new MyDynamicList<Integer>();
		
		// m2 = [5,20,1,10]
		MyList<Integer> m2 = new MyDynamicList<Integer>();
		m2.addElement(0, 5); 
		m2.addElement(1, 20);
		m2.addElement(2, 1);
		m2.addElement(3, 10);
		
		//3. We create extra variables for the results		
		MyList<Integer> resM = null;
		
		//---------------------
		// TESTS
		//---------------------		

		//----------------------------
		//1. We test ChangeMaking_1
		//----------------------------
		ChangeMaking ex1 = new ChangeMaking();

		for(int i=1; i<=2; i++)
		{
		
			switch(i){	
				case 1: 
					System.out.println("\n----------- Test: ChangeMaking with Dummy Selection Function -------------\n");
					break;
				case 2:
					System.out.println("\n----------- Test: ChangeMaking with Biggest Coin Selection Function -------------\n");
					break;
			}	
			
			System.out.println("The change of the amount 36 is:");
			resM = ex1.solve(i,m1, 36);
			System.out.println();
			
			System.out.println("The change of the amount 36 is:");
			resM = ex1.solve(i,m2, 36);
			System.out.println();
	
			System.out.println("The change of the amount 58 is:");
			resM = ex1.solve(i,m2, 58);
			System.out.println();
			
			System.out.println();		
		}
		
	}
	
	/**
	 * Main Method.
	 * @param args: We will run the program parameter free, so do not worry about it.
	 */
	public static void main(String[] args) {
		test();
	}

}
