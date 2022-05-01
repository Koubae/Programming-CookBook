var log = console.log;


function scrollEffect() 
{
    // --------------------- PARALLAX WITH SCROLL EVENT EFFECT 
    //-> Credit: https://stackoverflow.com/a/46636115/13903942
    function parallaxEffect() {
        
        var parallax = document.querySelectorAll(".parallax_two");
        var speed = .5; 


        function isInYViewport(element) {
            /**
             * HACK Function, Check if Element is in the Client View Port
             * @param element {DOM Element}
             * Credit: https://www.javascripttutorial.net/dom/css/check-if-an-element-is-visible-in-the-viewport/
             */
            const rect = element.getBoundingClientRect();
            const vh = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0)

            // if top is positive we still at the Top of the IMG, if Negative, the Client Top View Port has been passed
            // Using the Abs value we can flip the negative value so that is still True 
            return Math.abs(rect.top) <= Math.abs(vh);
        }


        [].slice.call(parallax).forEach(function(el, _) {

            let isElementInView = isInYViewport(el);
            if (!isElementInView) return;

            var elYOffSet = el.getBoundingClientRect().top;
            const vh = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0)
            var elBackgrounPos = "50%" + ((elYOffSet-vh) * speed) + "px";
            el.style.backgroundPosition = elBackgrounPos;
        })
    }

    // ----------- NOTE: Creating New Node as Parent Node, also attach all the current note
    // so that the Scroll Event listener won't be on the Body but to the new Created parent Node: Credit -> https://stackoverflow.com/a/15592944/13903942

    let DOM_ROOT$ = document.createElement("div");
    DOM_ROOT$.className = 'div__body';
    DOM_ROOT$.id = 'DOM_ROOT$'; 

    // document -> HTML -> #test (before Body)
    let HTMLNodes = document.childNodes[1].childNodes;
    for (let i = 2; i < HTMLNodes.length; i++) {
        DOM_ROOT$.appendChild(HTMLNodes.item(i));
        HTMLNodes.item(0).parentNode.insertBefore(DOM_ROOT$, HTMLNodes.item(i));
    }
    window.addEventListener('scroll', parallaxEffect);

}

window.addEventListener('DOMContentLoaded', scrollEffect);
