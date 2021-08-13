// CREDIT: https://usehooks.com/useAsync/

import React, { useState, useEffect, useCallback } from "react";
// Usage
function App() {
    const { execute, status, value, error } = useAsync(myFunction, false);
    return (
        <div>
        {status === "idle" && <div>Start your journey by clicking a button</div>}
        {status === "success" && <div>{value}</div>}
        {status === "error" && <div>{error}</div>}
        <button onClick={execute} disabled={status === "pending"}>
            {status !== "pending" ? "Click me" : "Loading..."}
        </button>
        </div>
    );
}
// An async function for testing our hook.
// Will be successful 50% of the time.
const myFunction = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
        const rnd = Math.random() * 10;
        rnd <= 5
            ? resolve("Submitted successfully 🙌")
            : reject("Oh no there was an error 😞");
        }, 2000);
    });
};
// Hook
const useAsync = (asyncFunction, immediate = true) => {
    const [status, setStatus] = useState("idle");
    const [value, setValue] = useState(null);
    const [error, setError] = useState(null);
    // The execute function wraps asyncFunction and
    // handles setting state for pending, value, and error.
    // useCallback ensures the below useEffect is not called
    // on every render, but only if asyncFunction changes.
    const execute = useCallback(() => {
        setStatus("pending");
        setValue(null);
        setError(null);
        return asyncFunction()
        .then((response) => {
            setValue(response);
            setStatus("success");
        })
        .catch((error) => {
            setError(error);
            setStatus("error");
        });
    }, [asyncFunction]);
    // Call execute if we want to fire it right away.
    // Otherwise execute can be called later, such as
    // in an onClick handler.
    useEffect(() => {
        if (immediate) {
        execute();
        }
    }, [execute, immediate]);
    return { execute, status, value, error };
};