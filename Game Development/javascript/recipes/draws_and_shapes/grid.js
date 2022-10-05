for (x = 0; x <= w; x += 20) {
    for (y = 0; y <= h; y += 20) {
        ctx.moveTo(x, 0);
        ctx.lineTo(x, h);
        ctx.stroke();
        ctx.moveTo(0, y);
        ctx.lineTo(w, y);
        ctx.stroke();
    }
}
