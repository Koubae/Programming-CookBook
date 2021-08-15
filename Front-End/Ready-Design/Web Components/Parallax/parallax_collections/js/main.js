// ============================== < UTILS > ====================================== \\ 

var log = console.log;

function rand(min, max) {
    let randomNum = Math.random() * (max - min) + min;
    return Math.floor(randomNum);
}


// ============================== < WEB COMPONENTS > ====================================== \\ 


function WebComponentsInit () 

{
    // ------- Handle Navbar
    let navBar = document.getElementsByClassName("nav-main")[0];
    let body = document.getElementsByTagName("body");

    const SCROLLDOWN = "nav-scroll-down";
    const navBarPosition = navBar.offsetTop;
    const BREAKPOINT_TOP = navBarPosition + 150;
   
    function showNavBarScroll() {  // Scroll Handle
        let currentPosition = window.pageYOffset;        
        if (currentPosition > BREAKPOINT_TOP) {
            navBar.classList.add(SCROLLDOWN);
        } else if (currentPosition <= BREAKPOINT_TOP && navBar.classList.contains(SCROLLDOWN)) {
            navBar.classList.remove(SCROLLDOWN); 
        }  
    }   
    Array.from(body).forEach((el) => {el.addEventListener("scroll", showNavBarScroll, false )});

    function showNavBarMouseMove(event) {  // Mouse Position Handle
        let currentPosition = window.pageYOffset;
        let mouseY = event.pageY;
        const BREAKPOINT = currentPosition + 100;
        if (mouseY <= BREAKPOINT) {
            if (navBar.classList.contains(SCROLLDOWN)) {
                navBar.classList.remove(SCROLLDOWN);
            }
        } else if (currentPosition > BREAKPOINT_TOP){
            navBar.classList.add(SCROLLDOWN);
        }    
    }
    window.addEventListener("mousemove", showNavBarMouseMove, false); 


    // ------- DropDown
    var dropDown = document.querySelectorAll(".dropdown");

    dropDown.forEach((dropdown)=> {
        dropdown.addEventListener("mouseenter", dropDownToggle);
        dropdown.addEventListener("mouseleave", dropDownToggle);
    })

    function dropDownToggle(event) {
        let dropDownWrapper = event.target.lastElementChild.firstElementChild;
        if (dropDownWrapper.classList[0] === "dropdown-wrapped") {
            dropDownWrapper.classList.toggle("dropdown-show")
            } 
    }

    // Make the Logo have functionality of an HyperLink, I don't want to add a HyperLink as wrapper of img because will break the Navbar style
    let logoHyper = document.getElementById("logoHyper");
    if (logoHyper !== null) logoHyper.addEventListener("click", ()=> { window.location = "index.html"; })

    let logoHyperBeginner1 = document.getElementById("logoHyperBeginner1");
    if (logoHyperBeginner1 !== null) logoHyperBeginner1.addEventListener("click", ()=> { window.location = "../index.html"; })

}

window.addEventListener('DOMContentLoaded', WebComponentsInit);


// ============================== < playBoxOne > ====================================== \\ 

let playBoxOne = document.getElementById("playBoxOne");
let buttonRGB = document.getElementById("buttonPlayBoxOneRGB");
let buttonHEX = document.getElementById("buttonPlayBoxOneHex");

if (buttonRGB !== null) buttonRGB.addEventListener("click", randBackgroundRGB);
if (buttonHEX !== null) buttonHEX.addEventListener("click", randBackgroundHEX);

let RGBMAX = 255;

