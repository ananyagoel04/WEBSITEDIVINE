const button1 = document.getElementById("mainmenu");
const menu = document.getElementById("list");

button1.addEventListener("click", function () {
    const isChecked = document.getElementById("checkbox").checked;
    menu.style.display = isChecked ? "block" : "none";
});





//transition to rotate arrow on dropdown
const dropdownButton2 = document.getElementById('dropdownDefaultButton');
const arrowSvg = document.getElementById('arrow');

dropdownButton2.addEventListener('click', function (event) {
    event.stopPropagation();
    arrowSvg.classList.toggle('rotate');
    setTimeout(() => {
        arrowSvg.classList.remove('no-rotate');
    }, 300); // Adjust to match the transition duration
});

// Event listener on the document body to detect clicks outside the button
document.body.addEventListener('click', function (event) {
    if (event.target !== dropdownButton2) {
        arrowSvg.classList.remove('rotate');
        arrowSvg.classList.add('no-rotate');
        // Remove the 'no-rotate' class after the transition completes
        setTimeout(() => {
            arrowSvg.classList.remove('no-rotate');
        }, 300); // Adjust to match the transition duration
    }
});









///////script for dropdown menu button in mobile screens
// Get the button and dropdown content elements
const dropdownButton1 = document.getElementById('dropdownButton1');
const dropdownContent = document.getElementById('dropdownContent');
const element = document.getElementById('myElement');
let isClicked = true;

function toggleStyles() {
    if (!isClicked) {
        // Add styles when it's clicked
        element.style.top = '0';
        element.style.marginLeft = '50%';
        element.style.transform = 'translateX(-50%)';
        element.style.width = '0';
        element.style.transition = 'width 0.3s ease-in-out';
    } else {
        // Remove styles when clicked again
        element.style = '';
    }
    isClicked = !isClicked;
}
dropdownButton1.addEventListener('click', toggleStyles);

// Toggle the dropdown content on button click if elements are found
if (dropdownButton1 && dropdownContent) {
    dropdownButton1.addEventListener('click', function () {
        dropdownContent.classList.toggle('hidden');
    });

    document.addEventListener('click', function (event) {
        if (!dropdownButton1.contains(event.target) && !dropdownContent.contains(event.target)) {
            dropdownContent.classList.add('hidden');
        }
    });
} else {
    console.error("Dropdown button or content element not found!");
}




