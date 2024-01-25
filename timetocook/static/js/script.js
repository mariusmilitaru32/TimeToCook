document.addEventListener("DOMContentLoaded", function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);

    let elems = document.querySelectorAll('.dropdown-trigger');
    let options = {inDuration: 300, outDuration: 225, coverTrigger: false}; M.Dropdown.init(elems, options);
    
    let category_input = document.querySelectorAll('select');
    M.FormSelect.init(category_input);

    //modal initialization for deleteting recipe/category
    let confirm_delete = document.querySelectorAll('.modal');
    M.Modal.init(confirm_delete);
 

});
