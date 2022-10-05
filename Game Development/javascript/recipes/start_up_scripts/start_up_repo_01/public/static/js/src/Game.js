"use strict";

// Classes
import GameEngine from "./GameEngine.js";
import GameEvents from "./GameEvent.js";
import {Ball} from "./entities.js";

function Game(canvas) {
    const BACKGROUND_COLOR = `rgba(0, 0, 0)`;

    const FONT_SIZE = "55px";
    const FONT_FAMILY = "serif";
    const FONT_COLOR = `rgb(255, 255, 255)`;

    this.canvas = canvas;
    this.ctx = undefined;
    this.screenWidth = window.innerWidth;
    this.screenHeight = window.innerHeight;
    this.gameEngine = GameEngine;
    this.gameEvents = GameEvents;


    this.constants = Object.freeze({
        BACKGROUND_COLOR: BACKGROUND_COLOR,

        FONT_SIZE: FONT_SIZE,
        FONT_FAMILY: FONT_FAMILY,
        FONT_COLOR: FONT_COLOR,
    })

    this.constructor = function () {
        this.ctx = this.canvas.getContext("2d", {alpha: false}); // Optimization by set alpha to false
        // Init Game-Engine
        this.gameEngine.game = this;
        this.gameEngine = Object.freeze(this.gameEngine);
        // Init Game-Events
        this.gameEvents.game = this;
        this.gameEvents = Object.freeze(this.gameEvents);
        this.gameEvents.resizeCanvas();

    }
    this.constructor();


    this.run = function () {
        this.gameEngine.gameLoop();
    }

    // --------------------------
    // Event Listeners
    // --------------------------
    // Window / Global Events
    // resize the canvas to fill browser window dynamically
    window.addEventListener('resize', this.gameEvents.resizeCanvas.bind(this.gameEvents), false);
    // Mouse Events
    document.addEventListener('mousemove', (e) => {
    }, false);
    document.addEventListener('mousedown', (e) => {
    }, false);
    document.addEventListener('mouseup', (e) => {
    }, false);
    document.addEventListener('dblclick', (e) => {
    }, false);
    // Keyboard Events
    document.addEventListener("keydown", this.gameEvents.keyDownHandler.bind(this.gameEvents), false);
    document.addEventListener("keyup", this.gameEvents.keyUpHandler.bind(this.gameEvents), false);

    // --------------------------
    // Game Logic
    // --------------------------

    // Game Entities Declarations here
    this.ball = new Ball(canvas, this.ctx);

    this.update = function () {
        this.ball.update();

        // Add Game Updates here


    }


}

export default Game;