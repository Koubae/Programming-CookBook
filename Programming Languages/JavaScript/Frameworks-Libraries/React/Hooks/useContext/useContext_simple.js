/*
    Simple Form Hook logic encapsulation
    Credit: https://www.youtube.com/watch?v=f687hBjwFcM   (1:40:00)

    Using React Router
*/

import React, { createContext, useMemo, useContext } from "react";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

const UserContext = createContext(null);

function About() { 
    const { value, setValue} = useContext(UserContext)    
return(
    <div>
        <h2>about</h2>
        <div>{ value }</div>
    </div>
)}

function Index() { 
    const { value, setValue} = useContext(UserContext)    
return(
    <div>
        <h2>Home</h2>
        <div>{ value }</div>
        <button onClick={() => setValue("Hey")}>Change Value</button>
    </div>
)}

const AppRouter = () => {
    const [value, setValue] = useState("Hello from Context Consumer");
    const providerValue = useMemo(() => ({value, setValue}, [value, setValue]));
return (
    <Router>
        <div>
            <nav>
                <ul>
                    <li>
                        <Link to="/">Home</Link>
                    </li>

                    <li>
                        <Link ti="/about/">About</Link>
                    </li>

                </ul>
            </nav>

            <UserContext.Provider value={ providerValue }>
                <Route path="/" exact component={ Index }/>
                <Route path="/about/" exact component={ About }/>
            </UserContext.Provider>
        </div>
    
    </Router>

)};

export default AppRouter;