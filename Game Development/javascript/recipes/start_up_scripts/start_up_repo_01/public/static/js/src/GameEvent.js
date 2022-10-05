"use strict";
// --------------------------
// Event Listeners
// --------------------------

const GameEvents = {
    game: undefined,
    keyDownHandler(e) {
        console.log("Gamevents this ", this);
        if (!("code" in e)) {
            return;
        }

        switch (e.code) {

            case "KeyJ":
                this.toggleFullScreen(); // @credit: https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API#simple_fullscreen_usage
                break;
            default:
                return;
        }
    },
    keyUpHandler(e) {
        if (!("code" in e)) {
            return;
        }

        switch (e.code) {

            default:
                return;
        }
    },
    resizeCanvas(e) {
        this.game.screenWidth = window.innerWidth;
        this.game.screenHeight = window.innerHeight;
        this.game.canvas.width = this.game.screenWidth;
        this.game.canvas.height = this.game.screenHeight;
        /**
         * Your drawings need to be inside this function otherwise they will be reset when
         * you resize the browser window and the canvas goes will be cleared.
         */
    },
    // @credit: https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API#simple_fullscreen_usage
    toggleFullScreen(e) {
        if (!document.fullscreenElement) {
            document.documentElement.requestFullscreen();
        } else if (document.exitFullscreen) {
            document.exitFullscreen();
        }
    },

}

export default GameEvents;