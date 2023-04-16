package com.koubae.app1;

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
        simple_scanner();
        scanner_try_catch();
        scanner_try_catch_with_resource();
        scanner_try_catch_with_resource_final();
    }

    public static void simple_scanner()
    {
        Scanner reader = new Scanner(System.in);
        System.out.print(">>> username: ");
        String username = reader.nextLine();
        System.out.format("Hello %s\n", username);

        System.out.print(">>> Enter a number: ");
        int num1 = reader.nextInt();
        System.out.format("Entered %d\n", num1);
        reader.skip("\n"); // "((?<!\\R)\\s)*" skip whitespace, stopping after any newline
        if (reader.hasNextLine()) {
            System.out.print(">>> Enter a string: ");
            String string1 = reader.nextLine();
            System.out.format("string1 = %s\n", string1);
        }
    }

    public static void scanner_try_catch()
    {
        Scanner reader = new Scanner(System.in);

        System.out.print(">>> username: ");
        try {
            if (reader.hasNextLine()) {
                String username = reader.nextLine();
                System.out.format("Hello %s", username);
            }
        } catch (NoSuchElementException | IllegalStateException error) {
            System.out.println("Error while reading scanner");
            error.printStackTrace();
        } finally {
            reader.close();
        }
    }

    public static void scanner_try_catch_with_resource()
    {
        try (Scanner reader = new Scanner(System.in)) {
            System.out.print(">>> username: ");
            if (reader.hasNextLine()) {
                String username = reader.nextLine();
                System.out.format("Hello %s", username);
            }
        } catch (NoSuchElementException | IllegalStateException error) {
            System.out.println("Error while reading scanner");
            error.printStackTrace();
        }
    }

    public static void scanner_try_catch_with_resource_final()
    {
        String fileName = "output.txt";
        final Scanner readerTerminal = new Scanner(System.in);
        try (
                readerTerminal;
                PrintWriter writer = new PrintWriter("output.txt");
        ) {
            System.out.print(">>> username: ");
            if (readerTerminal.hasNextLine()) {
                String username = readerTerminal.nextLine();
                System.out.format("Hello %s", username);

                writer.write(username);
            }
        } catch (FileNotFoundException error) {
            System.out.format("File %s not found, reason: %s", fileName, error);
            error.printStackTrace();
        } catch (NoSuchElementException | IllegalStateException error) {
            System.out.format("Error while reading scanner, reason: %s", error);
            error.printStackTrace();
        } catch (Exception error) {
            System.out.format("Something went wrong while reading scanner, reason: %s", error);
            error.printStackTrace();
        }
    }

}
