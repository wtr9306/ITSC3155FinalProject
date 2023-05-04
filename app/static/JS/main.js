// Basic JavaScript for your app

document.addEventListener("DOMContentLoaded", function() {
    // Add click event listener to a button with the ID 'exampleButton'
    const exampleButton = document.getElementById("exampleButton");
    if (exampleButton) {
        exampleButton.addEventListener("click", function() {
            alert("Button clicked!");
        });
    }
});
