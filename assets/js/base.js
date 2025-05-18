// Test

console.log("Base.Js loaded");

// ------------------------------ Topbar Date ---------------------------------


// Topbar time and Date
function formatDateTime() {
    const now = new Date();

    const days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
    const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

    const day = now.getDate();
    const month = months[now.getMonth()];
    const year = now.getFullYear();
    const weekday = days[now.getDay()];

    let hours = now.getHours();
    const minutes = now.getMinutes().toString().padStart(2, "0");
    const seconds = now.getSeconds().toString().padStart(2, "0");
    const ampm = hours >= 12 ? "PM" : "AM";
    hours = hours % 12 || 12; // Convert to 12-hour format

    const datePart = `${day}-${month}-${year}`;
    const timePart = `${hours}:${minutes}:${seconds} ${ampm}`;

    // Update the content of the spans
    document.getElementById("datePart").innerText = datePart;
    document.getElementById("weekdayPart").innerText = weekday;
    document.getElementById("timePart").innerText = timePart;
}

// Immediately set the date and time on page load
formatDateTime();

// Update the time every second
setInterval(formatDateTime, 1000);

// --------------------------- Add task bTn ( Base Js Code ) ------------------------------

function sidebarAddTaskBtn() {
    console.log("Clicked On Add Task Btn");
    window.location.href = "/home?showForm=true"; // Redirect to /home with query parameter
}

window.addEventListener("DOMContentLoaded", () => {
    const urlParams = new URLSearchParams(window.location.search);
    const showForm = urlParams.get("showForm"); // Get query parameter

    if (showForm === "true") {
        const taskForm = document.querySelector("#taskForm");
        const addTaskBtn = document.querySelector(".addTaskBtn");

        // Show the form and hide the button
        taskForm.style.display = "block";
        addTaskBtn.style.display = "none";
    }
});


// To Sync The Task - It Will reload On the Visible and Reload after the 10 Min completed

// Reload the page when the tab becomes visible
document.addEventListener("visibilitychange", function () {
    if (document.visibilityState === "visible") {
        location.reload(); 
    }
});

// Automatically reload the page every 10 minutes
setInterval(function () {
    location.reload();
}, 600000); //10 Min


// Save Scroll Postion

// Save the current scroll position before form submission
document.querySelectorAll('select[name="status"]').forEach(select => {
    select.addEventListener('change', function () {
        localStorage.setItem('scrollPos', window.scrollY);
        this.form.submit();
        console.log(scrollPos);
    });
});

// Restore scroll position after page reload
window.addEventListener('load', () => {
    const scrollPos = localStorage.getItem('scrollPos');
    if (scrollPos) {
        window.scrollTo(0, parseInt(scrollPos));
        localStorage.removeItem('scrollPos'); // Clear after restoring
        console.log(scrollPos);
        
    }
});

