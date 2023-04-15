public class generics_01 {
    
}
/**
 * @docs https://developer.ibm.com/tutorials/java-language-constructs-2/
 */

import org.jetbrains.annotations.NotNull;

import java.util.ArrayList;
import java.util.List;

import java.util.logging.Logger;

public class Main {

    private static final Logger log = Logger.getLogger(Main.class.getName());

    public static void main(String[] args)
    {
        int x = 0;
        System.out.println(x);
        System.out.println("Hello world!");
        System.out.println("Hello world!");

        listing5();
        iteratingWithGenerics();
    }

    public static void listing5() {
        ArrayList<String> arrayList = new ArrayList<>(); // Generic
        arrayList.add("A String");
        // TODO: Uncomment next line to see compile error
        // arrayList.add(Integer.valueOf(10));// compiler error!
        arrayList.add("Another String");
        log.info("Added " + arrayList.size() + " objects to arrayList");
        // So far, so good.
        // Process the ArrayList
        for (int aa = 0; aa < arrayList.size(); aa++) {
            String s = arrayList.get(aa); // No cast necessary
            log.info("String from ArrayList" + s);
        }
    }

    public static void iteratingWithGenerics() {
        ArrayList<String> arrayList = new ArrayList<>();
        arrayList.add("A String");
        // TODO: Uncomment next line to see compile error
        // arrayList.add(Integer.valueOf(10));// compiler error!
        arrayList.add("Another String");
        log.info("Added " + arrayList.size() + " objects to arrayList");
        // So far, so good.
        // Process the ArrayList

    }

    // Generic Method
    public <E> String formatArray(E @NotNull [] arrayToFormat) {
        StringBuilder sb = new StringBuilder();

        int index = 0;
        for (E element : arrayToFormat) {
            if (index > 0)
                sb.append(", ");
            sb.append("Element ");
            sb.append(index++);
            sb.append(" => ");
            sb.append(element);
        }

        return sb.toString();
    }

}

// Generic Class
class SimpleList<E> {
    private List<E> backingStore;

    public SimpleList() {
        backingStore = new ArrayList<E>();
    }

    public E add(E e) {
        if (backingStore.add(e))
            return e;
        else
            return null;
    }

    public int size() {
        return backingStore.size();
    }

    public void clear() {
        backingStore.clear();
    }
}