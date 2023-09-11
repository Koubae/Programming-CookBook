public class MainThreading {
    public static void main(String[] args) {
        System.out.printf("- [%s] Threading Example\n", Thread.currentThread().getName());

        Thread thread = new Thread() {
            @Override
            public void run() {
                String threadName = Thread.currentThread().getName();
                try {
                    System.out.printf("- [%s] start job\n", threadName);
                    for (int i = 0; i < 2; i ++) {
                        System.out.printf("- [%s] working on %d\n", threadName, i);
                        Thread.sleep(450);
                    }

                } catch (InterruptedException error) {
                    System.out.printf("- [%s] Error in thread, error %s\n", Thread.currentThread().getName(), error);
                }
            }
        };

        thread.start();

        Thread thread2 = new Thread(() -> System.out.println("Runing from thread " + Thread.currentThread().getName()));
        thread2.start();

        new Thread(() -> {
            String threadName = Thread.currentThread().getName();
            try {
                System.out.printf("- [%s] start job\n", threadName);
                for (int i = 0; i < 2; i ++) {
                    System.out.printf("- [%s] working on %d\n", threadName, i);
                    Thread.sleep(450);
                }

            } catch (InterruptedException error) {
                System.out.printf("- [%s] Error in thread, error %s\n", Thread.currentThread().getName(), error);
            }
        }).start();
        
        // one Liner
        new Thread(() -> System.out.println("Runing from thread " + Thread.currentThread().getName())).start();

    }
    
}
