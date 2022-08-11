/**
 * Let you choose at which screen to start the app 
 * @stackoverflow https://stackoverflow.com/a/73315578/13903942
 */
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
import javafx.geometry.Rectangle2D;
import javafx.scene.*;
import javafx.scene.control.*;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.*;

import javafx.scene.shape.*;
import javafx.stage.Screen;
import javafx.stage.Stage;
import javafx.scene.paint.Color;
import javafx.scene.text.Text;
import javafx.scene.text.Font;

import java.util.ArrayList;
import java.util.List;

import static javafx.geometry.Pos.CENTER;




public class Main extends Application {

    final public int WIN_WIDTH_MIN = 640;
    final public int WIM_HEIGHT_MIN = 480;


    public static void main(String[] args) {
        launch();
    }


    @Override
    public void start(Stage stage) {
        VBox mainView = layoutMain();
        Scene mainScene = new Scene(mainView);
        stage.setScene( mainScene );
        setupStageLocation(stage, 1, false, true);
        stage.show();


    }

    private VBox layoutMain() {
        VBox mainView = new VBox();
        mainView.setPadding(new Insets(10));
        mainView.setSpacing(4);
        return mainView;
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
