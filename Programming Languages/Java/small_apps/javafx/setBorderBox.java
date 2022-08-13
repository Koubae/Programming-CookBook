package Programming Languages.Java.small_apps.javafx;

public class setBorderBox {
    
    public static void main(String[] a) {
        String cssLayout = "-fx-border-color: red;\n" +
        "-fx-border-insets: 5;\n" +
        "-fx-border-width: 3;\n" +
        "-fx-border-style: dashed;\n";
HBox wrapper = new HBox(title);
wrapper.setStyle(cssLayout);
    }
}
