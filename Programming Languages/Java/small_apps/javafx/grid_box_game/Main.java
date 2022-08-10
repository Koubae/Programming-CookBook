package com.koubae;

import javafx.application.Application;
import javafx.beans.property.DoubleProperty;
import javafx.beans.property.SimpleDoubleProperty;
import javafx.event.EventHandler;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.SubScene;

import javafx.scene.input.MouseEvent;
import javafx.scene.layout.*;

import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;
import javafx.scene.Group;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;

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

    private DoubleProperty startX = new SimpleDoubleProperty();
    private DoubleProperty startY = new SimpleDoubleProperty();
    private DoubleProperty shownX = new SimpleDoubleProperty();
    private DoubleProperty shownY = new SimpleDoubleProperty();


    public static void main(String[] args) {
        launch();
    }


    @Override
    public void start(Stage stage) {


        int rows = 5;
        int columns = 5;

        stage.setTitle("Enjoy your game");
        GridPane grid = new GridPane();
        for(int i = 0; i < columns; i++) {
            ColumnConstraints column = new ColumnConstraints(40);
            grid.getColumnConstraints().add(column);
        }

        for(int i = 0; i < rows; i++) {
            RowConstraints row = new RowConstraints(40);
            grid.getRowConstraints().add(row);
        }

        grid.setOnMouseReleased(new EventHandler<MouseEvent>() {
            public void handle(MouseEvent me) {
                try {
                    grid.add(Anims.getAnim(1), (int)((me.getSceneX() - (me.getSceneX() % 40)) / 40), (int)((me.getSceneY() - (me.getSceneY() % 40)) / 40)); //here the getAnim argument could be between 1-7
                } catch (Exception e) {
                    throw new RuntimeException(e);
                }
            }
        });

        grid.setStyle("-fx-background-color: white; -fx-grid-lines-visible: true");
        Scene scene = new Scene(grid, (columns * 40) , (rows * 40), Color.WHITE);
        stage.setScene(scene);
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