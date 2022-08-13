// Source https://edencoding.com/scene-background/#:~:text=The%20simplest%20way%20to%20set,accept%20multiple%20images%20and%20fills.

class Main {

    public static void main(String[] args) {
        VBox view = new VBox(content, changeView);
        view.setPadding(new Insets(10));
        view.setSpacing(4);
        view.setAlignment(CENTER);

//        view.setBackground(new Background(new BackgroundFill(Color.	DARKSLATEGRAY, CornerRadii.EMPTY, Insets.EMPTY)));

        view.setBackground(new Background(
                new BackgroundFill(
                        new LinearGradient(0, 0, 0, 1, true,
                                CycleMethod.NO_CYCLE,
                                new Stop(0, Color.web("#4568DC")),
                                new Stop(1, Color.web("#B06AB3"))
                        ), CornerRadii.EMPTY, Insets.EMPTY
                ),
                new BackgroundFill(
                        new ImagePattern(
                                new Image("https://edencoding.com/resources/wp-content/uploads/2021/02/Stars_128.png"),
                                0, 0, 128, 128, false
                        ), CornerRadii.EMPTY, Insets.EMPTY
                ),
                new BackgroundFill(
                        new RadialGradient(
                                0, 0, 0.5, 0.5, 0.5, true,
                                CycleMethod.NO_CYCLE,
                                new Stop(0, Color.web("#FFFFFF33")),
                                new Stop(1, Color.web("#00000033"))),
                        CornerRadii.EMPTY, Insets.EMPTY
                )
        ));

    }
}