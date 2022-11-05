import * as THREE from './node_modules/three/build/three.module.js';

import {
    recipe01,
    recipe02,
    recipe03,
    recipe04,
    recipe05,
    latheGeometry,
    tankMultiCamera,

} from "./recipes/recipes.js";

// import mapping
const RECIPES = {
    "tutorial/01.js": recipe01,
    "tutorial/02.js": recipe02,
    "tutorial/03.js": recipe03,
    "tutorial/04.js": recipe04,
    "tutorial/05.js": recipe05,


    // Shapes
    "shapes/latheGeometry.js": latheGeometry,

    // Demos
    "demos/tankMultiCamera.js": tankMultiCamera,
};

// DOM Elements
const body = document.body;
const navbar = document.querySelector(".navbar");
const content = document.querySelector(".content-wrapper");
const recipeLinks = document.querySelectorAll(".recipeLink");
const btnBack = document.getElementById("btnBack");

/// Register Events
btnBack.addEventListener("click", unloadScript);
recipeLinks.forEach(link => {
    link.addEventListener("click", loadScript);
});

function triggerLinkOnStart(linkIndex = null) {
    if (linkIndex === null)  return;
    recipeLinks[linkIndex].click();
}
triggerLinkOnStart(6);



/**
 * Remove ALL declare requestAnimationFrom from the current window
 * Used when unload a three.js script
 * @credit https://stackoverflow.com/a/55443952
 */
function cancelAllAnimationFrames(){
    var id = window.requestAnimationFrame(function(){});
    while(id--){
        window.cancelAnimationFrame(id);
    }
}

/**
 * Hides the main content and show the script helpers
 */
function hideContent() {
    body.classList.remove("margin");
    content.classList.add("hide");
    navbar.classList.remove("hide");
}

/**
 * shows the main content and Hides the script helpers
 */
function showContent() {
    body.classList.add("margin");
    content.classList.remove("hide");
    navbar.classList.add("hide");
}

/**
 * Loads a new recipe script
 * @param event
 */
function unloadScript(event) {
    document.title = "Home";
    showContent();

    // remove all timers
    cancelAllAnimationFrames();
    // destroy and canvas in DOC
    let canvas = document.querySelectorAll("canvas");
    canvas.forEach(c => c.remove());
    // destroy and clean up all dom elements required for the script
    let domElements = document.querySelectorAll(".clean-up-required");
    domElements.forEach(c => c.remove());

}

/**
 * UnLoads a new recipe script
 * @param event
 */
function loadScript(event) {
  let recipeLink = this.dataset.recipe;

  if (recipeLink in RECIPES) {
      document.title = recipeLink;
      hideContent();
      RECIPES[recipeLink](THREE);
  } else {
      alert(`Link ${recipeLink} not available!`);
  }

}








