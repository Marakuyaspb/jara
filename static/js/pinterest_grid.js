window.onload = function() {
    var elem = document.querySelector('.el_grid_container');
    var msnry = new Masonry(elem, {
        itemSelector: '.el_grid',
        columnWidth: '.el_grid', 
        percentPosition: true,
        gutter: 20 
    });
};