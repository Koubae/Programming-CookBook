package dev.federicobau.games.jbreakout.screen;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Input;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.scenes.scene2d.ui.Skin;
import com.badlogic.gdx.scenes.scene2d.ui.TextButton;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable;
import com.badlogic.gdx.utils.ScreenUtils;
import dev.federicobau.games.jbreakout.JBreakout;

public class CustomButton implements Screen {
    final JBreakout game;


    private Stage stage;
    private Skin skin;
    private TextButton startButton;


    public MainMenuScreen(JBreakout game) {
        this.game = game;
    }

    @Override
    public void show() {
        stage = new Stage(game.viewport, game.batch);
        Gdx.input.setInputProcessor(stage);

//        skin = new Skin(Gdx.files.internal("uiskin.json"));
        skin = new Skin(Gdx.files.internal("uiskin.json"));

//        TextureRegionDrawable up = new TextureRegionDrawable(new TextureRegion(new Texture("button_up.png")));
//        TextureRegionDrawable down = new TextureRegionDrawable(new TextureRegion(new Texture("button_down.png")));
//        TextButton.TextButtonStyle style = new TextButton.TextButtonStyle(up, down, up, new BitmapFont());
//
//        startButton = new TextButton("Click Me", style);
//        TextButton button = new TextButton("Click Me", style);

        startButton = new TextButton("Start Game", skin);
        startButton.setSize(200, 60);
        startButton.setPosition(
            Gdx.graphics.getWidth() / 2f - startButton.getWidth() / 2,
            Gdx.graphics.getHeight() / 2f - startButton.getHeight() / 2
        );

        startButton.addListener(new ClickListener() {
            @Override
            public void clicked(InputEvent event, float x, float y) {
                Gdx.app.log("MainMenu", "Start button clicked!");
                // Here you can switch to another screen, e.g.:
                // game.setScreen(new GameScreen());
            }
        });

        stage.addActor(startButton);

        // Custom button
        TextButton.TextButtonStyle style = new TextButton.TextButtonStyle();
        style.font = skin.getFont("default-font");
        style.up   = skin.newDrawable("default-round", Color.GREEN); // normal state
        style.down = skin.newDrawable("default-round-down", Color.DARK_GRAY); // pressed state
        style.fontColor = Color.WHITE;

        TextButton greenButton = new TextButton("Play", style);
        greenButton.setSize(200, 60);
        greenButton.setPosition(200, 300);

        stage.addActor(greenButton);

        // Green here is a custom style added in uiskin.json
        TextButton greenCustomStyleButton = new TextButton("Play 2", skin, "green");
        greenCustomStyleButton.setSize(200, 60);
        greenCustomStyleButton.setPosition(400, 300);

        stage.addActor(greenCustomStyleButton);
    }

    @Override
    public void render(float delta) {
        input();

        ScreenUtils.clear(Color.BLACK);

        // Update camera
        game.camera.update();

        // Apply camera to renderers
        game.renderer.setProjectionMatrix(game.camera.combined);
        game.batch.setProjectionMatrix(game.camera.combined);

        float screenWidth = game.viewport.getWorldWidth();
        float screenHeight = game.viewport.getWorldHeight();

        game.renderer.begin(ShapeRenderer.ShapeType.Filled);

        game.renderer.setColor(1, 0, 0, 1); // Red
        game.renderer.rect(100, 100, 200, 50);
        game.renderer.rect(screenWidth / 2, screenHeight / 2, 200, 50);

        game.renderer.end();

        // Draw text
        game.batch.begin();

        game.font.draw( game.batch, "Hello World!", 100, 200);
        game.font.draw(game.batch, "Screen: " + screenWidth + "x" + (int)screenHeight, 400, 200);

        game.batch.end();

        stage.act(delta);
        stage.draw();

    }



    @Override
    public void resize(int width, int height) {
        game.viewport.update(width, height, true);
    }

    @Override
    public void pause() {

    }

    @Override
    public void resume() {

    }

    @Override
    public void hide() {

    }

    @Override
    public void dispose() {
        stage.dispose();
        skin.dispose();
    }

    private void input() {
        if (Gdx.input.isKeyJustPressed(Input.Keys.ESCAPE)) {
            Gdx.app.exit();
        }
    }

}
