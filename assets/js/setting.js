const nameInput = document.getElementById("nameInput");
const saveNameButton = document.getElementById("saveName");
const cancelButton = document.getElementById("cancel");

// Handle click on Edit/Update button
saveNameButton.addEventListener("click", function () {
    if (nameInput.hasAttribute("readonly")) {
        // Enable editing
        nameInput.removeAttribute("readonly");
        nameInput.focus();
        saveNameButton.querySelector("p").textContent = "Update"; // Change button text
        saveNameButton.setAttribute("type", "button"); // Set type to button
        cancelButton.classList.remove("hidden"); // Show cancel button
    } else {
        // Save changes
        nameInput.setAttribute("readonly", true);
        saveNameButton.querySelector("p").textContent = "Edit"; // Revert button text
        saveNameButton.setAttribute("type", "submit"); // Change type to submit
        cancelButton.classList.add("hidden"); // Hide cancel button
    }
});

// Handle click on Cancel button
cancelButton.addEventListener("click", function () {
    nameInput.setAttribute("readonly", true);
    saveNameButton.querySelector("p").textContent = "Edit"; // Revert button text
    saveNameButton.setAttribute("type", "button"); // Reset type to button
    cancelButton.classList.add("hidden"); // Hide cancel button
});


// For Email Tab

const emailInput = document.getElementById("emailInput");
const saveEmailButton = document.getElementById("saveEmail");
const emailCancelButton = document.getElementById("emailCancel");

// Handle click on Edit/Update button
saveEmailButton.addEventListener("click", function () {
    if (emailInput.hasAttribute("readonly")) {
        // Enable editing
        emailInput.removeAttribute("readonly");
        emailInput.focus();
        saveEmailButton.querySelector("p").textContent = "Update"; // Change button text
        saveEmailButton.setAttribute("type", "button"); // Set type to button while editing
        emailCancelButton.classList.remove("hidden"); // Show cancel button
    } else {
        // Save changes
        emailInput.setAttribute("readonly", true);
        saveEmailButton.querySelector("p").textContent = "Edit"; // Revert button text
        saveEmailButton.setAttribute("type", "submit"); // Change type to submit
        emailCancelButton.classList.add("hidden"); // Hide cancel button
    }
});

// Handle click on Cancel button
emailCancelButton.addEventListener("click", function () {
    emailInput.setAttribute("readonly", true); // Make input readonly
    saveEmailButton.querySelector("p").textContent = "Edit"; // Revert button text
    saveEmailButton.setAttribute("type", "button"); // Reset type to button
    emailCancelButton.classList.add("hidden"); // Hide cancel button
});

