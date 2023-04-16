package com.koubae.app1;

import java.util.Scanner;

class TerminalReader {
    private final Scanner reader;

    TerminalReader() {
        this.reader = new Scanner(System.in);
    }

    public String input()
    {
        return _inputString();
    }

    public String input(String message)
    {
        System.out.print(message);
        return _inputString();
    }

    public int input(int ignored__)
    {
        return _inputInt();
    }

    public int input(String message, int ignored__)
    {
        System.out.print(message);
        return _inputInt();
    }

    public boolean input(boolean ignored__)
    {
        return _inputBoolean();
    }

    public boolean input(String message, boolean ignored__)
    {
        System.out.print(message);
        return _inputBoolean();
    }


    private String _inputString()
    {
        String output = "";
        if (reader.hasNextLine()) {
            output = reader.nextLine();
        }
        return output;
    }

    private int _inputInt()
    {
        int output = 0;
        if (reader.hasNextInt()) {
            output = reader.nextInt();
        }
        return output;
    }

    private boolean _inputBoolean()
    {
        boolean output = false;
        if (reader.hasNextBoolean()) {
            output = reader.nextBoolean();
        }
        return output;
    }


}


package com.koubae.app1;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;
import java.util.NoSuchElementException;
import java.lang.IllegalStateException;



/**
 * Hello world!
 *
 */
public class Main
{
    public static void main( String[] args )
    {
        TerminalReader userInput = new TerminalReader();

        String inputString1 = userInput.input();
        String inputString2 = userInput.input(">>> username: ");
        int inputInt3 = userInput.input(">>> Int value: ", 0);




//        final Scanner readerUserTerminal = new Scanner(System.in);
//        try {
//            System.out.print(">>> username: ");
//            if (readerUserTerminal.hasNextLine()) {
//                String username = readerUserTerminal.nextLine();
//                System.out.format("Hello %s", username);
//            }
//        } catch (NoSuchElementException | IllegalStateException error) {
//            System.out.format("Error while reading scanner, reason: %s", error);
//            error.printStackTrace();
//        } catch (Exception error) {
//            System.out.format("Something went wrong while reading scanner, reason: %s", error);
//            error.printStackTrace();
//        }


    }


}
