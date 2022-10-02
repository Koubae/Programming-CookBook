(function on() {
    main();
})();

function main() {
    const canvas = document.getElementById('screen');
    if (!canvas.getContext) {
        // canvas-unsupported code here
        alert("Unsupported browser :/");
        return;
    }
    // Constants and variables
    const BACKGROUND_COLOR = `rgba(0, 0, 0)`;
    const BACKGROUND_GRADIENT_1 = 'rgba(20, 0, 120, .8)';
    const BACKGROUND_GRADIENT_2 = `rgba(80, 120, 0, 0.5)`;

    const FONT_SIZE = "55px";
    const FONT_FAMILY = "serif";
    const FONT_COLOR = `rgb(255, 255, 255)`;

    let screenWidth = window.innerWidth;
    let screenHeight = window.innerHeight;
    let backgroundGradient;

    // Initialize the 2D context
    const ctx = canvas.getContext("2d");

    resizeCanvas();


    // --------------------------
    // Game-Engine
    // --------------------------
    function clearScreen() {
        ctx.save();
        ctx.fillStyle = BACKGROUND_COLOR;
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        // Add gradient to screen
        ctx.fillStyle = backgroundGradient;
        ctx.fillRect(0, 0, screenWidth, screenHeight);
        ctx.restore();
    }

    function draw() {
        clearScreen();

        makeTitle();
        triangleFilled();
        triangleStroked();
    }

    function gameLoop() {
        draw();
        requestAnimationFrame(gameLoop);

    }

    gameLoop();

    // --------------------------
    // Game-Logic
    // --------------------------

    function makeTitle() {
        ctx.font = `${FONT_SIZE} ${FONT_FAMILY}`;
        ctx.fillStyle = `${FONT_COLOR}`;
        ctx.fillText('Hello world', canvas.width / 2 - 100, canvas.height / 2 - 10);
    }

    function triangleFilled() {
        // Filled triangle
        ctx.beginPath();
        ctx.moveTo(325, 325);
        ctx.lineTo(405, 325);
        ctx.lineTo(325, 405);
        ctx.fill();
        ctx.stroke();
    }

    function triangleStroked() {
        // Stroked triangle
        ctx.beginPath();
        ctx.moveTo(425, 425);
        ctx.lineTo(425, 345);
        ctx.lineTo(345, 425);
        ctx.closePath();
        ctx.stroke();
    }


    // --------------------------
    // Event Listeners
    // --------------------------
    // resize the canvas to fill browser window dynamically
    window.addEventListener('resize', resizeCanvas, false);

    /**
     * Resize the canvas
     */
    function resizeCanvas() {
        screenWidth = window.innerWidth;
        screenHeight = window.innerHeight;
        canvas.width = screenWidth;
        canvas.height = screenHeight;

        // Re creates a color gradient as soon as the client resize the screen
        let cx = canvas.width * 0.5
        let cy = canvas.height * 0.5;
        backgroundGradient = ctx.createRadialGradient(cx, cy, 0, cx, cy, Math.sqrt(cx * cx + cy * cy));
        backgroundGradient.addColorStop(0, BACKGROUND_GRADIENT_1);
        backgroundGradient.addColorStop(1, BACKGROUND_GRADIENT_2);

        /**
         * Your drawings need to be inside this function otherwise they will be reset when
         * you resize the browser window and the canvas goes will be cleared.
         */
        draw();
    }


}


