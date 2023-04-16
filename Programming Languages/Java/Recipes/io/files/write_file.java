// 1
package com.koubae.app1;


import java.io.*;
import java.nio.charset.StandardCharsets;

public class Main
{
    public static void main( String[] args ) {
        String fileName = "sample.txt";
        
        try (Writer writer = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(fileName), StandardCharsets.UTF_8))) {
            writer.write("text to write\n");
            writer.write("text to write 2\n");
        }
        catch (IOException error) {
            System.err.format("Error while writing to file %s, error %s\n", fileName, error);
            error.printStackTrace();
        }


    }

}
// append 1
package com.koubae.app1;


import java.io.*;
import java.nio.charset.StandardCharsets;

public class Main
{
    public static void main( String[] args ) {
        String fileName = "sample.txt";

        try (Writer writer = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(fileName, true), StandardCharsets.UTF_8))) {
            writer.write("text to write\n");
            writer.write("text to write 2\n");
        }
        catch (IOException error) {
            System.err.format("Error while writing to file %s, error %s\n", fileName, error);
            error.printStackTrace();
        }


    }

}


// append 2
package com.koubae.app1;


import java.io.*;

public class Main
{
    public static void main( String[] args ) {
        String fileName = "sample.txt";

        try (Writer writer = new BufferedWriter(new FileWriter(fileName, true))) {
            writer.write("text to write\n");
            writer.write("text to write 2\n");
        }
        catch (IOException error) {
            System.err.format("Error while writing to file %s, error %s\n", fileName, error);
            error.printStackTrace();
        }


    }

}
