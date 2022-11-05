import {boot}  from "../core.js";

export default function recipe(THREE) {
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
    points.push( new THREE.Vector3( - 10, 0, 0 ) );
    points.push( new THREE.Vector3( 0, 10, 0 ) );
    points.push( new THREE.Vector3( 10, 0, 0 ) );

    const geometry = new THREE.BufferGeometry().setFromPoints( points );


    const line = new THREE.Line( geometry, material )
    scene.add( line );


    let t = 0;
    function animate(_t) {
        requestAnimationFrame( animate );

        const delta = clock.getDelta();
        const time = clock.getElapsedTime();

        line.rotation.x = time * 0.25;
        line.rotation.y = time * 0.5;
        line.rotation.z = time * 0.5;

        // Update the position randomly
        /*let newPosition = line.geometry.attributes.position.array.map(l => {
           l += 0.1;
           if (l > 50) {
               l = 0;
           }
           return l;
        });*/

        // Update only preciy points
        let newPosition = line.geometry.attributes.position.array.slice();

        newPosition[0] += 0.1;
        newPosition[1] += 0.1;
        newPosition[2] += 0.1;
        if (newPosition[0] > 20) {
            newPosition[0] = 0;
        }
        if (newPosition[1] > 20) {
            newPosition[1] = 0;
        }
        if (newPosition[2] > 20) {
            newPosition[2] = 0;
        }

        newPosition[3] -= 0.1;
        newPosition[4] -= 0.1;
        newPosition[5] -= 0.1;
        if (newPosition[3] > -20) {
            newPosition[3] = 0;
        }
        if (newPosition[4] > -20) {
            newPosition[4] = 0;
        }
        if (newPosition[5] > -20) {
            newPosition[5] = 0;
        }

        line.geometry.attributes.position.array = newPosition;

        line.geometry.attributes.position.needsUpdate = true;

        t += delta * 0.5;

        renderer.render( scene, camera );
    }
    animate();
}