function randBackgroundRGB () {
    let red = rand(0, RGBMAX);
    let green = rand(0, RGBMAX);
    let blue = rand(0, RGBMAX);
    let alpha = rand(0, 10);

    function alphanize(alpha) {
        // Having Integer betwen 0 - 10. For Int between 1 - 9 we want to turn them into 0.[num] for ALPHA values. (0 - 1)
        if (alpha == 10) {
            return 1;
        } else if (alpha == 0) {
            return 0;
        } else {
            let newAlpha = '0.' + (alpha + '');
            return parseFloat(newAlpha);
        }
    }

    function unscramble(color) {
        // Function used to set an oppsite color in order to set it to the rgbValue Color style

        let currentColor = color.split(",");
        let red, green, blue;
        for (let i = 0; i<3; i++) {
            let current = currentColor[i];
            let newC;
            if (parseInt(current) >= 127) {
                newC = parseInt(currentColor[i]) - 127;
            } else {
                newC = parseInt(currentColor[i]) +  127;
            }
            if (i == 0) red = newC;
            else if (i == 1) green = newC;
            else if (i == 2) blue = newC;
            
        }     
        let newColor = [parseInt(red), parseInt(green), parseInt(blue)].join(',');
        return newColor;
    }
    alpha = alphanize(alpha);    
    rgbColorValue = [parseInt(red), parseInt(green),parseInt(blue),alpha].join(',')
    playBoxOne.style.backgroundColor = `rgba(${rgbColorValue})`;
    let rgbValue = document.getElementById("rgbaValue");

    let newColor = unscramble(rgbColorValue);
    rgbValue.textContent = `RGBA(${rgbColorValue})`;
    rgbValue.style.color = `rgb(${newColor})`;
}


function randBackgroundHEX () {
    let red = rand(0, RGBMAX);
    let green = rand(0, RGBMAX);
    let blue = rand(0, RGBMAX);
    var colorsHEX = [red.toString(16).toUpperCase(), green.toString(16).toUpperCase(), blue.toString(16).toUpperCase()].join('')
    
    playBoxOne.style.backgroundColor = `#${colorsHEX}`;

    let hexValue = document.getElementById("hexValue");
    hexValue.textContent = `#${colorsHEX}`;
    

}

// ====================================== < ************** > ====================================== \\ 
/*
    ---------------------------------------    CAROUSEL    ---------------------------------------
*/
// ====================================== < ************** > ====================================== \\ 


// ============================== < carouselOne > ====================================== \\ 

let carouselOneConfigs = {
    picNum: new Set,
    picURL: [],
    offSetStart: 1,
    offSetEnd: 100,
    cursor: null,
    curorValue: function (value) {
        this.cursor += value;
    },
    reset: function() {
        this.picNum.clear();
        this.picURL.length = 0;
        this.offSetStart += 100;
        this.offSetEnd += 100;
    }
}

function setCursorIndex(stackNext) {
    
    let setCursor = carouselOneConfigs.curorValue.bind(carouselOneConfigs);
    // 1. If First pic Set Index to 0 
    if (carouselOneConfigs.picURL.length == 1) setCursor(0); 
    else if (stackNext == 'stackDown') setCursor(-1); 
    else if(stackNext == 'stackUp') setCursor(1); 

}

function carouselMovePictureEvent (target) {
    /**
     * Random Picture Request Event Handler 
    */   

    let arrow = target.currentTarget;  
    let targetCarousel = arrow.carouselContainer;
    if (!(targetCarousel.firstElementChild.dataset.playBox == "carouselOne")) return;

    const PICSUMS_URL_ROOT = "https://picsum.photos/"
    const DEFAULT_PIC_SIZE = "800/600"
    const RANDOM = "random="
    let image = targetCarousel.lastElementChild;

    function init()  {
        /** Check If was the First Time Called (or it was Reset Passed the offSetEnd), so we Push the Main Picture to The Stack
         * 
         */

        let firstPicNum = image.src.split('=')[1];
        carouselOneConfigs.picNum.add(parseInt(firstPicNum));
        carouselOneConfigs.picURL.push(image.src);
        setCursorIndex("stackUp");
    }   
    if (!(carouselOneConfigs.picURL.length)) init();

    function setPictureURL() {
        image.src = carouselOneConfigs.picURL[carouselOneConfigs.cursor];
    }

    function requestNewPicture() {
        let request = true;
        index = 0;
        while (request) {
            // ------------- RESET STATUS
            request = index == 50 ? false : true; // Avoid Go over 50 Loops
            if (carouselOneConfigs.picNum.size == 100) {
                carouselOneConfigs.reset.call(carouselOneConfigs);  
                init();             
            }

            let num_rand = rand(carouselOneConfigs.offSetStart, carouselOneConfigs.offSetEnd);
            if (!carouselOneConfigs.picNum.has(num_rand)) {
                let newPictUrl = PICSUMS_URL_ROOT + DEFAULT_PIC_SIZE + '?'  + RANDOM + num_rand;
                image.src = newPictUrl;
                carouselOneConfigs.picNum.add(num_rand);
                carouselOneConfigs.picURL.push(newPictUrl);
                break;
            } 
            index ++;  
        }
        setCursorIndex("stackUp");
    }

    function moveCarouselLeft() {     
        setCursorIndex("stackDown");
        setPictureURL();
        return;
    }

    function moveCarouselRight() {       
        setCursorIndex("stackUp");
        setPictureURL();      
    }   
    let isLeftArrow = arrow.classList.contains('carousel-arrow-left');
    let cursor = carouselOneConfigs.cursor;
    let totalPics = carouselOneConfigs.picURL.length;

    // --------------------- Handle Stack Left Movement First
    if (isLeftArrow && !cursor == 0 || !cursor == undefined) moveCarouselLeft();
    else if (isLeftArrow && cursor == 0 || cursor == undefined) return;
    // --------------------- Check if we should Request A Picture
    else if ((cursor+1) == totalPics || totalPics == 0) requestNewPicture();
    // --------------------- Finally Handle Right Stack Movement
    else if (cursor > totalPics) carouselOneConfigs.cursor = totalPics;
    else if (cursor < totalPics) moveCarouselRight();
}

