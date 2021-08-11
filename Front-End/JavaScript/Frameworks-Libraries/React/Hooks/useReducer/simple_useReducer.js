/*
    Simple Form Hook logic encapsulation
    Credit: https://www.youtube.com/watch?v=f687hBjwFcM   (1:21:00)
*/

import React, { useReducer } from "react";

function reducer(state, action) {

    switch(action.type) {

        case 'INCREMENT':
            return state + 1; // Don't use ++ but re-create a new Var
        case 'DECREMENT':
            return state - 1; // Don't use -- but re-create a new Var
        default:
            return state;
    }
};


const App = () => {
    const [count, dispatch] = useReducer(reducer, 0);

return (
    <div>
        <div>count: { count }</div>
        <button onClick={ () => dispatch({ type: "INCREMENT"})}>Increment</button>
        <button onClick={ () => dispatch({ type: "DECREMENT"})}>Decrement</button>
    
    </div>

)};

export default App;