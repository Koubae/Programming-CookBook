var dom = document.getElementById('mainHolder');
dom.style.backgroundImage = '-moz-linear-gradient('
        + orientation + ', ' + colorOne + ', ' + colorTwo + ')';


// Detect which browser prefix to use for the specified CSS value
// (e.g., background-image: -moz-linear-gradient(...);
//        background-image:   -o-linear-gradient(...); etc).
//

function getCssValuePrefix()
{
    var rtrnVal = '';//default to standard syntax
    var prefixes = ['-o-', '-ms-', '-moz-', '-webkit-'];

    // Create a temporary DOM object for testing
    var dom = document.createElement('div');

    for (var i = 0; i < prefixes.length; i++)
    {
        // Attempt to set the style
        dom.style.background = prefixes[i] + 'linear-gradient(#000000, #ffffff)';

        // Detect if the style was successfully set
        if (dom.style.background)
        {
            rtrnVal = prefixes[i];
        }
    }

    dom = null;
    delete dom;

    return rtrnVal;
}

// Setting the gradient with the proper prefix
dom.style.backgroundImage = getCssValuePrefix() + 'linear-gradient('
        + orientation + ', ' + colorOne + ', ' + colorTwo + ')';