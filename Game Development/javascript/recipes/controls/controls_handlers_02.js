/**
 * Simple recipes of a list of commond event handlers
 */
// --------------------------
// Event Listeners
// --------------------------
// resize the canvas to fill browser window dynamically
window.addEventListener('resize', resizeCanvas, false);
document.addEventListener("keydown", keyDownHandler, false);
document.addEventListener("keyup", keyUpHandler, false);

/**
 * Resize the canvas
 */
function resizeCanvas() {
    screenWidth = window.innerWidth;
    screenHeight = window.innerHeight;
    canvas.width = screenWidth;
    canvas.height = screenHeight;
    /**
     * Your drawings need to be inside this function otherwise they will be reset when
     * you resize the browser window and the canvas goes will be cleared.
     */
    // draw(); // becareful with this
}

function keyDownHandler(e) {
    if (!("code" in e)) {
        return;
    }

    switch (e.code) {

        case "Insert":
            toggleFullScreen(); // @credit: https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API#simple_fullscreen_usage
            break;
        default:
            return;
    }

}

function keyUpHandler(e) {
    if (!("code" in e)) {
        return;
    }

    switch (e.code) {

        default:
            return;
    }
}


// @credit: https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API#simple_fullscreen_usage
function toggleFullScreen() {
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen();
    } else if (document.exitFullscreen) {
        document.exitFullscreen();
    }
}


window.addEventListener('DOMContentLoaded', function (event) {
    main()
});