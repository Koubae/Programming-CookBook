/*
    Simple Form Hook logic encapsulation
    Credit: https://www.youtube.com/watch?v=f687hBjwFcM   (30:00)
*/

import React, { useEffect, useState } from "react";

const useFetch = (url) => {
    const [state, setState] = useState({data: null, loading: true});

    useEffect(() =>{
        setState( state => ( { data: state.data, loading: true}));

        fetch(url)
            .then(x => x.text())
            .then(y => {
                setState({ data: y, loading: true});
            });

    }, [url, setState]);

return state;
}

const App = () => {
    const [data, loading] = useFetch("http://numbersapi.com/1/trivia");

return (
    <div>
        <div>{ !data ? "loading..." : data }</div>
    
    </div>

)};

export default App;