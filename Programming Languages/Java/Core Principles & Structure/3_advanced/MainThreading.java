public class MainThreading {
    public static void main(String[] args) {
        System.out.printf("- [%s] Threading Example\n", Thread.currentThread().getName());

        Thread thread = new Thread() {
            @Override
            public void run() {
                String threadName = Thread.currentThread().getName();
                try {
                    System.out.printf("- [%s] start job\n", threadName);
                    for (int i = 0; i < 10; i ++) {
                        System.out.printf("- [%s] working on %d\n", threadName, i);
                        Thread.sleep(450);
                    }

                } catch (InterruptedException error) {
                    System.out.printf("- [%s] Error in thread, error %s\n", Thread.currentThread().getName(), error);
                }
            }
        };

        thread.start();


    }
    
}
