/**
 * Simple Programs that show arrays in java
 * @docs https://docs.oracle.com/javase/tutorial/java/nutsandbolts/arrays.html
 * --- BUILD 
 * javac simple_array.java
 * 
 * --- RUN 
 * 
 * java Array
 * OUTPUTS:
 * 
Element at index 0: 100
Element at index 1: 200
Element at index 2: 300
Element at index 3: 400
Element at index 4: 500
Element at index 5: 600
Element at index 6: 700
Element at index 7: 800
Element at index 8: 900
Element at index 9: 1000
 */
class Array {
    public static void main(String[] args) {
        // declares an array of integers
        int[] anArray;

        // allocates memory for 10 integers
        anArray = new int[10];
            
        // initialize first element
        anArray[0] = 100;
        // initialize second element
        anArray[1] = 200;
        // and so forth
        anArray[2] = 300;
        anArray[3] = 400;
        anArray[4] = 500;
        anArray[5] = 600;
        anArray[6] = 700;
        anArray[7] = 800;
        anArray[8] = 900;
        anArray[9] = 1000;

        System.out.println("Element at index 0: "
                            + anArray[0]);
        System.out.println("Element at index 1: "
                            + anArray[1]);
        System.out.println("Element at index 2: "
                            + anArray[2]);
        System.out.println("Element at index 3: "
                            + anArray[3]);
        System.out.println("Element at index 4: "
                            + anArray[4]);
        System.out.println("Element at index 5: "
                            + anArray[5]);
        System.out.println("Element at index 6: "
                            + anArray[6]);
        System.out.println("Element at index 7: "
                            + anArray[7]);
        System.out.println("Element at index 8: "
                            + anArray[8]);
        System.out.println("Element at index 9: "
                            + anArray[9]);
    }
} 
