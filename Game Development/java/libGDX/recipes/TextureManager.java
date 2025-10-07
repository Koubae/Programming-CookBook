import com.badlogic.gdx.graphics.Texture;
import java.util.HashMap;
import java.util.Map;


/**
 * 

@usage

TextureManager textureManager = new TextureManager();
textureManager.load();

Texture playerTexture = textureManager.get("player");

// when closing the game or changing screen
textureManager.dispose();

 */
public class TextureManager {
    private final Map<String, Texture> textures = new HashMap<>();

    public void load() {
        textures.put("player", new Texture("textures/player.png"));
        textures.put("enemy", new Texture("textures/enemy.png"));
        textures.put("background", new Texture("textures/background.png"));
    }

    public Texture get(String name) {
        return textures.get(name);
    }

    public void dispose() {
        for (Texture texture : textures.values()) {
            texture.dispose();
        }
        textures.clear();
    }
}
