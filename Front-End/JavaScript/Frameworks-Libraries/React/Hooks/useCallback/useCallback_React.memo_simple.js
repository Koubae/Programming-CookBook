/*
    Simple Form Hook logic encapsulation
    Credit: https://www.youtube.com/watch?v=f687hBjwFcM   (1:05:00)
*/

import React, { useState, useCallback } from "react";

const useCountRenders = () => {
    const rensers = useRef(0);
    console.log(`Renders: ${renders.current++}`);
};

const Square = React.memo( ({ increment }) => {
    useCountRenders();

    return <button onClick={ () => increment(n)}> { n } </button>
});


const App = () => {
    const [count, SetCount] = useState(0);
    const favNums = [1, 2, 3];

    const increment = useCallback(n => {    // Function incapsulated is memoized untill dependencies (setCount) change
        setCount(c => c + n);
    }, [setCount]);

return (
    <div>
        <div>
            <h1 ref={ elRef }>HEllo Word</h1>
            <div>count: { count } </div>
            {
                favNums.map( n => {
                    return <Square increment={ increment } n={n} key={n} />
                })
            }
        </div>
    
    </div>

)};

export default App;