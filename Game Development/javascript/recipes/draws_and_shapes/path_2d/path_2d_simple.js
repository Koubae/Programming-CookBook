const rectangle = new Path2D();
rectangle.rect(10, 10, 50, 50);

const circle = new Path2D();
circle.arc(100, 35, 25, 0, 2 * Math.PI);

ctx.stroke(rectangle);
ctx.fill(circle);


// Using SVG
const p = new Path2D('M10 10 h 80 v 80 h -80 Z');

ctx.stroke(p)