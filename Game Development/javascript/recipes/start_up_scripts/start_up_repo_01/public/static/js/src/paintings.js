"use strict";
function circle(ctx, coordX, coordY, radius, color) {
    ctx.beginPath();
    ctx.arc(coordX, coordY, radius, 0, Math.PI * 2, true); // circle
    ctx.closePath();
    ctx.fillStyle = color;
    ctx.fill();
}

export {
    circle,
}