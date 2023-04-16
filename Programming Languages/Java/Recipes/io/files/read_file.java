package com.koubae.app1;


import com.koubae.app1.utils.TerminalReader;

import java.io.*;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Hello world!
 *
 */
public class Main
{
    public static void main( String[] args ) throws IOException {
        TerminalReader userInput = new TerminalReader();

//        String userName = userInput.input(">>> username: ");
//        int userId = userInput.input(">>> user-id: ", 0);
//        boolean enable = userInput.input(">>> Enable feature ? : ", true);

        String userName = "user001";
        int userId = 89219;
        boolean enable = true;

        System.out.format("Welcome %s (%d) - %s!\n", userName, userId, enable);

        String fileStorageName = "storage.txt";
        System.out.format("Content of file %s\n", fileStorageName);

        String rootPath = new File(".").getCanonicalPath();
        Path storagePath = Paths.get(rootPath, "storage");
        Path dataStoredPath = Paths.get(storagePath.toString(), fileStorageName);

        try (
            BufferedReader readBuff = new BufferedReader(new FileReader(dataStoredPath.toFile()))
        )  {

            String output = "";
            String line;
            while ((line = readBuff.readLine()) != null) output += line + "\n";
            System.out.format("%s\n", output);

        } catch (FileNotFoundException error) {
            System.err.format("File %s not found! Error : %s", fileStorageName, error);
            error.printStackTrace();
        } catch (IOException error) {
            System.err.format("I/O Exception while reading file %s Error : %s", fileStorageName, error);
            error.printStackTrace();
        } catch (Exception error) {
            System.err.format("Exception while reading file %s Error : %s", fileStorageName, error);
            error.printStackTrace();
        }


    }


}