

import java.util.Arrays;
import java.util.logging.Logger;


public class App {

    final String LOG_FORMAT_SYSTEM = "java.util.logging.SimpleFormatter.format";
    final String LOG_FORMAT = "[%1$tF %1$tT] [%4$-1s] %5$s %n";
    private static Logger log = null;

    public App() {
        setup();
    }


    public static void main(String[] args) {
        App app = new App();

        log.info("Args " + args.length);
        log.info("Args " + args.length);


        System.out.println(Arrays.toString(args));
    }

    public void setup() {
        System.setProperty(LOG_FORMAT_SYSTEM, LOG_FORMAT);
        log =  Logger.getLogger(App.class.getName());
    }
}
