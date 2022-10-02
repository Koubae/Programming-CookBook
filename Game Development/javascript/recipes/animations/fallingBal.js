function fallingBal() {

    let raf;

    const ball = {
        x: 100,
        y: 100,
        vx: 5,
        vy: 2,
        radius: 25,
        color: 'blue',
        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2, true);
            ctx.closePath();
            ctx.fillStyle = this.color;
            ctx.fill();
        }
    };

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ball.draw();
        ball.x += ball.vx;
        ball.y += ball.vy;
        raf = window.requestAnimationFrame(draw);
    }

    canvas.addEventListener('mouseover', (e) => {
        raf = window.requestAnimationFrame(draw);
    });

    canvas.addEventListener('mouseout', (e) => {
        window.cancelAnimationFrame(raf);
    });
}

fallingBal();