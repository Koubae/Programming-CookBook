package com.firstapp;


/**
 *
 * ----------------
 * Documentations
 * ----------------
 *
 * java.util.* https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/package-summary.html
 *
 * ----------------
 * StackOverflow
 * ----------------
 *
 * https://stackoverflow.com/questions/1200621/how-do-i-declare-and-initialize-an-array-in-java
 *
 */


import java.util.stream.IntStream;

// -------------------------------
// Standard Library Data-Structure
// -------------------------------
// Interfaces
import java.util.List;
import java.util.Set;
import java.util.Map;
// Classes
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.HashMap;


class ArraysLearn {

    public static void main(String[] args) {
        ArraysLearn app = new ArraysLearn();

        app.ArrayPrimitives();
        System.out.println();
        app.ListsPrimitives();
        System.out.println();
        app.ArrayList();
        System.out.println();
        app.SetExample();
        System.out.println();
        app.MapExample();
    }


    public void ArrayPrimitives() {
        // Primitives
        int[] intArray01 = new int[3];
        int[] intArray02 = {1, 2, 3};
        int[] intArray03 = new int[]{1, 2, 3};

        // Multidimension Array
        int[][] intArrayMulti01 = new int[5][2];
        intArrayMulti01[0][0]=1;
        intArrayMulti01[0][1]=2;
        intArrayMulti01[1][0]=1;
        intArrayMulti01[1][1]=2;
        intArrayMulti01[2][0]=1;
        intArrayMulti01[2][1]=2;
        intArrayMulti01[3][0]=1;
        intArrayMulti01[3][1]=2;
        intArrayMulti01[4][0]=1;
        intArrayMulti01[4][1]=2;
        System.out.println(intArrayMulti01.length);
        int[][] intArrayMulti02 ={ {1,2}, {1,2}, {1,2}, {1,2}, {1,2} };
        System.out.println(intArrayMulti02.length);


        // Primitives using IntStream  https://docs.oracle.com/javase/8/docs/api/java/util/stream/IntStream.html
        int[] intArrayStream01 = IntStream.range(0, 100).toArray(); // 0 -> 99
        int[] intArrayStream02 = IntStream.rangeClosed(0, 100).toArray(); // 0 -> 100
        int[] intArrayStream03 = IntStream.of(12,25,36,85,28,96,47).toArray(); // The order is preserved.
        int[] intArrayStream04 = IntStream.of(12,25,36,85,28,96,47).sorted().toArray(); // Sort

        for(int element: intArray01)
            System.out.print(element + ", ");
        System.out.print('\n');
        for(int element: intArray02)
            System.out.print(element + ", ");
        System.out.print('\n');
        for(int element: intArray03)
            System.out.print(element + ", ");
        System.out.print('\n');

        for(int[] i: intArrayMulti01)
            for(int y: i)
                System.out.print(y + ", ");
        System.out.print('\n');
        for(int[] i: intArrayMulti02)
            for(int y: i)
                System.out.print(y + ", ");
        System.out.print('\n');

        System.out.println(intArrayStream01.length);
        System.out.println(intArrayStream02.length);

        for(int element:  intArrayStream03)
            System.out.print(element + ", ");
        System.out.print('\n');
        for(int element:  intArrayStream04)
            System.out.print(element + ", ");

        /// String
        String[] intString01 = new String[3];
        String[] intString02 = {"a", "b", "c"};
        String[] intString03 = new String[]{"a", "b", "c"};
        String[] intString04; // Declaration
        intString04 = new String[]{"a", "b", "c"}; // Initialization
    }


    public void ListsPrimitives() {
        // Strings
        List<String> number = Arrays.asList("1", "2", "3");
        number.forEach(item -> System.out.print(item + " - "));
        System.out.println();
        // Integers
        List<Integer> numbers = Arrays.asList(1, 2, 3);
        numbers.forEach(item -> System.out.print(item + " - "));
        System.out.println();




    }

    public void ArrayList() {

        List<Integer> l1 = new ArrayList<Integer>();

        l1.add(0, 1);
        l1.add(1, 2);
        // Print the elements inside the object
        System.out.println(l1);

        // Add new ArrayList into l1
        List<Integer> l2 = new ArrayList<Integer>();
        l2.add(1);
        l2.add(2);
        l2.add(3);

        l1.addAll(1, l2); // Add l2 to l1 from index 1
        System.out.println(l1);
        // Removes element from index 1
        l1.remove(1);

        // Prints element at index 3 in list 1
        // using get() method
        System.out.println(l1.get(3));

        // Replace 0th element with 5
        // in List 1
        l1.set(0, 5);

        // Again printing the updated List 1
        System.out.println(l1);


        // ---------------------
        //  Iteration
        // ---------------------
        // for loop classic
        System.out.println("\n------------ Classic for-loop");
        for (int i = 0; i < l1.size(); i++) {
            System.out.print((String) (l1.get(i) + ", "));
        }
        System.out.println("\n------------ Enhanced for-loop");
        // enhanced for-loop
        for (Integer item: l1)
            System.out.print(item + ", ");
        // Using foreach calling stream classic
        System.out.println("\n------------ foreach: lambda classic");
        l1.stream().forEach(item -> System.out.print(item + ", "));
        // Using foreach
        System.out.println("\n------------ foreach: lambda");
        l1.forEach(item -> System.out.print(item + ", "));
        // Using foreach with method ::
        System.out.println("\n------------ foreach: lambda with Method call");
        l1.forEach(System.out::print);
    }

    public void SetExample() {
        System.out.println("\n------------ SetExamplel");
        Set<String> mySet = new HashSet<String>();
        // Adding Elements
        mySet.add("one");
        mySet.add("two");
        mySet.add("three");
        mySet.add("four");
        mySet.add("five");

        // Set follows unordered way.
        System.out.println(mySet);
    }

    public void MapExample() {
        Map<Integer, String> myMap = new HashMap<Integer, String>();

        myMap.put(100, "Val1");
        myMap.put(101, "Val2");
        myMap.put(102, "Val3");

        for (Map.Entry entry: myMap.entrySet()) {
            System.out.println(entry.getKey() + " -> " + entry.getValue());
        }

    }
}
