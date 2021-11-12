//Declare variables for the detail title selector and the thumbnail anchor selector
const DETAIL_IMAGE_SELECTOR = '[data-image-role="target"]';
const DETAIL_TITLE_SELECTOR = '[data-image-role="title"]';
const THUMBNAIL_LINK_SELECTOR = '[data-image-role="trigger"]';

/* To change the detail image
 * @param imageUrl which image to use by supplying its URL
 * @param titleText what title to use for the corresponding image specified as imageUrl
 */
function setDetails(imageUrl, titleText) {
    'use strict'; //tells the browser that they conform to the most recent standard version of JavaScript

    //To get a reference to the element for the detail image
    let detailImage = document.querySelector(DETAIL_IMAGE_SELECTOR);
    //to change the detail image
    detailImage.setAttribute('src',imageUrl);

    //To get a reference to the element for the detail image title
    let detailTitle = document.querySelector(DETAIL_TITLE_SELECTOR);
    //to change the detail image title
    detailTitle.textContent = titleText;
}

//main function
function main() {
    let otterOneImage = 'img/otter1.jpg';
    let otterOneTitle = 'Stayin\' Alive';
    setDetails(otterOneImage, otterOneTitle);
}

main();




