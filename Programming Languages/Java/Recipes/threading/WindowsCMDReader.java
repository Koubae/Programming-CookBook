import java.io.IOException;
import java.io.File;
import java.io.OutputStream;
import java.io.InputStream;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Scanner;

// @credit: https://stackoverflow.com/a/70156036/13903942
public class WindowsCMDReader {
    public static void main(String[] args) throws IOException {
        String[] commands = {"C:/windows/system32/cmd.exe"};
        ProcessBuilder builder = new ProcessBuilder(commands);
        builder.directory(new File("C:/windows/system32"));
        Process process = builder.start();

        OutputStream stdin = process.getOutputStream();
        InputStream stdout = process.getInputStream();
        InputStream stderr = process.getErrorStream();

        BufferedReader reader = new BufferedReader(new InputStreamReader(stdout));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(stdin));
        BufferedReader error = new BufferedReader(new InputStreamReader(stderr));

        new Thread(() -> {
            String read;
            try {
                while ((read = reader.readLine()) != null) {
                    System.out.println(read);
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }).start();

        new Thread(() -> {
            String read;
            try {
                while ((read = error.readLine()) != null) {
                    System.out.println(read);
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }).start();

        new Thread(() -> {
            while (true) {
                try {
                    Scanner scanner = new Scanner(System.in);
                    writer.write(scanner.nextLine());
                    writer.newLine();
                    writer.flush();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }).start();
    }
}
