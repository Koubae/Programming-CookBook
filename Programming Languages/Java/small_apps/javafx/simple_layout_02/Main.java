package com.koubae;

import javafx.application.Application;
import javafx.beans.binding.Bindings;
import javafx.beans.property.DoubleProperty;
import javafx.beans.property.SimpleDoubleProperty;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.scene.*;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.*;

import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.scene.text.Text;
import javafx.scene.text.Font;

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

        group.getChildren().addAll(stack, hello, world, button1, button2);



        HBox hbox = new HBox(group);
        hbox.setPadding( new Insets(10));
        hbox.setSpacing( 2 );

        VBox vbox = new VBox(hbox);
        vbox.setPadding( new Insets(10));
        vbox.setSpacing(4);
        return vbox;
    }


}