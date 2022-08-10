import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.*;

import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;
import javafx.scene.Group;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.scene.text.Text;
import javafx.scene.text.Font;

import static javafx.geometry.Pos.CENTER;

public class Snake extends Application {

    final public int WIN_WIDTH_MIN = 640;
    final public int WIM_HEIGHT_MIN = 480;

    private DoubleProperty startX = new SimpleDoubleProperty();
    private DoubleProperty startY = new SimpleDoubleProperty();
    private DoubleProperty shownX = new SimpleDoubleProperty();
    private DoubleProperty shownY = new SimpleDoubleProperty();


    public static void main(String[] args) {
        launch();
    }


    @Override
    public void start(Stage stage) {
//        Parent contentRoot = createInitialContent();
//        Scene scene = new Scene(contentRoot, WIN_WIDTH_MIN, WIM_HEIGHT_MIN, Color.GRAY);
//        scene.setOnKeyPressed(e -> {
//            String codeString = e.getCode().toString();
//            System.out.println(codeString);
//        });
//        stage.setScene(scene);
//        stage.show();

        Label startLabel = new Label("Start Dimensions");
        TextField startTF = new TextField();
        startTF.textProperty().bind(
                Bindings.format("(%.1f, %.1f)", startX, startY)
        );

        Label shownLabel = new Label("Shown Dimensions");
        TextField shownTF = new TextField();
        shownTF.textProperty().bind(
                Bindings.format("(%.1f, %.1f)", shownX, shownY)
        );

        GridPane gp = new GridPane();
        gp.getColumnConstraints().add(new ColumnConstraints(50)); // column 0 is 100 wide
        gp.add(startLabel, 0,0);
        gp.add(startTF, 1, 0);
        gp.add(shownLabel, 0, 1);
        gp.add(shownTF, 1, 1);
        gp.add(new Label("Hello world"), 0, 2);
        gp.add(new Label("Hello world"), 0, 3);
        gp.add(new Label("Hello world"), 0, 4);
        gp.setHgap(10);
        gp.setVgap(10);
        System.out.println(gp.getRowConstraints().size());

        HBox hbox = new HBox(gp);
        hbox.setAlignment(CENTER);


        VBox vbox = new VBox(hbox);
        vbox.setAlignment(CENTER);

        Scene scene = new Scene(new StackPane(vbox), 480, 320);
        stage.setScene(scene);

        // before show()...I just set this to 480x320, right?
        startX.set( stage.getWidth() );
        startY.set( stage.getHeight() );
        stage.setOnShown( (evt) -> {
            shownX.set( stage.getWidth() );
            shownY.set( stage.getHeight() );  // all available now
        });

        stage.setTitle("Start Vs. Shown");
        stage.show();



    }

    private Parent createInitialContent() {
        Rectangle box = new Rectangle(100, 50, Color.BLUE);
        transform(box);

        return new Pane(box);
    }

    private void transform(Rectangle box) {
        box.setTranslateX(100);
        box.setTranslateY(200);

        box.setScaleX(1.5);
        box.setScaleY(1.5);

        box.setRotate(30);

        box.setOnMouseEntered(e -> System.out.println("hello"));
    }

}