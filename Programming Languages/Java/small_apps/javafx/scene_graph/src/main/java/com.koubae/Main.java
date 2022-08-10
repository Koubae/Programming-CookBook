// @source: https://openjfx.io/javadoc/18/javafx.graphics/javafx/scene/package-summary.html
package example;

import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.Group;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.scene.text.Text;
import javafx.scene.text.Font;

public class Example extends Application {

    @Override public void start(Stage stage) {
        
        Group root = new Group();
        Scene scene = new Scene(root, 200, 150);
        scene.setFill(Color.LIGHTGRAY);

        Circle circle = new Circle(60, 40, 30, Color.GREEN);
        
        Text text = new Text(10, 90, "JavaFX Scene");
        text.setFill(Color.DARKRED);
        
        Font font = new Font(20);
        text.setFont(font);
        
        root.getChildren().add(circle);
        root.getChildren().add(text);
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        Application.launch(args);
    }
}