/*
    Simple Form Hook logic encapsulation
    Credit: https://www.youtube.com/watch?v=f687hBjwFcM   (1:32:00)
*/

import React, { useReducer } from "react";

function reducer(state, action) {

    switch(action.type) {

        case 'ADD-TODO':
            return {
                todos: [...state.todos, { text: action.text, completed: false}],
                todoCount: state.todoCount + 1
            };
        case 'TOGGLE-TODO':
            return {
                todos: state.todos.map( (t, idx) =>
                    idx === action.idx ? { ...t, completed: !t.completed } : t
                ),
                todoCount: state.todoCount 
            };
        default:
            return state;
    }
};


const App = () => {
    const [{ todos, todoCount}, dispatch] = useReducer( reducer, {
        todos: [],
        todoCount: 0
    });
    const [text, setText] = useState();

return (
    <div>
        <form
            onSubmit={ e => {
                e.preventDefault();
                dispatch( { type: "ADD-TODO", text});
                setText("");
            }}
        >
            <input value={text} onChange={ e => setText(e.target.value)}/>
        </form>

        <div> Number of Todos: { todoCount }</div>
        {
            todos.map( (t, idx) => (
                <div
                    key={t.text}
                    onClick={ () => dispatch({type: 'TOGGLE-TODO', idx})}
                    style={{textDecoration: t.completed ? 'line-through': ''}}
                >
                    {t.text}
                </div>
            ))
        }
    
    </div>

)};

export default App;