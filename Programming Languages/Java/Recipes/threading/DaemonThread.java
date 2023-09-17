public class DaemonThread {
    public static class Worker extends Thread {
        public Worker() {
            setDaemon(true);
        }

        public void run() {
            while (true) {
                System.out.println("Hello world");
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    break;
                }
            }
        }

    }

    public static void main(String[] args) throws InterruptedException {
        new Worker().start();
        for (int i = 0; i < 5; i++) {
            Thread.sleep(1000);
        }

    }

}
