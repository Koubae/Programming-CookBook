import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Scanner;

public class PythonConsole {
    public static void main(String[] args) throws IOException {
        String[] commands = {"python", "-i"};  // -i for Interactive IS ESSENTIAL! I spent some times for this..
        ProcessBuilder builder = new ProcessBuilder(commands);
        builder.redirectErrorStream(true);
        Process process = builder.start();

        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(process.getOutputStream()));

        new Thread(() -> {
            String read;
            try {
                while ((read = reader.readLine()) != null) {
                    System.out.println(read.replace(">>> ", "").replace("... ", ""));
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