window.addEventListener('load', () => {
    
    let carouselWidget = document.querySelectorAll(".carousel-widget");
    if (carouselWidget !== null) {

        carouselWidget.forEach((carousel)=> {
            let carouselContainer = carousel.children[1];
            let arrowLeft = carousel.firstElementChild;
            let arrowRight = carousel.lastElementChild;
            
            // --------------------------- EVENTS 
            if (arrowLeft !== null)  arrowLeft.addEventListener("click", carouselMovePictureEvent);
            if (arrowRight !== null)  arrowRight.addEventListener("click", carouselMovePictureEvent);
            // ---------------------------

            // --------------------------- APPLY STYLE (Set Arrows box at the Middle of the carouselContainer depending on the Client's screen size)
            arrowLeft.carouselContainer = carouselContainer;
            arrowRight.carouselContainer = carouselContainer;

            let carouselHeight = carouselContainer.clientHeight;
            let arrowHeight = arrowLeft.clientHeight;
            let arrowWidth = arrowLeft.clientWidth;
            
            let arrowHeightPosition = (carouselHeight / 2) - (arrowHeight / 2);
            arrowLeft.style.top = `${arrowHeightPosition}px`;
            arrowRight.style.top = `${arrowHeightPosition}px`;
            
            let arrowWidthPosition =  (carousel.offsetWidth - carouselContainer.offsetWidth) - (arrowWidth + (arrowWidth/2.5));
            arrowLeft.style.left = `${arrowWidthPosition}px`;
            arrowRight.style.left = `-${arrowWidthPosition}px`;
            // ---------------------------            
        })
    }
})


// ============================== < carouselTwo > ====================================== \\


const carouselMove = (slide, direction) => {
    
    const slides = slide.allSlides;
    let distance = direction.distance;
    let current_node = direction.current_node;
    let next_node = direction.next_node;
    
    slides.forEach(($slide) => {          
        $slide.style.transform = `translate(-${distance}px)`

    })
    current_node.currentImg = 'false';
    next_node.currentImg = 'true';   
} 

function carouselNavbarUpdate(target_old, target_new) {
    /** Updates the Navbar Style of the Carousel
     * 
     * @param target_old {DOM obj} Old Navbar obj with currently the Active State
     * @param target_new {DOM obj} New Navbar Obj where the Active State must be set
     */

    let navItemActive = "carousel__navigator-item--active";   
    target_old.classList.remove(navItemActive);
    target_new.classList.add(navItemActive);
}

