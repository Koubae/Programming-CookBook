
package com.waves;

import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.HashSet;
import java.util.logging.Logger;

import static com.waves.Arguments.MAX_VALUE;
import static com.waves.Arguments.MV;

public class App {

    final String LOG_FORMAT_SYSTEM = "java.util.logging.SimpleFormatter.format";
    final String LOG_FORMAT = "[%1$tF %1$tT] [%4$-1s] %5$s %n";

    final int REVOLUTION_MAX = 10_000;
    final int REVOLUTION_MIN = 1;
    final int REVOLUTION_DEFAULT = 100;
    private static Logger log = null;

    private int maxValue = 10;
    private int minValue = 1;
    private int revolutions = REVOLUTION_DEFAULT;

    private boolean withFace = false;
    public App() {
        setup();
    }


    public static void main(String[] args) {
        App app = new App();

        log.info("Total arguments called " + args.length);
        log.info("Arguments are: " + Arrays.toString(args));

        // Now map the arguments
        HashMap<String, String> argsMap = app.mapCliArgs(args);
        log.info("Arguments Mapped: ");
        app.setApp(argsMap);

        System.out.println("Min Value -> " + app.minValue);
        System.out.println("Max Value -> " + app.maxValue);
        System.out.println("Revolutions -> " + app.revolutions);
        app.runApp();
    }

    private void runApp() {

        for (int i = 0; i < revolutions; i++) {


            for (int y = 0; y < maxValue + 1; y++) {
                int startN = 0;
                while (startN < y) {
                    System.out.print("*");
                    startN ++;
                }
                if (y+1 != maxValue+1)
                    System.out.print('\n');
            }
            if (withFace)
                System.out.print("  :)  ");
            System.out.print('\n');

            for (int alpha = maxValue; alpha > 0; alpha --) {

                int startN = alpha;
                while (startN > 0) {
                    System.out.print("*");
                    startN --;
                }
                if (alpha == maxValue)
                    if (withFace)
                        System.out.print("  :)  ");
                System.out.print('\n');
            }
            System.out.print('\n');
        }
    }

    public void setup() {
        System.setProperty(LOG_FORMAT_SYSTEM, LOG_FORMAT);
        log =  Logger.getLogger(App.class.getName());
    }

    private void setApp(HashMap<String, String> argsMap) {
        if (argsMap.size() == 0) {
            return;
        }
        // Loop Through each key-value pair and set up the app
        for(Map.Entry<String, String> entry : argsMap.entrySet()) {
            try {
                Arguments key = Arguments.valueOf(entry.getKey()); // Convert Enum to a string
                String value = entry.getValue();

                switch (key) {

                    case MAX_VALUE:
                    case MV:
                        maxValue = Integer.parseInt(value);
                        break;
                    case MIN_VALUE:
                    case MIV:
                        minValue = Integer.parseInt(value);
                        break;

                    case REVOLUTIONS:
                    case R:
                        revolutions = Integer.parseInt(value);
                        break;

                    case FACE:
                        withFace = Boolean.parseBoolean(value);
                        break;

                    default:
                        break;
                }
            } catch (IllegalArgumentException e) {
                log.warning(e.getMessage());
            }
        }

        // Check integrity of the app's Value
        if (maxValue <= 0)
            maxValue = 10;
        if (minValue <= 0)
            minValue = 1;
        if (maxValue <= minValue)
            maxValue = maxValue + 2;
        if (minValue >= maxValue) {
            minValue = minValue - 2;
        }

        // Check the revolution don't exceed min and max
        if (revolutions < REVOLUTION_MIN)
            revolutions = REVOLUTION_DEFAULT;
        if (revolutions > REVOLUTION_MAX)
            revolutions = REVOLUTION_MAX;

    }

    private HashMap<String, String> mapCliArgs(String[] args) {
        HashMap<String, String> argsMap = new HashMap<>();

        Set<String> arguments = new HashSet<>();
        arguments.add(String.valueOf(MAX_VALUE));
        arguments.add(String.valueOf(Arguments.MV));

        arguments.add(String.valueOf(Arguments.MIN_VALUE));
        arguments.add(String.valueOf(Arguments.MIV));

        arguments.add(String.valueOf(Arguments.REVOLUTIONS));
        arguments.add(String.valueOf(Arguments.R));

        arguments.add(String.valueOf(Arguments.FACE));

        String lastKey = null;
        for (String arg: args) {
            arg = arg.toLowerCase();
            if (arg.contains("-") || arg.contains("--")) { // Then we have a key value
                arg = arg.replaceFirst("^--", "").replaceFirst("^-", ""); // clean up flags
                arg = arg.replace("-", "_").toUpperCase();
                if (!arguments.contains(arg)) // Skip if not in HasSet with Enum
                    continue;
                lastKey = arg; // fill up the new key
                continue;
            }
            // Here we have a value
            if (lastKey == null || argsMap.containsKey(lastKey))
                continue;
            arg = arg.replace("-", "_").toUpperCase();
            argsMap.put(lastKey, arg); // Add key to value

        }

        return argsMap;
    }
}
