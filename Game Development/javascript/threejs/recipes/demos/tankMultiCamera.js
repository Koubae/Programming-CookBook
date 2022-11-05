import {boot}  from "../core.js";

// CONFIGS
const TARGET_MOVEMENT_LEVEL = 1;
const TARGET_CHANGE_COLOR = false;

export default function recipe(THREE) {
    /// Utilities
    function doesRendererRequiresResize(renderer) {
        const canvas = renderer.domElement;
        const width = canvas.clientWidth;
        const height = canvas.clientHeight;
        const needResize = canvas.width !== width || canvas.height !== height;
        if (needResize) {
            renderer.setSize(width, height, false);
        }
        return needResize;
    }

    function resizeRendererToDisplaySize(renderer, cameras) {
        if (doesRendererRequiresResize(renderer)) {
            const canvas = renderer.domElement;
            cameras.forEach((cameraInfo) => {
                const camera = cameraInfo.cam;
                camera.aspect = canvas.clientWidth / canvas.clientHeight;
                camera.updateProjectionMatrix();
            });
        }
    }


    const [renderer, camera, scene, clock] = boot(THREE, {
        cameraType: "perspective",
        fov: 40,
        aspect: window.innerWidth / window.innerHeight,
        near: 0.1,
        far: 1000
    }, true);
    const SKY_COLOR = `#a2d5dc`;
    renderer.setClearColor(SKY_COLOR);
    renderer.shadowMap.enabled = true;

    // ----------------- < GAME COMPONENTS > --------------------- \\
    // Main Camera
    camera.position.set( 8, 5, 15 ).multiplyScalar(3);
    camera.lookAt( 0, 0, 0 );

    // Set up worlds lights
    {
        const light = new THREE.DirectionalLight(0xffffff, 1);
        light.position.set(0, 20, 0);
        scene.add(light);
        light.castShadow = true;
        light.shadow.mapSize.width = 2048;
        light.shadow.mapSize.height = 2048;

        const d = 50;
        light.shadow.camera.left = -d;
        light.shadow.camera.right = d;
        light.shadow.camera.top = d;
        light.shadow.camera.bottom = -d;
        light.shadow.camera.near = 1;
        light.shadow.camera.far = 50;
        light.shadow.bias = 0.001;
    }

    {
        const light = new THREE.DirectionalLight(0xffffff, 1);
        light.position.set(1, 2, 4);
        scene.add(light);
    }

    // Build world
    const groundGeometry = new THREE.PlaneGeometry(150, 150);
    const groundMaterial = new THREE.MeshPhongMaterial({ color: `rgb(116, 67, 47)`});
    const groundMesh = new THREE.Mesh(groundGeometry, groundMaterial);
    groundMesh.rotation.x = Math.PI * -.5;
    groundMesh.receiveShadow = true;
    scene.add(groundMesh);


    // Build tank
    const tankWidth = 4;
    const tankHeight = 1;
    const tankLength = 8;

    const tank = new THREE.Object3D();
    tank.castShadow = true;
    scene.add(tank);

    const tankMaterial = new THREE.MeshPhongMaterial({ color: `#788492`});
    const tankBody = new THREE.Mesh(
      new THREE.BoxGeometry(tankWidth, tankHeight, tankLength),
      tankMaterial,
    );
    tankBody.position.y = 1.4;
    tankBody.castShadow = true;
    tank.add(tankBody);

    const domeRadius = 2;
    const domeWidthSubDiv = 12;
    const domeHeightSubDiv = 12;
    const domePhiStart = 0;
    const domePhiEnd = Math.PI * 2;
    const domeThetaStart = 0;
    const domeThetaEnd = Math.PI * .5;
    const domeGeometry = new THREE.SphereGeometry(
        domeRadius,
        domeWidthSubDiv,
        domeHeightSubDiv,
        domePhiStart,
        domePhiEnd,
        domeThetaStart,
        domeThetaEnd
    );
    const tankDome = new THREE.Mesh(domeGeometry, tankMaterial);
    tankDome.castShadow = true;
    tankBody.add(tankDome);
    tankDome.position.y = .5;

    const turretWidth = .1;
    const turretHeight = .1;
    const turretLength = tankLength * .75 * .2;
    const turretGeometry = new THREE.BoxGeometry(
        turretWidth,
        turretHeight,
        turretLength
    );
    const tankTurret = new THREE.Mesh(turretGeometry);
    tankTurret.castShadow = true;
    tankTurret.position.y = .2;
    tankTurret.position.z = turretLength * .5;
    const turretBase = new THREE.Object3D();
    turretBase.scale.set(5, 5, 5);
    turretBase.position.y = .5;
    turretBase.add(tankTurret);
    tankBody.add(turretBase);

    const wheelRadius = 1;
    const wheelThickness = 1.5;
    const wheelUnderCart = 1; // Determines how many pixels does the tank wheel goes under the tank cart
    const wheelSegments = 6;
    const wheelPositions = [
        [-tankWidth / 2 - wheelThickness / 2 - -wheelUnderCart, -tankHeight / 2,  tankLength / 3],
        [ tankWidth / 2 + wheelThickness / 2 - wheelUnderCart, -tankHeight / 2,  tankLength / 3],
        [-tankWidth / 2 - wheelThickness / 2 - -wheelUnderCart, -tankHeight / 2, 0],
        [ tankWidth / 2 + wheelThickness / 2 - wheelUnderCart, -tankHeight / 2, 0],
        [-tankWidth / 2 - wheelThickness / 2 - -wheelUnderCart, -tankHeight / 2, -tankLength / 3],
        [ tankWidth / 2 + wheelThickness / 2 - wheelUnderCart, -tankHeight / 2, -tankLength / 3],
    ];
    const wheelGeometry = new THREE.CylinderGeometry(
        wheelRadius,     // top radius
        wheelRadius,     // bottom radius
        wheelThickness,  // height of cylinder
        wheelSegments
    );
    const wheelMaterial = new THREE.MeshPhongMaterial({color: `#888888`});
    const wheels = wheelPositions.map(position => {
        const mesh = new THREE.Mesh(wheelGeometry, wheelMaterial);
        mesh.position.set(...position);
        mesh.rotation.z = Math.PI * .5;
        mesh.castShadow = true;
        tankBody.add(mesh)

        return mesh;
    });

    // Target
    const targetGeometry = new THREE.SphereGeometry(.5, 10, 10);
    const targetMaterial = new THREE.MeshPhongMaterial(
        {
            color: `#00FF00`,
            flatShading: true
        }
    );
    const target = new THREE.Mesh(targetGeometry, targetMaterial);
    target.castShadow = true;

    const targetOrbit = new THREE.Object3D();
    const targetElevation = new THREE.Object3D();
    const targetBob = new THREE.Object3D();

    targetElevation.position.z = tankLength * 2;
    targetElevation.position.y = 8;

    targetBob.add(target);
    targetElevation.add(targetBob);
    targetOrbit.add(targetElevation);
    scene.add(targetOrbit);


    // sine-like Curget
    const curve = new THREE.SplineCurve([
        new THREE.Vector2( -10, 0 ),
        new THREE.Vector2( -5, 5 ),
        new THREE.Vector2( 0, 0 ),
        new THREE.Vector2( 5, -5 ),
        new THREE.Vector2( 10, 0 ),
        new THREE.Vector2( 5, 10 ),
        new THREE.Vector2( -5, 10 ),
        new THREE.Vector2( -10, -10 ),
        new THREE.Vector2( -15, -8 ),
        new THREE.Vector2( -10, 0 ),
    ]);
    const points = curve.getPoints(50);
    const geometry = new THREE.BufferGeometry().setFromPoints(points);
    const material = new THREE.LineBasicMaterial({color: `#FF0000`});
    const splineObject = new THREE.Line(geometry, material);
    splineObject.rotation.x = Math.PI * .5;
    splineObject.position.y = 0.05;
    scene.add(splineObject);



    // ----------------- < CAMERAS > --------------------- \\
    function makeCamera(fov = 40) {
        const aspect = 2;  // the canvas default
        const zNear = 0.1;
        const zFar = 1000;
        return new THREE.PerspectiveCamera(fov, aspect, zNear, zFar);
    }

    const tankCamera = makeCamera(75);
    tankCamera.position.y = 3;
    tankCamera.position.z = -6;
    tankCamera.rotation.y = Math.PI;
    tankBody.add(tankCamera);

    const turretCamera = makeCamera();
    turretCamera.position.y = .75 * .2;
    tankTurret.add(turretCamera);

    const targetCamera = makeCamera();
    const targetCameraPivot = new THREE.Object3D();
    targetCamera.position.y = 1;
    targetCamera.position.z = -5;
    targetCamera.rotation.y = Math.PI;
    targetBob.add(targetCameraPivot);
    targetCameraPivot.add(targetCamera);

    const cameras = [
        { cam: camera, desc: 'detached camera', },
        { cam: turretCamera, desc: 'on turret looking at target', },
        { cam: targetCamera, desc: 'near target looking at tank', },
        { cam: tankCamera, desc: 'above back of tank', },
    ];

    let cameraUserIndex = 0;
    const infoContainer = document.createElement('div');

    infoContainer.classList.add("clean-up-required");
    infoContainer.style.cssText = `    
        position: absolute;
        left: 25em;
        top: 1em;
        background: rgba(255,255,255,1);
        padding: 2rem 6rem;
        color: black;
        text-transform: uppercase;
        font-family: monospace;
    `;
    const infoElem = document.createElement('div');
    infoElem.addEventListener("click", () => {
       cameraUserIndex++;
       if (cameraUserIndex >= cameras.length) {
           cameraUserIndex = 0;
       }
    });
    infoContainer.appendChild(infoElem);

    const radioButtonContainer = document.createElement("div");
    radioButtonContainer.innerHTML = `
    <input type="checkbox" name="cameraAutoPlay" checked="checked"/>
    <label for="cameraAutoPlay">Camera AutoPlay</label>
    `;
    let cameraAutoPlay = true;
    const radioButtonCameraAutoPlay = radioButtonContainer.querySelector("input");
    radioButtonCameraAutoPlay.addEventListener("input", () => {
        cameraAutoPlay = !cameraAutoPlay;
    });
    infoContainer.appendChild(radioButtonContainer);

    document.body.appendChild(infoContainer);

    const targetPosition = new THREE.Vector3();
    const tankPosition = new THREE.Vector2();
    const tankTarget = new THREE.Vector2();

    /// Updater
    function updateTarget(_time) {
        targetOrbit.rotation.y = _time * .30;
        targetBob.position.y = Math.sin(_time * 2) * 6;

        switch (TARGET_MOVEMENT_LEVEL) {
            case 1:
                target.rotation.x = _time * 2;
                target.rotation.y = _time * 2;
                target.rotation.z = _time * 2;
                if (TARGET_CHANGE_COLOR) {
                    targetMaterial.emissive.setHSL(_time * 10 % 60, 1, .25);
                    targetMaterial.color.setHSL(_time / .5 % 60, 1, .1);
                }
                break;
            case 2:
                target.rotation.x = _time * 5;
                target.rotation.y = _time * 10;
                target.rotation.z = _time * 2;

                if (TARGET_CHANGE_COLOR) {
                    targetMaterial.emissive.setHSL(_time * 10 % 1, 1, .25);
                    targetMaterial.color.setHSL(_time / .5 % 1, 1, .1);
                }
                break;
            case 3:
            default:
                target.rotation.x = _time * 7;
                target.rotation.y = _time * 13;
                target.rotation.z = _time * 2;
                if (TARGET_CHANGE_COLOR) {
                    targetMaterial.emissive.setHSL(_time * 10 % 1, 1, .25);
                    targetMaterial.color.setHSL(_time / .5 % 1, 1, .1);
                }
                break;

        }


    }

    function updateTank(_time) {
        const updateTime = _time * .05;
        curve.getPointAt(updateTime % 1, tankPosition);
        curve.getPointAt((updateTime + 0.01) % 1, tankTarget);

        tank.position.set(tankPosition.x, 0, tankPosition.y);
        tank.lookAt(tankTarget.x, 0, tankTarget.y);

        // Update Tank Turret
        target.getWorldPosition(targetPosition);
        turretBase.lookAt(targetPosition);
        // Point Turret Camerat at Target
        turretCamera.lookAt(targetPosition);

        // make the targetCameraPivot look at the at the tank
        tank.getWorldPosition(targetPosition);
        targetCameraPivot.lookAt(targetPosition);

        // Rotate Tank wheels
        wheels.forEach((obj) => {
            obj.rotation.x = _time * 5;
        });
    }



    function update(_time) {
        _time *= 0.001;  // time in seconds
        resizeRendererToDisplaySize(renderer, cameras);

        // Game Logic

        // Update Target
        updateTarget(_time);
        // Update Tank
        updateTank(_time);

        let cameraIndex;
        if (cameraAutoPlay) {
            cameraIndex = _time * .25 % cameras.length | 0;
            cameraIndex += cameraUserIndex;
            if (cameraIndex >= cameras.length) {
                cameraIndex = 0;
            }
        } else {
            cameraIndex = cameraUserIndex;
        }


        const _camera = cameras[cameraIndex];
        infoElem.textContent = `
        Current Camera: ${++cameraIndex}
        Camera Name: ${_camera.desc}
        `;


        renderer.render( scene, _camera.cam );
        requestAnimationFrame( update );
    }
    requestAnimationFrame( update );
}




