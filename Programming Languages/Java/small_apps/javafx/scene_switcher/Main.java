package com.koubae;

import javafx.event.ActionEvent;
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
import javafx.geometry.Rectangle2D;
import javafx.scene.*;
import javafx.scene.control.*;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.*;

import javafx.scene.shape.*;
import javafx.scene.text.FontWeight;
import javafx.stage.Screen;
import javafx.stage.Stage;
import javafx.scene.paint.Color;
import javafx.scene.text.Text;
import javafx.scene.text.Font;

import java.util.ArrayList;
import java.util.List;

import static javafx.geometry.Pos.CENTER;




public class Snake extends Application {

    final public int WIN_WIDTH_MIN = 640;
    final public int WIM_HEIGHT_MIN = 480;

    private Stage stage;


    public static void main(String[] args) {
        launch();
    }


    @Override
    public void start(Stage stageMain) {
        try {
            stage = stageMain;
            Scene root = new Scene(layoutMain());
            stage.setScene( root );
            setupStageLocation(stage, 1, false, true);
            stage.setTitle("Start");
            stage.show();
        } catch (Exception e) {
            e.printStackTrace();

        }


    }

    private void viewMain() {
        VBox view = layoutMain();
        // Get the stage
        Scene scene = new Scene(view);
        stage.setScene(scene);
        setupStageLocation(stage, 1, false, true);
        stage.setTitle("View Main");

    }

    private void viewTwo() {

        Label text = new Label("World");
        Font font = Font.font("Courier New", FontWeight.BOLD, 36);
        text.setFont(font);

        HBox content = new HBox(text);
        content.setAlignment(CENTER);

        Button changeView = new Button("View 1");
        changeView.setOnAction(e -> viewMain());

        VBox view = new VBox(content, changeView);
        view.setPadding(new Insets(10));
        view.setSpacing(4);
        view.setAlignment(CENTER);

        // Get the stage
        Scene scene = new Scene(view);
        stage.setScene(scene);
        setupStageLocation(stage, 1, false, true);
        stage.setTitle("View Second");
    }
    private VBox layoutMain() {
        Label text = new Label("Hello");
        Font font = Font.font("Courier New", FontWeight.BOLD, 36);
        text.setFont(font);

        HBox content = new HBox(text);
        content.setAlignment(CENTER);

        Button changeView = new Button("View 2");
        changeView.setOnAction(e -> viewTwo());

        VBox view = new VBox(content, changeView);
        view.setPadding(new Insets(10));
        view.setSpacing(4);
        view.setAlignment(CENTER);
        return view;
    }

    /**
     * @credit john16384 https://community.oracle.com/tech/developers/discussion/2390272/how-to-use-dual-monitor-in-javafx2
     * @param stage
     * @param screenNumber
     * @param fullScreen
     * @param maxSize
     */
    private void setupStageLocation(Stage stage, int screenNumber, boolean fullScreen, boolean maxSize) {
        ObservableList<Screen> screens = Screen.getScreens();
        Screen screen = screens.size() <= screenNumber ? Screen.getPrimary() : screens.get(screenNumber);

        Rectangle2D bounds = screen.getBounds();
        boolean primary = screen.equals(Screen.getPrimary());    // WORKAROUND: this doesn't work nice in combination with full screen, so this hack is used to prevent going fullscreen when screen is not primary

        stage.setX(bounds.getMinX());
        stage.setY(bounds.getMinY());

        if (maxSize) {
            stage.setWidth(bounds.getWidth());
            stage.setHeight(bounds.getHeight());
        } else {
            stage.setWidth(WIN_WIDTH_MIN);
            stage.setHeight(WIM_HEIGHT_MIN);
        }
        stage.setFullScreen(fullScreen);

        if(primary) {
            // Do some other settings
        } else {
            stage.toFront();
        }

    }



}