function carouselGetCurrentSlide() { 

    let slideSelector = document.querySelectorAll(".carousel__slide");
    let slides = Array.from(slideSelector);

    // Get the Current Slide
    let slide = {
        allSlides: [],
        currentSlide: null,
        nextSlide: null,
        prevSlide: null,
        slideWidth: undefined,
        slideIndex: null,
        isHead: false,
        isTail: false
    }
    for (img of slides) {
        let dataset = img.dataset;      
        if (dataset.currentImg == "true") {
            slide.currentSlide = img;
            slide.nextSlide = img.nextElementSibling;
            slide.prevSlide = img.previousElementSibling;
            slide.slideWidth = img.getBoundingClientRect().width;
            slide.slideIndex = parseInt(dataset.indexNumber);          
            slide.isHead = dataset.carouselHead == 'true' ? true : false;
            slide.isTail = dataset.carouselTail == 'true' ? true : false;
            break;
        }
    } 
    slide.allSlides.push.apply(slide.allSlides, slides);
    return slide;
}

function getDistance(where, distanceData, next_node) {

    let [width, index, direction] = distanceData;
    if (where == 'prev') {
        direction.distance = width * (index - 1); 
    } else if (where == 'next') {
        direction.distance = width * (index + 1); 
    } else { // Means a NavBar Movement
        direction.distance = width * (index); 
    }
    direction.next_node = next_node;
    
}

const carouselEventButtonPress = (event) => {

    let target = event.target;
    let next = false;
    let prev = false;
    if (target.classList.contains('next')) next = true;
    else if (target.classList.contains('prev')) prev = true;
    else return; // Make sure that if incorrect HTML / CSS Settings we won't go any further

    slide = carouselGetCurrentSlide();
    // Check if we are at the first (Head) or Last (tail) of the Carousel Images
    if (next && slide.isTail) return;
    else if (prev && slide.isHead) return;

    let direction = {
        distance: undefined,
        current_node: slide.currentSlide.dataset,
        next_node: undefined
    }
    // Change The Active State of NavBar-Item
    let navTarget;
    let navbarItems = document.querySelectorAll('.carousel__navigator-item');
    let target_old = document.querySelector('.carousel__navigator-item--active');
    let indexSign = prev ? -1 : 1  // Check which Direction we are moving, back or Forth
    for (item of navbarItems) {
        if (item.dataset.indexNumber == (slide.slideIndex + indexSign)) navTarget = item;
    }
    carouselNavbarUpdate(target_old, navTarget);    

    let distanceData = [slide.slideWidth, slide.slideIndex, direction]; 
    if (prev) getDistance('prev', distanceData, slide.prevSlide.dataset);
    else if (next) getDistance('next', distanceData, slide.nextSlide.dataset);;    
    carouselMove(slide, direction);    
}

const carouselEventNavBarPress = (event) => {

    let navTarget = event.target.closest('.carousel__navigator-item');
    if (!navTarget) return; // Makes Sure we actually Hit the NavBar-Item
    slide = carouselGetCurrentSlide();
    let direction = {
        distance: undefined,
        current_node: slide.currentSlide.dataset,
        next_node: undefined
    }

    let target_old = event.target.parentElement.querySelector('.carousel__navigator-item--active');
    carouselNavbarUpdate(target_old, navTarget);    
    
    let targetIndex = parseInt(navTarget.dataset.indexNumber);
    let slideIndex = slide.slideIndex;
    let distanceData = [slide.slideWidth, targetIndex, direction]; 
    if (slideIndex == targetIndex) return;
    else if (targetIndex < slideIndex) getDistance(null, distanceData, slide.prevSlide.dataset);
    else if (targetIndex > slideIndex) getDistance(null, distanceData, slide.nextSlide.dataset);
    carouselMove(slide, direction)
}

