import {boot}  from "../core.js";

function getRandomNumber(range) {
    return Math.random() - range;
}

function clamp(value, type = "") {
    switch (type) {
        case "full height":
            if (value > -1) return -1;
            if (value < 1) return 1;
            return value;
        case "margin":
            let margin = .2;
            if (value < 0) {
                if (value < -margin) return -margin;
            } else {
                if (value > margin) return margin;
            }


            return value;
        default:
            if (value < 0) {
                if (value < -1) return -1;
            } else {
                if (value > 1) return 1;
            }
            return value;
    }


}

export default function recipe(THREE) {
    const [renderer, camera, scene] = boot(THREE, {
        cameraType: "perspective",
        fov: 75,
        aspect: window.innerWidth / window.innerHeight,
        near: 0.1,
        far: 1000
    });

    // Game components
    const POINTS = 100;
    const DIMENSION = 3; // Number of Dimension of the Points, example 3 = x,y,z
    const POSITION_MULTIPLIER = 30;
    const positions = new Float32Array(POINTS * DIMENSION);  // Initialize 3 positions for each point to 0.00

    const geometry = new THREE.BufferGeometry();
    geometry.setAttribute("position", new THREE.BufferAttribute(positions, DIMENSION));


    // draw
    let drawCount = 2; // draw first 2 points
    geometry.setDrawRange(0, drawCount);

    // material
    const material = new THREE.LineBasicMaterial({ color: 0xff0000});
    // Mash Line
    const line = new THREE.Line(geometry, material);
    scene.add(line);
    lineUpdatePosition(line);

    /**
     * Updates randomly the position of a line
     * @param {THREE.Line} entity
     */
    function lineUpdatePosition(entity, reset = false) {
        const positions = entity.geometry.attributes.position.array;
        let x = 0;
        let y = 0;
        let z = 0;
        let index = 0;

        for ( let i = 0, l = POINTS; i < l; i ++ ) {
            positions[ index ++ ] = x;
            positions[ index ++ ] = y;
            positions[ index ++ ] = z;
            if (reset) {
              /*  x = ( getRandomNumber(.5) ) * POSITION_MULTIPLIER;
                y = ( getRandomNumber(.5) ) * POSITION_MULTIPLIER;
                z = ( getRandomNumber(.5) ) * POSITION_MULTIPLIER;*/

                x += ( Math.random() - 0.5 ) * 30;
                y += ( Math.random() - 0.5 ) * 30;
                z += ( Math.random() - 0.5 ) * 30;

               /* x = clamp(x, );
                y = clamp(y, );
                z = clamp(z, );*/

            } else {
              /*  x += ( getRandomNumber(.5) ) * POSITION_MULTIPLIER;
                y += ( getRandomNumber(.5) ) * POSITION_MULTIPLIER;
                z += ( getRandomNumber(.5) ) * POSITION_MULTIPLIER;*/
                x += ( Math.random() - 0.5 ) * 30;
                y += ( Math.random() - 0.5 ) * 30;
                z += ( Math.random() - 0.5 ) * 30;
            }
        }

        entity.geometry.computeBoundingBox();
        entity.geometry.computeBoundingSphere();
        line.geometry.attributes.position.needsUpdate = true; // required after the first render
        line.material.color.setHSL( Math.random(), 1, 0.5 );

    }


    function animate(time) {
        requestAnimationFrame( animate );

        drawCount = ( drawCount + 1 ) % POINTS ;
        //console.log(drawCount);
        line.geometry.setDrawRange( 0, drawCount );
        if ( drawCount === 0 ) {
            lineUpdatePosition(line, true); // periodically, generate new data
        }

        renderer.render( scene, camera );

    }
    animate();
}



