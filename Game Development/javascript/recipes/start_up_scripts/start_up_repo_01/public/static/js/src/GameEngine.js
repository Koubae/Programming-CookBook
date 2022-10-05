"use strict";

// --------------------------
// Game-Engine
// --------------------------
const GameEngine = {
    game: undefined,
    clearScreen() {
        this.game.ctx.save();
        this.game.ctx.clearRect(0, 0, this.game.canvas.width, this.game.canvas.height);
        this.game.ctx.restore();
    },

    draw() {
        this.clearScreen();
        this.game.update();
    },

    gameLoop() {
        this.draw();
        requestAnimationFrame(this.gameLoop.bind(this));
    }
}

export default GameEngine;