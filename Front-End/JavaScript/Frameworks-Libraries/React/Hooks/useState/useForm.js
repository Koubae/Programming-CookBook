/*
    Simple Form Hook logic encapsulation
    Credit: https://www.youtube.com/watch?v=f687hBjwFcM   (14:00)
*/

import React, { useState } from "react";

const useForm = (formValues) => {
    const [values, setValues] = useState(formValues);

return [
    values, 
    e => {
        setValues({
            ...values, 
            [e.target.name]: e.target.value
        })
    }
]
}

const App = () => {
    const [values, handleChange] = useForm({email: "", password: ""});

return (
    <div>
        <input name="email" value={values.email} onChange={ handleChange}/>
        <input name="password" type="password" value={values.email} onChange={ handleChange}/>
    
    </div>

)};

export default App;