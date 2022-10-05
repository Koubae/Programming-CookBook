// @credit:https://codereview.stackexchange.com/a/135207/235477
// the render logic should be focusing on the rendering
var drawGrid = function(ctx, w, h, step) {
    ctx.beginPath();
    for (var x=0;x<=w;x+=step) {
        ctx.moveTo(x, 0);
        ctx.lineTo(x, h);
    }
    // set the color of the line
    ctx.strokeStyle = 'rgb(255,0,0)';
    ctx.lineWidth = 1;
    // the stroke will actually paint the current path
    ctx.stroke();
    // for the sake of the example 2nd path
    ctx.beginPath();
    for (var y=0;y<=h;y+=step) {
        ctx.moveTo(0, y);
        ctx.lineTo(w, y);
    }
    // set the color of the line
    ctx.strokeStyle = 'rgb(20,20,20)';
    // just for fun
    ctx.lineWidth = 5;
    // for your original question - you need to stroke only once
    ctx.stroke();
};


drawGrid(this.ctx, 200, 200, 20);