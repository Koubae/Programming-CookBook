      static public enum Commands {
                EXIT("exit"),
                QUIT("quit"),
                HELP("help"),
                SAVE("save"),
                LOAD("load"),
            ;

            private final String text;

            Commands(final String text) {
                this.text = text;
            }

            /* (non-Javadoc)
             * @see java.lang.Enum#toString()
             */
            @Override
            public String toString() {
                return text;
            }
    
        }