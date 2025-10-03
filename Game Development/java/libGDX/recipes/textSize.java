Label title = new Label("My Game", skin, "green"); // or another style key
title.setPosition((screenWidth - title.getPrefWidth())/2f, screenHeight - 100);
title.setFontScale(2f);
stage.addActor(title);

Color old = game.font.getColor().cpy();
game.font.getData().setScale(2f);     // 2x size
game.font.setColor(Color.YELLOW);     // set font color
game.font.draw(game.batch, UIConstants.GAME_TITLE, (screenWidth / 2), screenHeight - 100);
game.font.setColor(old);
