
// Materialize initialization
document.addEventListener("DOMContentLoaded", function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);

    // dropdown initialization
    let elems = document.querySelectorAll('.dropdown-trigger');
    let options = {inDuration: 300, outDuration: 225, coverTrigger: false}; M.Dropdown.init(elems, options);
    
    // select initialization
    let category_input = document.querySelectorAll('select');
    M.FormSelect.init(category_input);

    //modal initialization for deleteting recipe/category
    let confirm_delete = document.querySelectorAll('.modal');
    M.Modal.init(confirm_delete);
 

});

// Code from stackoverflow and adapted for this project
// Function to validate image urls
function validateAndSetImageUrls() {
    let images = document.querySelectorAll('.card-image img');
    let defaultImageUrl = '../images/logo.png';
  
    images.forEach(function(img) {
        // Create a new Image object for validation
        let testImage = new Image();
        testImage.onload = function() {
            // If this fires, the URL is valid and the image is loaded
            img.src = testImage.src;
        };
        testImage.onerror = function() {
            // If this fires, the URL is invalid or the image cannot be loaded
            img.src = defaultImageUrl;
        };
        // Set the src to test loading the image
        testImage.src = img.src;
    });
  }
  window.onload = validateAndSetImageUrls();
  