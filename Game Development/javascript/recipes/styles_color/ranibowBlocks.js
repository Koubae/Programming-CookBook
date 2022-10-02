function rainbowBlocks() {
    let blockPosition = 0;
    for (let i = 0; i < 6; i++) {
        for (let j = 0; j < 6; j++) {
            ctx.fillStyle = `rgb(${Math.floor(255 - 42.5 * i)}, ${Math.floor(255 - 42.5 * j)}, 0)`;
            ctx.fillRect(j * 25 + (blockPosition), i * 25, 25, 25);
        }
    }
    blockPosition += 150;

    for (let i = 0; i < 6; i++) {
        for (let j = 0; j < 6; j++) {
            ctx.fillStyle = `rgb(${Math.floor(255 - 42.5 * i)}, ${Math.floor(255 - 42.5 * j)}, ${Math.floor(255 - 42.5 * j)})`;
            ctx.fillRect(j * 25 + (blockPosition), i * 25, 25, 25);
        }
    }

    blockPosition += 150;
    for (let i = 0; i < 6; i++) {
        for (let j = 0; j < 6; j++) {
            ctx.fillStyle = `rgb(${Math.floor(255 - 42.5 * i)}, 0, ${Math.floor(255 - 42.5 * j)})`;
            ctx.fillRect(j * 25 + (blockPosition), i * 25, 25, 25);
        }
    }

    blockPosition += 150;
    for (let i = 0; i < 6; i++) {
        for (let j = 0; j < 6; j++) {
            ctx.fillStyle = `rgb(0, ${Math.floor(255 - 42.5 * i)}, ${Math.floor(255 - 42.5 * j)})`;
            ctx.fillRect(j * 25 + (blockPosition), i * 25, 25, 25);
        }
    }
}

rainbowBlocks();
