import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.concurrent.ArrayBlockingQueue;

public class PythonConsoleQueue {
    public static void main(String[] args) throws IOException {
        String[] commands = {"python", "-i"};  // -i for Interactive IS ESSENTIAL! I spent some times for this..
        ProcessBuilder builder = new ProcessBuilder(commands);
        builder.redirectErrorStream(true);
        Process process = builder.start();

        ArrayBlockingQueue<String> queue = new ArrayBlockingQueue<>(10);
        threadPipeOut(process);
        threadPipeIn(process, queue);

        try {
            queue.put("print('Hello world');");
            queue.put("print('Hello world');");
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }

    }

    private static void threadPipeIn(Process process, ArrayBlockingQueue<String> queue) {
        Thread job = new Thread(() -> {
            BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(process.getOutputStream()));
            while (true) {
                try {
                    String command = queue.take();
                    writer.write(command);
                    writer.newLine();
                    writer.flush();
                } catch (IOException | InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });
        job.start();
    }

    private static void threadPipeOut(Process process) {
        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
        Thread job = new Thread(() -> {
            String line;
            try {
                while ((line = reader.readLine()) != null) {
                    System.out.println(line.replace(">>> ", "").replace("... ", ""));
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        });
        job.start();
    }

}