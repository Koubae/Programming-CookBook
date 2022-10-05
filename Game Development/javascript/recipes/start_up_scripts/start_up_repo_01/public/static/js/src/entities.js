"use strict";

import { circle } from "./paintings.js";

function Ball(canvas, ctx) {
    this.x = 250;
    this.y = 250;
    this.radius = 50;
    this.velocityX = 10;
    this.velocityY = 10;
    this.color = `rgb(255, 0, 0)`
    this.ctx = ctx;
    this.canvas = canvas;


}

Ball.prototype.draw = function () {
    circle(this.ctx, this.x, this.y, this.radius, this.color);
}

Ball.prototype.update = function () {
    this.draw();

    // TODO: 'inject' the collision type into the enity!
    const wallXMin = this.x - this.radius / 2;
    const wallXMax = this.x + this.radius / 2;

    const wallYMin = this.y - this.radius / 2;
    const wallYMax = this.y + this.radius / 2;

    if (wallXMax + this.velocityX > this.canvas.width || wallXMin + this.velocityX < 0) {
        this.velocityX = -this.velocityX;
    }
    if (wallYMax + this.velocityY > this.canvas.height || wallYMin + this.velocityY < 0) {
        this.velocityY = -this.velocityY;
    }

    // TODO: we should 'inject' into the instance type that this entity is subject to gravity
    // GRAVITY
    this.x += this.velocityX;
    this.y += this.velocityY;


}

export {
    Ball,
}