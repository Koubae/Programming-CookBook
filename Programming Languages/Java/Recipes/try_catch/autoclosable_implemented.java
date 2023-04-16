import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;
import java.util.NoSuchElementException;
import java.lang.IllegalStateException;



// normal autoclosable

public class Main
{
    public static class MyResource implements AutoCloseable {
        @Override
        public void close() throws Exception {
            System.out.println("Resource closed, let's call some resource ... ");
        }
    }

    public static void main( String[] args )
    {
        final MyResource resource1 = new MyResource();

        try (resource1; ) {
            System.out.println("Inside Try - catch block");
        } catch (Exception error) {
            error.printStackTrace();
        }

    }
}

// no try- catch
public class Main
{
    public static class MyResource implements AutoCloseable {
        @Override
        public void close() {
            System.out.println("Resource closed, let's call some resource ... ");
        }
    }

    public static void main( String[] args )
    {
        final MyResource resource1 = new MyResource();

        try (resource1; ) {
            System.out.println("Inside Try - catch block");
        }

    }
}

// still will close the resource if another error occurred
public class Main
{
    public static class MyResource implements AutoCloseable {
        @Override
        public void close() {
            System.out.println("Resource closed, let's call some resource ... ");
        }
    }

    public static void main( String[] args ) throws FileNotFoundException {
        final MyResource resource1 = new MyResource();

        try (resource1; ) {
            System.out.println("Inside Try - catch block");
            final Scanner readerTerminal = new Scanner(new File("dont_exits.txt"));
        }

    }
}