let CarouselTwo = {

    carouselPrepare: function(carousel, imagesArray, navbarArray) {
        this.initImgDataset(imagesArray);   
        this.initNavbarDataset(navbarArray);    
        this.initEvent(carousel);
    },

    initImgDataset: function(imagesArray) {

        imagesArray.forEach( (el, index) =>  {
            el.dataset.indexNumber = index;
            if (index == 0) {
                el.dataset.currentImg = true;
                el.dataset.carouselHead = true;
            }
            else el.dataset.currentImg = false;
        })
        imagesArray[imagesArray.length -1].dataset.carouselTail = true;
    },

    initNavbarDataset: function(navbarArray) {
        navbarArray.forEach( (el, index) => {
            el.dataset.indexNumber = index;
        })
    },

    initEvent: function(carousel){               

        // ----------- Carousel Buttons Prev / Next
        let carouselButtons = {
            buttonPrev: undefined,
            buttonNext: undefined,
            attachEvent: function(eventType, callback) {
                this.buttonPrev.addEventListener(eventType, callback);
                this.buttonNext.addEventListener(eventType, callback);
            }
        }
        const CAROUSELBTNS = carousel.querySelectorAll('.carousel_button');
        CAROUSELBTNS.forEach((btn) => {
            if (btn.classList.contains('carousel_button--left')) carouselButtons.buttonPrev = btn;
            else if (btn.classList.contains('carousel_button--right')) carouselButtons.buttonNext = btn;
        })
        carouselButtons.attachEvent.apply(carouselButtons, ['click', carouselEventButtonPress]);

        // ----------- Carousel NavBar
        const CAROUSELNAVBAR = carousel.querySelector('.carousel__nav');
        CAROUSELNAVBAR.addEventListener('click', carouselEventNavBarPress);
    },
    
}

window.addEventListener('load', () => {

    const CAROUSELTWO = document.querySelector('#carouselTwo');
    if (CAROUSELTWO == undefined) return;
    
    const slideSelector = CAROUSELTWO.querySelectorAll(".carousel__slide");
    let slides = Array.from(slideSelector);  

    const navbarSelector = CAROUSELTWO.querySelectorAll('.carousel__navigator .carousel__navigator-item');
    let navbarItems = Array.from(navbarSelector);

    if (CAROUSELTWO && slides && navbarItems) CarouselTwo.carouselPrepare(CAROUSELTWO, slides, navbarItems);
})


// ============================== < carouselGliderJSOne > ====================================== \\ 

if (typeof Glider !== 'undefined') {

    // ---- First Instance
    new Glider(document.querySelector('#gliderJSOne'), {
        slidesToShow: 5,
        slidesToScroll: 5,
        draggable: true,
        dots: '#gliderJSOneDots',
        arrows: {
            prev: '#gliderOnePrev',
            next: '#gliderOneNext'
        }
    });

    // ---- Second Instance
    new Glider(document.querySelector('#gliderJSTwo'), {
        slidesToShow: 1,
        dots: '#gliderJSTwoDots',
        draggable: true,
        arrows: {
            prev: '#gliderTwoPrev',
            next: '#gliderTwoNext'
        }
    });

    // ---- Third Instance
    const GLIDERTHREE = "gliderJSThree";
    const DOTSTHREE = "gliderJSThreeDots";
    const PREVTHREE = "gliderThrePrev";
    const NEXTTHREE = "gliderThreeNext";

    /* NOTE: 
        Technically we won't need to set up an additional Variable for the Glider instance
        Once the new Glider is Created, the DOM Element used as Glider argument will have attached
        to its property the actual instance. Access it via element._glider
    */ 
    let gliderThree = new Glider(document.querySelector(`#${GLIDERTHREE}`), {  
        slidesToShow: 5,
        slidesToScroll: 1,
        draggable: true,
        dots: `#${DOTSTHREE}`,
        arrows: {
            prev: `#${PREVTHREE}`,
            next: `#${NEXTTHREE}`
        }
    });

    const CUSTOMSLIDES = "slides__custom--three";
    let slides$3 = gliderThree.slides;
    (function gliderThreeCustomStyle(slides){
        for (let slide of slides) {
            slide.classList.add(CUSTOMSLIDES);
        }
    })(slides$3);

    let slider$3 = gliderThree.ele; // The Actual Glider
    slider$3.classList.add("glider-persp");

}



// ============================== < INPUT HANDLER EMITTER > ====================================== \\ 

const emitterBox = document.querySelector('#emitterOne');
const emitterInput = emitterBox.querySelector('.emitter__input');
const whiteborard = emitterBox.querySelector('#whiteBoardOne');

function emitter(event) {
    whiteborard.value = event.target.value;    
}

function initEmitterOne() {
    emitterInput.addEventListener('input', emitter);
}

if (emitterBox !== undefined && emitterInput !== undefined  && whiteborard !== undefined) initEmitterOne();
