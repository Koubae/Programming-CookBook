/**
 * @credit https://www.logicbig.com/tutorials/core-java-tutorial/logging/customizing-default-format.html
 */
package com.waves;

import java.util.Arrays;
import java.util.logging.Logger;


public class App {

    private static  Logger log = null;
    static {
        System.setProperty("java.util.logging.SimpleFormatter.format",
                "[%1$tF %1$tT] [%4$-1s] %5$s %n%6$s%n");
        log = Logger.getLogger(App.class.getName());

    }

    public static void main(String[] args) {
        log.info("Args " + args.length);
        log.info("Args " + args.length);


        System.out.println(Arrays.toString(args));
    }
}
