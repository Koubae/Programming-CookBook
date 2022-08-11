package com.koubae;

import javafx.application.Application;
import javafx.beans.binding.Bindings;
import javafx.beans.property.DoubleProperty;
import javafx.beans.property.ReadOnlyObjectProperty;
import javafx.beans.property.SimpleDoubleProperty;
import javafx.beans.property.SimpleObjectProperty;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.*;
import javafx.scene.control.*;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.*;

import javafx.scene.shape.*;
import javafx.stage.Stage;
import javafx.scene.paint.Color;
import javafx.scene.text.Text;
import javafx.scene.text.Font;

import java.util.ArrayList;
import java.util.List;

import static javafx.geometry.Pos.CENTER;

class Anims {

    public static SubScene getAnim(final int number) throws Exception {
        Circle circle = new Circle(20, 20f, 7);
        circle.setFill(Color.RED);
        Group group = new Group();
        group.getChildren().add(circle);
        SubScene scene = new SubScene(group, 40, 40);
        scene.setFill(Color.WHITE);
        return scene;
    }
}



public class Snake extends Application {

    final public int WIN_WIDTH_MIN = 640;
    final public int WIM_HEIGHT_MIN = 480;


    public static void main(String[] args) {
        launch();
    }


    @Override
    public void start(Stage stage) {
        Scene mainScene = new Scene(layoutMain(), WIN_WIDTH_MIN, WIM_HEIGHT_MIN);
        stage.setScene( mainScene );
        stage.show();


    }

    private VBox layoutMain() {


        Group group = new Group();

        int initialYPos = 10;
        int YPosIncrementer = 100;

        StackPane stack = new StackPane();
        stack.getChildren().addAll(new Rectangle(100,100,Color.BLUE), new Label("Go!"));
        stack.setLayoutY(initialYPos);
        initialYPos = initialYPos + YPosIncrementer;


        Label hello = new Label("Hello");
        Label world = new Label("World");
        hello.setLayoutY(initialYPos);
        world.setLayoutY(initialYPos);
        world.setLayoutX(50);
        initialYPos = initialYPos + YPosIncrementer;

        Button button1 = new Button("Button Number 1");
        Button button2 = new Button("Button 2");
        button1.setLayoutY(initialYPos);
        initialYPos = initialYPos + YPosIncrementer;
        button2.setLayoutY(initialYPos);

//        group.getChildren().addAll(stack, hello, world, button1, button2);

        final Ellipse shape = new Ellipse(50, 50);
        shape.setCenterX(80);
        shape.setCenterY(80);
        shape.setFill(Color.LIGHTCORAL);
        shape.setStroke(Color.LIGHTCORAL);

        ObservableList<String> severities =
                FXCollections.observableArrayList("Blocker", "Workaround", "N/A");
        ComboBox<String> cbSeverity = new ComboBox<>(severities);


        HBox hbox = new HBox();
        hbox.getChildren().addAll(stack, hello, world, button1, button2, shape, cbSeverity);
        hbox.setPadding( new Insets(10));
        HBox.setMargin(hbox, new Insets(1.0d, 1.0d, 1.0d, 1.0d));
        hbox.setSpacing( 2 );

        TilePane tilePane = new TilePane();
        tilePane.setPrefColumns(3);
        tilePane.setPrefRows(3);
        tilePane.setTileAlignment( Pos.CENTER );

        tilePane.getChildren().addAll(
                new Rectangle(50, 50, Color.RED),
                new Rectangle( 50, 50, Color.GREEN ),
                new Rectangle( 50, 50, Color.BLUE ),
                new Rectangle( 50, 50, Color.YELLOW ),
                new Rectangle( 50, 50, Color.CYAN ),
                new Rectangle( 50, 50, Color.PURPLE ),
                new Rectangle( 50, 50, Color.BROWN ),
                new Rectangle( 50, 50, Color.PINK ),
                new Rectangle( 50, 50, Color.ORANGE )
        );
//        tilePane.setPrefTileHeight(100);
//        tilePane.setPrefTileWidth(100);

        TilePane tilePane2 = new TilePane();
        tilePane2.setPrefColumns(2);
        tilePane2.setPrefRows(2);
        tilePane2.setTileAlignment( Pos.CENTER );

        Circle redCircle = new Circle(50, Color.RED);
        Circle greenCircle = new Circle( 50, Color.GREEN );
        Circle blueCircle = new Circle( 50, Color.BLUE );
        Circle yellowCircle = new Circle( 50, Color.YELLOW );

        List<Circle> circles = new ArrayList<>();
        circles.add( redCircle );
        circles.add( greenCircle );
        circles.add( blueCircle );
        circles.add( yellowCircle );

        circles
                .stream()
                .forEach( (c) -> c.getProperties().put( "selected", Boolean.FALSE ));

        tilePane2.getChildren().addAll(
                circles
        );

        tilePane2.setOnMouseClicked(

                (evt) -> tilePane
                        .getChildren()
                        .stream()
                        .filter( c ->
                                c.contains(
                                        c.sceneToLocal(evt.getSceneX(), evt.getSceneY(), true)
                                )
                        )
                        .findFirst()
                        .ifPresent(
                                (c) -> {
                                    Boolean selected = (Boolean) c.getProperties().get("selected");
                                    if( selected == null || selected == Boolean.FALSE ) {
                                        c.setOpacity(0.3d);
                                        c.getProperties().put("selected", Boolean.TRUE);
                                    } else {
                                        c.setOpacity( 1.0d );
                                        c.getProperties().put("selected", Boolean.FALSE);
                                    }
                                }
                        )
        );

        ProgressBar pb = new ProgressBar();
        HBox hbox2 = new HBox(tilePane2, pb);
        hbox.setPadding( new Insets(10));
        HBox.setMargin(hbox, new Insets(1.0d, 1.0d, 1.0d, 1.0d));
        hbox.setSpacing( 2 );


        VBox vbox = new VBox(hbox, hbox2);
        vbox.setPadding( new Insets(10));
        vbox.setSpacing(4);
        return vbox;
    }



}