function toggleDropdown() {
    document.getElementById("dropdown-content").classList.toggle("show");
}

// window.onclick = function(event) {
//     console.log("HALO");
//     if (!event.target.matches('.menu-icon')) {
//         var dropdowns = document.getElementsByClassName("dropdown-content");
//         var i;
//         for (i = 0; i < dropdowns.length; i++) {
//             var openDropdown = dropdowns[i];
//             if (openDropdown.classList.contains('show')) {
//                 openDropdown.classList.remove('show');
//             }
//         }
//     }
// }
 
// let dropdownWrap = document.getElementById("dropdownWrap");

// function toggleMenu() {
//     console.log("HALO");
//     console.log("Halo" + dropdownWrap);
//     dropdownWrap.classList.toggle("open-menu");
// } 

function toggleMenu() {
    let dropdownWrap = document.getElementById("dropdownWrap");
    console.log("HALO");
    console.log("Halo" + dropdownWrap);
    dropdownWrap.classList.toggle("open-menu");
}

document.addEventListener("DOMContentLoaded", function() {
    // Attach click event listener to the menu icon
    document.querySelector(".menu-icon").addEventListener("click", toggleMenu);
});