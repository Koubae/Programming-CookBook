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
import javafx.scene.input.KeyCode;
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




public class Snake extends Application {

    public static void main(String[] args) throws Exception { launch(args); }


    @Override public void start(Stage primaryStage) throws Exception {
        QuadCurve curve = createStartingCurve();


        final BorderPane root = new BorderPane();
        Scene scene = new Scene(root, 1000, 1000);

        final Anchor control2 = new Anchor(Color.GOLDENROD, curve.controlXProperty(), curve.controlYProperty());


        root.getChildren().add(curve);
        root.getChildren().add(control2);


        primaryStage.setTitle("Quadcurve Manipulation");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private QuadCurve createStartingCurve() {
        QuadCurve curve = new QuadCurve();
        curve.setStartX(100);
        curve.setStartY(100);
        curve.setControlX(200);
        curve.setControlY(50);
        curve.setEndX(300);
        curve.setEndY(100);
        curve.setStroke(Color.BLACK);
        curve.setStrokeWidth(10);
        curve.setStrokeLineCap(StrokeLineCap.ROUND);
        curve.setFill(Color.CORNSILK.deriveColor(0, 1.2, 1, 0.6));
        return curve;
    }

    // a draggable anchor displayed around a point.
    class Anchor extends Circle {

        Anchor(Color color, DoubleProperty x, DoubleProperty y) {
            super(x.get(), y.get(), 10);
            setFill(color.deriveColor(1, 1, 1, 0.5));

            y.bind(centerYProperty());
            enableDrag();
            changeCurve();
        }


        private void changeCurve() {
            setOnKeyPressed((event) -> {
                System.out.println(event.getCode() == KeyCode.DOWN);
                if (event.getCode() == KeyCode.DOWN) {
                    double newY = getCenterY();
                    while (newY > 0 && newY < getScene().getHeight()) {
                        setCenterY(newY);
                        newY+=1;
                    }
                }
                else if (event.getCode() == KeyCode.UP) {
                    double newY = getCenterY();
                    while (newY > 0 && newY < getScene().getHeight()) {
                        setCenterY(newY);
                        newY-=1;
                    }
                }
            });
            setOnKeyReleased((event) -> {
                if (event.getCode() == KeyCode.DOWN) {
                }
                if (event.getCode() == KeyCode.UP) {
                }

            });
        }

        // make a node movable by dragging it around with the mouse.
        private void enableDrag() {
            setOnMousePressed(new EventHandler<MouseEvent>() {
                @Override public void handle(MouseEvent mouseEvent) {
                    // record a delta distance for the drag and drop operation.
                    getScene().setCursor(Cursor.MOVE);
                }
            });
            setOnMouseReleased(new EventHandler<MouseEvent>() {
                @Override public void handle(MouseEvent mouseEvent) {
                    getScene().setCursor(Cursor.HAND);
                }
            });
            setOnMouseDragged(new EventHandler<MouseEvent>() {
                @Override public void handle(MouseEvent mouseEvent) {
                    double newY = mouseEvent.getY();
                    System.out.println(newY);
                    if (newY > 0 && newY < getScene().getHeight()) {
                        setCenterY(newY);
                    }
                }
            });
            setOnMouseEntered(new EventHandler<MouseEvent>() {
                @Override public void handle(MouseEvent mouseEvent) {
                    if (!mouseEvent.isPrimaryButtonDown()) {
                        getScene().setCursor(Cursor.HAND);
                    }
                }
            });
            setOnMouseExited(new EventHandler<MouseEvent>() {
                @Override public void handle(MouseEvent mouseEvent) {
                    if (!mouseEvent.isPrimaryButtonDown()) {
                        getScene().setCursor(Cursor.DEFAULT);
                    }
                }
            });
        }
    }



}