function flipflop(id) {
    element = document.getElementById(id);
    if(element) {
        element.style.display = element.style.display == "none" ? "" : "none";
    }
}