// https://dev.java/learn/generics/intro/
/*
-- Type Parameter Naming Conventions

By convention, type parameter names are single, uppercase letters. This stands in sharp contrast to the variable naming conventions that you already know about, and with good reason: without this convention, it would be difficult to tell the difference between a type variable and an ordinary class or interface name.

The most commonly used type parameter names are:

    E - Element (used extensively by the Java Collections Framework)

    K - Key

    N - Number

    T - Type

    V - Value

    S, U, V etc. - 2nd, 3rd, 4th types

    You will see these names used throughout the Java SE API and the rest of this section.

Type Parameter and Type Argument Terminology:
 Many developers use the terms "type parameter" and "type argument" interchangeably, but these terms are not the same. When coding,
  one provides type arguments in order to create a parameterized type. Therefore, the T in Foo<T> is a type parameter and the String in Foo<String> f is a type argument. 
This section observes this definition when using these terms.

*/
class Main {
    public static void main(String... args) {
        List<String> list = new ArrayList<String>();
        list.add("hello");
        String s = list.get(0);   // no cast

    }
}

/**
 * Generic version of the Box class.
 * @param <T> the type of the value being boxed
 */
public class Box<T> {
    // T stands for "Type"
    private T t;

    public void set(T t) { this.t = t; }
    public T get() { return t; }
}


// Multiple Type Parameters
public interface Pair<K, V> {
    public K getKey();
    public V getValue();
}

public class OrderedPair<K, V> implements Pair<K, V> {

    private K key;
    private V value;

    public OrderedPair(K key, V value) {
    this.key = key;
    this.value = value;
    }

    public K getKey()    { return key; }
    public V getValue() { return value; }
}

class Main {
    public static void main(String... args) {
        Pair<String, Integer> p1 = new OrderedPair<String, Integer>("Even", 8);
        Pair<String, String>  p2 = new OrderedPair<String, String>("hello", "world");

        // compiler infer via diamon notation
        OrderedPair<String, Integer> p1 = new OrderedPair<>("Even", 8);
        OrderedPair<String, String>  p2 = new OrderedPair<>("hello", "world");

        OrderedPair<String, Box<Integer>> p = new OrderedPair<>("primes", new Box<Integer>(...));


    }
}


// Raw types
public class Box<T> {
    public void set(T t) { /* ... */ }
    // ...
}
class Main {
    public static void main(String... args) {
       // Using parameteriezed type
       Box<Integer> intBox = new Box<>();
       // raw type 
       Box rawBox = new Box();

    }
}


// --  type inference

public class Util {
    public static <K, V> boolean compare(Pair<K, V> p1, Pair<K, V> p2) {
        return p1.getKey().equals(p2.getKey()) &&
               p1.getValue().equals(p2.getValue());
    }
}

public class Pair<K, V> {

    private K key;
    private V value;

    public Pair(K key, V value) {
        this.key = key;
        this.value = value;
    }

    public void setKey(K key) { this.key = key; }
    public void setValue(V value) { this.value = value; }
    public K getKey()   { return key; }
    public V getValue() { return value; }
}


class Main {
    public static void main(String... args) {
        Pair<Integer, String> p1 = new Pair<>(1, "apple");
        Pair<Integer, String> p2 = new Pair<>(2, "pear");
        boolean same = Util.<Integer, String>compare(p1, p2);

        Pair<Integer, String> p1 = new Pair<>(1, "apple");
        Pair<Integer, String> p2 = new Pair<>(2, "pear");
        boolean same = Util.compare(p1, p2);



    }
}

// -- Bounded Type Parameters
public class Box<T> {

    private T t;          

    public void set(T t) {
        this.t = t;
    }

    public T get() {
        return t;
    }

    public <U extends Number> void inspect(U u){
        System.out.println("T: " + t.getClass().getName());
        System.out.println("U: " + u.getClass().getName());
    }

    public static void main(String[] args) {
        Box<Integer> integerBox = new Box<Integer>();
        integerBox.set(new Integer(10));
        integerBox.inspect("some text"); // error: this is still String!
    }
}

/*
<T extends B1 & B2 & B3>

Class A { /* ... */ }
interface B { /* ... */ }
interface C { /* ... */ }

class D <T extends A & B & C> { /* ... */ }

class D <T extends B & A & C> { /* ... */ }  // compile-time error

*/
