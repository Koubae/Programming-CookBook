// @docs https://developer.ibm.com/tutorials/java-language-constructs-2/
import org.jetbrains.annotations.NotNull;

import java.io.*;
import java.util.List;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;


class Main {

    private static final Logger log = Logger.getLogger(Main.class.getName());

    public static void main(String[] args)  {
        Main m = new Main();

        List<String> result = m.readWordsUnbufferedStream("10Words.txt");

        result.forEach(item -> System.out.println("Element -> " + (String) item));
        result.forEach(System.out::println);

        // Now write the result into a new file
        int wordCount = m.saveWordsUnbufferedStream("newfile.txt", result);
        System.out.println("Total -> " + wordCount);
    }

    // Read into file
    public List<String> readWordsUnbufferedStream(String wordsFilename) {
        long startTime = System.currentTimeMillis();

        // Return value: list of strings
        List<String> ret = new ArrayList<>();

        File wordsFile = new File(wordsFilename);

        int numberOfWords = 0;
        try (InputStreamReader reader = new InputStreamReader(new FileInputStream(wordsFile))) {
            boolean done = false;
            // While there is more in the file to read
            while (!done) {
                int charRead = reader.read();
                if (charRead == -1) {
                    done = true;
                } else {
                    StringBuilder word = new StringBuilder();
                    // Read the current word (file has one word per line)
                    while (charRead != -1 && charRead != '\n' && charRead != '\r') {
                        word.append(charRead);
                        charRead = reader.read();
                    }
                    ret.add(word.toString());
                    numberOfWords++;
                }
            }
        } catch (IOException e) {
            log.log(Level.SEVERE, "IOException occurred, message = " + e.getLocalizedMessage(), e);
        }

        log.info("Read " + numberOfWords + " words in " + Long.toString(System.currentTimeMillis() - startTime) + "ms");

        return ret;

    }

    public int saveWordsUnbufferedStream(String filename, List<String> words) {
        long startTime = System.currentTimeMillis();

        // Return value: number of words written
        int wordCount = 0;

        File file = new File(filename);
        try (OutputStreamWriter writer = new OutputStreamWriter(new FileOutputStream(file))) {
            for (String word : words) {
                if (wordCount > 0) {
                    writer.append(' ');
                }
                writer.write(word);
                wordCount++;
            }
        } catch (IOException e) {
            log.log(Level.SEVERE, "IOException occurred, message = " + e.getLocalizedMessage(), e);
        }

        log.info("Wrote " + wordCount + " words in " + Long.toString(System.currentTimeMillis() - startTime) + "ms");

        return wordCount;
    }


    // Reading file buffered I/O
    public List<String> readWordsBufferedStream(String wordsFilename) {
        long startTime = System.currentTimeMillis();

        // Return value: list of strings
        List<String> ret = new ArrayList<>();

        File wordsFile = new File(wordsFilename);

        int numberOfWords = 0;
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(wordsFile)))) {
            String line = reader.readLine();
            // While there is more in the file to read
            while (line != null) {
                ret.add(line);
                numberOfWords++;
                line = reader.readLine();
            }
        } catch (IOException e) {
            log.log(Level.SEVERE, "IOException occurred, message = " + e.getLocalizedMessage(), e);
        }

        log.info("Read " + numberOfWords + " words in " + Long.toString(System.currentTimeMillis() - startTime) + "ms");

        return ret;

    }

    // Writing file buffered I/O
    public int saveWordsBufferedStream(String filename, @NotNull List<String> words) {
        long startTime = System.currentTimeMillis();

        // Return value: number of words written
        int wordCount = 0;

        File file = new File(filename);
        try (BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(file)))) {
            for (String word : words) {
                if (wordCount > 0) {
                    writer.append(' ');
                }
                writer.write(word);
                wordCount++;
            }
        } catch (IOException e) {
            log.log(Level.SEVERE, "IOException occurred, message = " + e.getLocalizedMessage(), e);
        }

        log.info("Wrote " + wordCount + " words in " + Long.toString(System.currentTimeMillis() - startTime) + "ms");

        return wordCount;
    }

}
