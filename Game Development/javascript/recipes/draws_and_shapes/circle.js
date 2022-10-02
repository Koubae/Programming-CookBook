function circle() {
    ctx.beginPath();
    ctx.arc(250, 250, 150, 0, Math.PI * 2, true); // circle
    ctx.stroke();
}

circle()


function arcs() {
    for (let i = 0; i < 4; i++) {
        for (let j = 0; j < 3; j++) {
            ctx.beginPath();
            const x = 25 + j * 50; // x coordinate
            const y = 25 + i * 50; // y coordinate
            const radius = 20; // Arc radius
            const startAngle = 0; // Starting point on circle
            const endAngle = Math.PI + (Math.PI * j) / 2; // End point on circle
            const counterclockwise = i % 2 !== 0; // clockwise or counterclockwise

            ctx.arc(x, y, radius, startAngle, endAngle, counterclockwise);

            if (i > 1) {
                ctx.fill();
            } else {
                ctx.stroke();
            }
        }
    }
}

arcs();
