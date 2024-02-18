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




