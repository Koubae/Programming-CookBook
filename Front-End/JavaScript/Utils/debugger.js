/*
    Simple JavaScript Debugger
    
    @Author: iTundra.com
    @Company: Tamarack Management SL
    @Credit: Federico Baù
    @Date: 2 - February 2021

    Version: 1.0
    
*/ 

/*
.1 Console log + CSS style
.2 tables
.3 Create a tracer with console.trace

*/

// ========================= < CSS Style > ========================= // 

var NULL_CSS = {
    color: "white",
    background_color: 'fuchsia',
    font_family: 'sans-serif',
    text_shadow: '2px 2px 4px white ',
    font_size: '15px',
    font_weight: '400',
    text_decoration: 'none',
    display: 'inline-block',
    padding: '3px 8px',
    border: 'none',
    border_radius: '5px'
}

var UNDEFINED_CSS = {
    color: "yellowgreen",
    background_color: 'black',
    font_family: 'sans-serif',
    text_shadow: '2px 2px 4px white ',
    font_size: '15px',
    font_weight: '400',
    text_decoration: 'none',
    display: 'inline-block',
    padding: '3px 8px',
    border: 'none',
    border_radius: '5px'
}

var DEFAULT_CSS = {
    color: "white",
    background_color: 'black',
    font_family: 'american typewriter',
    text_shadow: '2px 2px 4px white ',
    font_size: '15px',
    font_weight: '400',
    text_decoration: 'none',
    display: 'inline-block',
    padding: '0',
    border: 'none',
    border_radius: '0'


}

function createCSS_String(defaultCss) {
    css_style = typeof defaultCss !== 'undefined' ? defaultCss : DEFAULT_CSS;

    cssString = `
    color: ${css_style['color']};
    background-color: ${css_style['background_color']};
    font-familiy: ${css_style['font_family']};
    text-shadow: ${css_style['text_shadow']};
    font-size: ${css_style['font_size']};
    font-weigth: ${css_style['font_weight']};
    text-decoration: ${css_style['text_decoration']};
    display: ${css_style['display']};
    padding: ${css_style['padding']};
    border: ${css_style['border']};
    border-radius: ${css_style['border_radius']};
    `
    return (cssString);
};


// ========================= < Console Proxy handler > ========================= // 

function isObject(val) {
    if (val === null) {return false;}
    return ( (typeof val === 'function') || (typeof val === 'object'));
}

function consoleProxy(functionType, css, ...args) {

    let consoleFunctionMap = {
        log: console.log,
        info: console.info,
        debug: console.debug,
        dir: console.dir,
        group: console.group,
        table: console.table,
        trace: console.trace,
        warn: console.warn
    };
    let functionToUse = consoleFunctionMap[functionType]

    if (functionType === 'dir') return functionToUse(args[0]);
    else {
        const CSS_VALUE = css;
        const RESET_INPUT = "%c ";
        const RESET_CSS = "";
        var inputs = [];
        var modifiers = [];
        for ( var i = 0 ; i < args.length ; i++ ) {        

            var current_value = args[ i ];  // Check current Value
            if (isObject(current_value) || Array.isArray(current_value)) {
                inputs.push( "%o", RESET_INPUT );
                modifiers.push( current_value, RESET_CSS );
            }   
            
            else if (current_value === null){  // Add Style to Null items
                const css = createCSS_String(NULL_CSS);
                inputs.push( ( "%c" + current_value ), RESET_INPUT );
                modifiers.push(css, RESET_CSS );
            }
            
            else if (current_value === undefined){ // Add style to undefined
                const css = createCSS_String(UNDEFINED_CSS);
                inputs.push( ( "%c" + current_value ), RESET_INPUT );
                modifiers.push(css, RESET_CSS );
            }

            // TODO: Add Int | Float | Date handlers

            else { // Any other item not listed Above
                inputs.push( ( "%c" + current_value ), RESET_INPUT );
                modifiers.push( CSS_VALUE, RESET_CSS );
            }
        }

        functionToUse( inputs.join( "" ), ...modifiers ); // Runs the actual Function

    }

}



// ========================= < Document's Method Customized > ========================= // 

/*
    These function are just a wrapper around the typical console's functions.

    The main reason is to have some syntax sugar and type faster.
    In additiona the style is changes in each variable css.

*/

// TODO: Add more console's Methods.
// https://developer.mozilla.org/en-US/docs/Web/API/console#usage

const Echo = function(...args) {

    const css = createCSS_String();
    consoleProxy('log', css, ...args);
}


const Info = function(...args) {
    
    css_ = Object.assign({}, DEFAULT_CSS); // HACK: Shallow Copy of Object.
    css_.background_color = '#f0fc03'
    css_.color = 'black';
    css_.padding = '3px 8px';
    css_.border_radius = '5px';
    const css = createCSS_String(css_);    
    consoleProxy('info', css, ...args);
}


const Debug = function(...args) {

    const css = createCSS_String();
    consoleProxy('debug', css, ...args);
}


const Dir = function(...args) {

    const css = createCSS_String();
    consoleProxy('dir', css, ...args);
}


const Group = function(...args) {

    const css = createCSS_String();
    consoleProxy('group', css, ...args);
}


const Table = function(...args) {

    const css = createCSS_String();
    consoleProxy('table', css, ...args);
}


const Trace = function(...args) {

    const css = createCSS_String();
    consoleProxy('trace', css, ...args);
}


const Warn = function(...args) {

    const css = createCSS_String();
    consoleProxy('warn', css, ...args);
}


// ========================= < Functions debuggers > ========================= //
var object = {name: "name", int: 10};

function showSequence(sequence, line_start, line_stop) {

    line_start = typeof line_start !== 'undefined' ? line_start : ' #';
    line_stop = typeof line_stop !== 'undefined' ? line_stop : ' #';
    let liner = "========================================== "
    if (sequence === 'Array') { // Array

        Info(liner + line_start);
        sequence.forEach(function (value, index) {
            Echo(`${index}) ${value}`);
            Echo('-------------------');
        });
        Info(liner + line_stop);
    } 
    else if ( isObject(sequence)) { // Objer or Function
        const keys = Object.keys(sequence);
        Info(liner + line_start);
        Warn(sequence);
        keys.forEach((key, index) => {
            Echo(`${index}) ${key}: ${sequence[key]}`);
            Echo('-------------------');
        });
        Info(liner + line_stop);
    } else {
        Echo(liner + line_start);
        Warn("Item is not a sequence!");
        Info(`Item passed: ${sequence}`);
        Echo(liner + line_stop);
    }   
}
