/*
    Simple Form Hook logic encapsulation
    Credit: https://www.youtube.com/watch?v=f687hBjwFcM   (1:40:00)

    Using React Router
*/

import React, { createContext, useMemo, useContext } from "react";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

const UserContext = createContext(null);

async function login() {
    return {
        id: 1, 
        username: "bob",
        email: "bob@bob.com"
    }
}
function About() { 
    const { user, setUser} = useContext(UserContext)    
return(
    <div>
        <h2>about</h2>
        <div><pre> { JSON.stringify(user, null, 2) } </pre></div>
    </div>
)}

function Index() { 
    const { user, setUser} = useContext(UserContext)    
return(
    <div>
        <h2>Home</h2>
        <div><pre> { JSON.stringify(user, null, 2) } </pre></div>
        {
            user ? 

            <button onClick={async () => {
                const user = await login();
                setUser(null);
            }}>Logout</button>
            :
            <button onClick={async () => {
                const user = await login();
                setUser(user);
            }}>Login</button>
        }

    </div>
)}

const AppRouter = () => {
    const [user, setUser] = useState("Hello from Context Consumer");
    const providerValue = useMemo(() => ({user, setUser}, [user, setUser]));
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