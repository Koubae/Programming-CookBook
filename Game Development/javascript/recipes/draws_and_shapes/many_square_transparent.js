function main() {
    const canvas = document.getElementById('screen');
    if (!canvas.getContext) {
        // canvas-unsupported code here
        alert("Unsupported browser :/");
        return;
    }

    const ctx = canvas.getContext('2d');

    const red = "rgb(200, 0, 0, 0.5)";
    const blue = "rgb(0, 0, 200, 0.5)";

    for (let i = 0; i < 100; i++) {
        const rect_width = 50;
        const rect_height = 50;

        const rect_1_x = 10;
        const rect_1_y = 10;

        const rect_2_x = 30;
        const rect_2_y = 30;
        ctx.fillStyle = i % 2 === 0 ? red : blue;
        ctx.fillRect(rect_1_x * i, rect_1_y * i, rect_width, rect_height);

        // ctx.fillStyle = "rgba(0, 0, 200, 0.5)";
        // ctx.fillRect(rect_2_x * i, rect_2_y * i, rect_width, rect_height);
    }

}


(function gameOn() {
    main();
})()