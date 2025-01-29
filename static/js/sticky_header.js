window.onscroll = function() { stickyHeader() };

    const header = document.getElementById("tab_header");

    function stickyHeader() {
        if (window.pageYOffset > 0) {
            header.classList.add("sticky");
        } else {
            header.classList.remove("sticky");
        }
    }