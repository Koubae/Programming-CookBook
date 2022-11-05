import {boot}  from "../core.js";

export default function recipe(THREE) {
    function normalizeCoords(vector, canvas) {
        let widthHalf = canvas.width / 2;
        let heightHalf = canvas.height / 2;
       /* vector.x = ( vector.x + 1) * canvas.width / 2;
        vector.y = - ( vector.y - 1) * canvas.height / 2;*/
   /*
        vector.x = ( vector.x * widthHalf ) + widthHalf;
        vector.y = - ( vector.y * heightHalf ) + heightHalf;*/

        // this works!!!
       /* vector.x =  ( vector.x / window.innerWidth ) * 2 - 1;
        vector.y = - ( vector.y / window.innerHeight ) * 2 + 1;*/
        vector.x =  ( vector.x / window.innerWidth ) * 2 - 1;
        vector.y = - ( vector.y / (window.innerHeight) ) * 2 + 1;

        return vector;
    }




    const [renderer, camera, scene, clock] = boot(THREE, {
        cameraType: "perspective",
        fov: 45,
        aspect: window.innerWidth / window.innerHeight,
        near: 1,
        far: 500
    }, true);

    // Game components
    camera.position.set( 0, 0, 100 );
    camera.lookAt( 0, 0, 0 );

    //create a blue LineBasicMaterial
    const material = new THREE.LineBasicMaterial( { color: 0xff00ff } );
    const points = [];
    points.push( new THREE.Vector3( 78, 0, 0 ) );
    points.push( new THREE.Vector3( 0, 10, 0 ) );
    points.push( new THREE.Vector3( 10, 0, 0 ) );
    points.push( new THREE.Vector3( -10, 0, 0 ) );

    // Triangle 2
/*    points.push(new THREE.Vector3(-30, 2, 2));
    points.push(new THREE.Vector3(2, 30, 2));
    points.push(new THREE.Vector3(30, 2, 2));
    points.push(new THREE.Vector3(-30, 2, 2));*/


    const geometry = new THREE.BufferGeometry().setFromPoints( points );


    const line = new THREE.Line( geometry, material )
    scene.add( line );

    // Triangle 3
    const shape = new THREE.Shape();
    const x = 0;
    const y = 0;
    shape.moveTo(x - 2, y - 2);
    shape.lineTo(x + 2, y - 2);
    shape.lineTo(x, y + 2);

    const TriangleGeometry = new THREE.ShapeGeometry(shape);

    const m = new THREE.MeshBasicMaterial( { color: 0xff0000 } );
    const mesh = new THREE.Mesh( TriangleGeometry, m ) ;
    scene.add( mesh );
    mesh.position.set(-5, 15, 0);
    mesh.matrixWorldNeedsUpdate = true;

    const canvas = renderer.domElement;


    let offset = normalizeCoords(new THREE.Vector2(canvas.width / 2, 0), canvas);
    console.log(canvas.width, renderer.domElement);
    console.log(offset);
    window.offsetX = offset.x * 100;
    window.offsetY = offset.y * 100;

    window.addEventListener("mousemove", function(event) {
        let offset = normalizeCoords(new THREE.Vector2(event.clientX, event.clientY), canvas);
        window.offsetX = offset.x * 100;
        window.offsetY = offset.y * 50; // why needs half only???
        console.log(window.offsetX, window.offsetY);
    });

    let t = 0;
    function animate(_t) {
        requestAnimationFrame( animate );

        const delta = clock.getDelta();
        const time = clock.getElapsedTime();

        let newPosition = line.geometry.attributes.position.array.slice();

/*        newPosition[0] += .5;
        console.log(newPosition[0]);*/
        // newPosition[1] += 0.1;
        // newPosition[2] += 0.1;

        newPosition[0] = window.offsetX;
        newPosition[1] = window.offsetY;


        line.geometry.attributes.position.array = newPosition;

        line.geometry.attributes.position.needsUpdate = true;

        t += delta * 0.5;

        renderer.render( scene, camera );
    }
    animate();
}




