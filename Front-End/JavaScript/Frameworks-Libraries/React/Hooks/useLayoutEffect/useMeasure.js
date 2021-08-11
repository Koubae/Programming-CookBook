/*
    Simple Form Hook logic encapsulation
    Credit: https://www.youtube.com/watch?v=f687hBjwFcM   (55:00)
*/

import React, { useState, useLayoutEffect } from "react";

const useMeasure = (deps) => {
    const [react, setReact] = useState({data: null, loading: true});
    const elRef = useRef();

    useLayoutEffect(() =>{
        setReact(elRef.current.getBoundingClientRect());

    }, deps);

return [rect, elRef];
}

const App = () => {
    const [rect, elRef] = useMeasure([]);

return (
    <div>
        <div>
            <h1 ref={ elRef }>HEllo Word</h1>
        </div>
    
    </div>

)};

export default App;