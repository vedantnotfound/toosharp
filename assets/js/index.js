// Test
console.log("JS Loaded");
// ---------------------------------------------- Filter Member ( Member Page Js ) -------------------------------
// Filter Employees Based on Search Input
function filterEmployees() {
    const searchInput = document.getElementById('searchEmployee').value.toLowerCase(); // Get search input and convert to lowercase
    const employeeItems = document.querySelectorAll('.employee-item'); // Select all employee items

    employeeItems.forEach((employee) => {
        // Get data attributes for filtering
        const name = employee.getAttribute('data-name');
        const department = employee.getAttribute('data-department');
        const position = employee.getAttribute('data-position');

        // Check if search input matches any of the data attributes
        if (
            name.includes(searchInput) || 
            department.includes(searchInput) || 
            position.includes(searchInput)
        ) {
            employee.style.display = 'flex'; // Show matching employee
        } else {
            employee.style.display = 'none'; // Hide non-matching employee
        }
    });
}

// Add Event Listener for Search Input
document.getElementById('searchEmployee').addEventListener('keyup', filterEmployees);

// Base

//  -------------------------------- Add Task Btn ( Today Page Js ) -------------------------------

let addTaskBtn = document.querySelector(".addTaskBtn");
let taskForm = document.querySelector("#taskForm");

addTaskBtn.addEventListener("click", function () {
    // Show the form when the button is clicked
    taskForm.style.display = "block";
    addTaskBtn.style.display = "none";
});

let closeTaskForm = document.getElementById("closeTaskForm");
closeTaskForm.addEventListener("click", function () {
    // Show the form when the button is clicked
    taskForm.style.display = "none";
    addTaskBtn.style.display = "flex";
});

// --------------------------- Add task bTn ( Base Js Code ) ------------------------------

function sidebarAddTaskBtn() {
    console.log("Clicked On Add Task Btn");
    window.location.href = "/?showForm=true"; // Redirect with query parameter
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

// ------------------------------------ Greeting ( Today Page ) ---------------------------------
function updateGreeting() {
    const greetingElement = document.getElementById("greeting");
    const currentTime = new Date();
    const hours = currentTime.getHours();
    
    // Determine the time of day and update the greeting accordingly
    if (hours < 12) {
        greetingElement.textContent = "Morning";
    } else if (hours < 18) {
        greetingElement.textContent = "Afternoon";
    } else {
        greetingElement.textContent = "Evening";
    }
}


// Call the function to update the greeting when the page loads
updateGreeting();


// ---------------------------------- Search ( Today , Upcoming & History Page Js) --------------------------------------
function filterTasks() {
    const searchInput = document.getElementById("searchInput").value.toLowerCase(); // Get search input
    const tasks = document.querySelectorAll(".task-item"); // Get all tasks

    tasks.forEach((task) => {
        // Retrieve all searchable data from custom attributes
        const date = task.getAttribute("data-date");
        const title = task.getAttribute("data-title");
        const desc = task.getAttribute("data-desc");
        const employee = task.getAttribute("data-employee");
        const priority = task.getAttribute("data-priority");
        const status = task.getAttribute("data-status");

        // Check if any data matches the search input
        if (
            date.includes(searchInput) ||
            title.includes(searchInput) ||
            desc.includes(searchInput) ||
            employee.includes(searchInput) ||
            priority.includes(searchInput) ||
            status.includes(searchInput)
        ) {
            task.style.display = "flex"; // Show matching task
        } else {
            task.style.display = "none"; // Hide non-matching task
        }
    });
}



// -------------------- Text areat Auto rezie after the paste - ( Today Page ) --------------------
document.addEventListener("DOMContentLoaded", function () {

    const textarea = document.getElementById("description");


    function autoResize() {
        textarea.style.height = "0px";
        textarea.style.height = textarea.scrollHeight + "px";
    }


    textarea.addEventListener("input", autoResize);
    textarea.addEventListener("paste", autoResize);


    window.addEventListener("load", autoResize);
})


// ----------------- Date Picker Active ( Today Page JS) ---------------
// Get current date and month
// document.addEventListener("DOMContentLoaded", function () {
//     let today = new Date();
//     let selectedDate = today; // Store the currently selected date
//     let currentDate = today.getDate();
//     let currentMonth = today.getMonth();
//     let currentYear = today.getFullYear();
//     let selectedDayCell = null; // Keep track of selected date cell

//     // Function to format the date (DD-MMM-YYYY)
//     function formatDate(date) {
//         const options = { year: 'numeric', month: 'short', day: 'numeric' };
//         return date.toLocaleDateString('en-GB', options);
//     }

//     // Show/Hide Date Picker on Button Click (Toggle)
//     document.getElementById("date-button").addEventListener("click", function () {
//         const datePicker = document.getElementById("date-picker");
//         datePicker.classList.toggle("hidden"); // Toggle visibility of the picker
//         populateCalendar(currentMonth, currentYear); // Populate the current month calendar
//     });

//     // Populate the Calendar for a given month and year
//     function populateCalendar(month, year) {
//         const firstDayOfMonth = new Date(year, month, 1);
//         const lastDayOfMonth = new Date(year, month + 1, 0);
//         const daysInMonth = lastDayOfMonth.getDate();
//         const startingDay = firstDayOfMonth.getDay();
//         const calendar = document.getElementById("calendar");

//         // Set the current month in the header
//         const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
//         document.getElementById("current-month").textContent = `${monthNames[month]} ${year}`;

//         // Clear existing days
//         calendar.innerHTML = '';

//         // Fill in the empty cells before the first day of the month
//         for (let i = 0; i < startingDay; i++) {
//             const emptyCell = document.createElement('div');
//             calendar.appendChild(emptyCell);
//         }

//         // Fill the calendar with actual days
//         for (let day = 1; day <= daysInMonth; day++) {
//             const dayCell = document.createElement('p');
//             dayCell.classList.add("text-center", "w-[30px]", "h-[30px]", "text-[14px]", "cursor-pointer", "hover:bg-gray-200", "rounded-lg", "flex", "items-center", "justify-center");

//             const currentDateObj = new Date(year, month, day);

//             // Disable past dates before "Yesterday" but keep today clickable
//             // Disable past dates before "Yesterday" but keep today clickable
//             if (isBeforeToday(currentDateObj, today)) {
//                 dayCell.classList.add("text-gray-400");
//                 dayCell.style.pointerEvents = "none"; // Disable clicking for past dates
//             } else {
//                 // Keep today and future dates clickable
//                 dayCell.classList.add("text-black");
//             }

//             // Helper function to compare only date (ignoring time)
//             function isBeforeToday(date1, date2) {
//                 // Compare the year, month, and day only
//                 return date1.getFullYear() < date2.getFullYear() ||
//                     (date1.getFullYear() === date2.getFullYear() && date1.getMonth() < date2.getMonth()) ||
//                     (date1.getFullYear() === date2.getFullYear() && date1.getMonth() === date2.getMonth() && date1.getDate() < date2.getDate());
//             }


//             // // Highlight today's date with a circle
//             // if (currentDateObj.toDateString() === today.toDateString()) {
//             //   dayCell.classList.add("bg-blue-100", "rounded-full"); // Circle around today's date
//             // }

//             dayCell.textContent = day;

//             // Click event to select a date
//             dayCell.addEventListener("click", function () {
//                 selectedDate = currentDateObj;
//                 document.getElementById("date-button").textContent = formatDate(currentDateObj); // Update button text with selected date
//                 console.log("Selected date:", selectedDate); // Console log the selected date

//                 // Highlight the selected date cell
//                 if (selectedDayCell) {
//                     selectedDayCell.classList.remove('bg-blue-100'); // Remove highlight from previously selected date
//                 }
//                 dayCell.classList.add('bg-blue-100'); // Add background to the selected date cell
//                 selectedDayCell = dayCell; // Store the currently selected cell

//                 // Check if selected date matches Today or Tomorrow
//                 if (isSameDay(selectedDate, today)) {
//                     document.getElementById("date-button").textContent = "Today"; // Update label to "Today"
//                 } else if (isSameDay(selectedDate, getTomorrow(today))) {
//                     document.getElementById("date-button").textContent = "Tomorrow"; // Update label to "Tomorrow"
//                 }

//                 document.getElementById("date-picker").classList.add("hidden"); // Close the picker
//             });

//             calendar.appendChild(dayCell);
//         }
//     }

//     // Handle Previous and Next Month Buttons
//     document.getElementById("prev-month").addEventListener("click", function () {
//         if (currentMonth === 0) {
//             currentMonth = 11;
//             currentYear--;
//         } else {
//             currentMonth--;
//         }
//         populateCalendar(currentMonth, currentYear); // Re-populate calendar with previous month
//     });

//     document.getElementById("next-month").addEventListener("click", function () {
//         if (currentMonth === 11) {
//             currentMonth = 0;
//             currentYear++;
//         } else {
//             currentMonth++;
//         }
//         populateCalendar(currentMonth, currentYear); // Re-populate calendar with next month
//     });

//     // Handle Today Button
//     document.getElementById("today-button").addEventListener("click", function () {
//         selectedDate = today; // Set today's date
//         document.getElementById("date-button").textContent = "Today"; // Update button text to "Today"
//         console.log("Selected date:", selectedDate); // Console log the selected date
//         populateCalendar(currentMonth, currentYear); // Re-populate calendar
//         document.getElementById("date-picker").classList.add("hidden"); // Close the picker
//     });

//     // Handle Tomorrow Button
//     document.getElementById("tomorrow-button").addEventListener("click", function () {
//         const tomorrow = getTomorrow(today);
//         selectedDate = tomorrow;
//         document.getElementById("date-button").textContent = "Tomorrow"; // Update button text to "Tomorrow"
//         console.log("Selected date:", selectedDate); // Console log the selected date
//         populateCalendar(currentMonth, currentYear); // Re-populate calendar
//         document.getElementById("date-picker").classList.add("hidden"); // Close the picker
//     });

//     // Handle Next Week Button
//     document.getElementById("next-week-button").addEventListener("click", function () {
//         const nextWeek = getNextWeek(today);
//         selectedDate = nextWeek;
//         document.getElementById("date-button").textContent = formatDate(nextWeek); // Set next week's date in label
//         console.log("Selected date:", selectedDate); // Console log the selected date
//         populateCalendar(currentMonth, currentYear); // Re-populate calendar
//         document.getElementById("date-picker").classList.add("hidden"); // Close the picker
//     });

//     // Helper function to check if two dates are the same day
//     function isSameDay(d1, d2) {
//         return d1.toDateString() === d2.toDateString();
//     }

//     // Helper function to get Tomorrow's date
//     function getTomorrow(date) {
//         const tomorrow = new Date(date);
//         tomorrow.setDate(date.getDate() + 1);
//         return tomorrow;
//     }

//     // Helper function to get Next Week's date
//     function getNextWeek(date) {
//         const nextWeek = new Date(date);
//         nextWeek.setDate(date.getDate() + 7);
//         return nextWeek;
//     }

//     // Initialize with the current month
//     populateCalendar(currentMonth, currentYear);

// });

document.addEventListener("DOMContentLoaded", function () {
    let today = new Date();
    let tomorrow = new Date(today);
    tomorrow.setDate(today.getDate() + 1); // Set tomorrow's date
    let nextWeek = new Date(today);
    nextWeek.setDate(today.getDate() + 7); // Set next week's date

    let currentDate = today;
    let currentMonth = today.getMonth();
    let currentYear = today.getFullYear();

    let selectedDate = today; // Store the currently selected date
    let selectedDayCell = null; // To store the currently selected day cell

    // Function to format the date (DD-MMM-YYYY)
    function formatDate(date) {
        const options = { year: 'numeric', month: 'short', day: 'numeric' };
        return date.toLocaleDateString('en-GB', options);
    }

    // Show/Hide Date Picker on Button Click (Toggle)
    document.getElementById("date-button").addEventListener("click", function (event) {
        const datePicker = document.getElementById("date-picker");
        datePicker.classList.toggle("hidden"); // Toggle visibility of the picker
        populateCalendar(currentMonth, currentYear); // Populate the current month calendar
        event.stopPropagation(); // Prevent click event from propagating to the document
    });

    // Function to update the button text by changing <p> content
    function updateButtonText(newText) {
        const dateLabel = document.getElementById("date-label"); // Target the <p> tag
        dateLabel.textContent = newText; // Change the text of <p> tag
        console.log("Updated Button Text:", newText); // Log the button text
    }

    // Function to compare two dates (ignoring time)
    function compareDates(date1, date2) {
        return date1.getFullYear() === date2.getFullYear() &&
            date1.getMonth() === date2.getMonth() &&
            date1.getDate() === date2.getDate();
    }

    // Populate the Calendar for a given month and year
    function populateCalendar(month, year) {
        const firstDayOfMonth = new Date(year, month, 1);
        const lastDayOfMonth = new Date(year, month + 1, 0);
        const daysInMonth = lastDayOfMonth.getDate();
        const startingDay = firstDayOfMonth.getDay();
        const calendar = document.getElementById("calendar");

        // Set the current month in the header
        const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
        document.getElementById("current-month").textContent = `${monthNames[month]} ${year}`;

        // Clear existing days
        calendar.innerHTML = '';

        // Fill in the empty cells before the first day of the month
        for (let i = 0; i < startingDay; i++) {
            const emptyCell = document.createElement('div');
            calendar.appendChild(emptyCell);
        }

        // Fill the calendar with actual days
        for (let day = 1; day <= daysInMonth; day++) {
            const dayCell = document.createElement('p');
            dayCell.classList.add("text-center", "w-[30px]", "h-[30px]", "text-[14px]", "cursor-pointer", "hover:bg-gray-200", "rounded-lg", "flex", "items-center", "justify-center");

            const currentDateObj = new Date(year, month, day);

            // Disable past dates before "Yesterday" but keep today clickable
            if (isBeforeToday(currentDateObj, today)) {
                dayCell.classList.add("text-gray-400");
                dayCell.style.pointerEvents = "none"; // Disable clicking for past dates
            } else {
                dayCell.classList.add("text-black"); // Keep today and future dates clickable
            }

            // Helper function to compare only date (ignoring time)
            function isBeforeToday(date1, date2) {
                return date1.getFullYear() < date2.getFullYear() ||
                    (date1.getFullYear() === date2.getFullYear() && date1.getMonth() < date2.getMonth()) ||
                    (date1.getFullYear() === date2.getFullYear() && date1.getMonth() === date2.getMonth() && date1.getDate() < date2.getDate());
            }

            dayCell.textContent = day;

            // Click event to select a date
            dayCell.addEventListener("click", function () {
                selectedDate = currentDateObj;

                // Check if selected date is today, tomorrow or any other date
                if (compareDates(selectedDate, today)) {
                    updateButtonText("Today"); // If it's today's date, show "Today"
                    console.log("Selected date:", selectedDate); // Log selected date
                    // Ensure correct local date in "YYYY-MM-DD" format
                    let storeDateInput = document.getElementById("storeDate");
                    let localDate = new Date(selectedDate.getTime() - selectedDate.getTimezoneOffset() * 60000) // Adjust for timezone offset
                        .toISOString()
                        .split('T')[0]; // Extract only the date part 
                    storeDateInput.value = localDate; // Set the value
                    console.log("Stored date in hidden input:", storeDateInput.value); // Log stored date
                } else if (compareDates(selectedDate, tomorrow)) {
                    updateButtonText("Tomorrow"); // If it's tomorrow's date, show "Tomorrow"
                    console.log("Selected date:", selectedDate); // Log selected date
                    // Ensure correct local date in "YYYY-MM-DD" format
                    let storeDateInput = document.getElementById("storeDate");
                    let localDate = new Date(selectedDate.getTime() - selectedDate.getTimezoneOffset() * 60000) // Adjust for timezone offset
                        .toISOString()
                        .split('T')[0]; // Extract only the date part 
                    storeDateInput.value = localDate; // Set the value
                    console.log("Stored date in hidden input:", storeDateInput.value); // Log stored date
                } else {
                    updateButtonText(formatDate(selectedDate)); // Otherwise, show the formatted date
                    console.log("Selected date:", selectedDate); // Log selected date
                    // Ensure correct local date in "YYYY-MM-DD" format
                    let storeDateInput = document.getElementById("storeDate");
                    let localDate = new Date(selectedDate.getTime() - selectedDate.getTimezoneOffset() * 60000) // Adjust for timezone offset
                        .toISOString()
                        .split('T')[0]; // Extract only the date part 
                    storeDateInput.value = localDate; // Set the value
                    console.log("Stored date in hidden input:", storeDateInput.value); // Log stored date
                }

                // Highlight the selected date cell
                if (selectedDayCell) {
                    selectedDayCell.classList.remove('bg-blue-100');
                }
                dayCell.classList.add('bg-blue-100'); // Add background to the selected date cell
                selectedDayCell = dayCell;

                document.getElementById("date-picker").classList.add("hidden"); // Close the picker
            });

            calendar.appendChild(dayCell);
        }
    }

    // Handle Previous and Next Month Buttons
    document.getElementById("prev-month").addEventListener("click", function () {
        if (currentMonth === 0) {
            currentMonth = 11;
            currentYear--;
        } else {
            currentMonth--;
        }
        populateCalendar(currentMonth, currentYear);
    });

    document.getElementById("next-month").addEventListener("click", function () {
        if (currentMonth === 11) {
            currentMonth = 0;
            currentYear++;
        } else {
            currentMonth++;
        }
        populateCalendar(currentMonth, currentYear);
    });

    // Handle Tomorrow Button
    document.getElementById("tomorrow-button").addEventListener("click", function () {
        selectedDate = tomorrow; // Set selected date to tomorrow
        updateButtonText("Tomorrow"); // Update button text to "Tomorrow"
        console.log("Selected date:", selectedDate); // Log selected date
        // Ensure correct local date in "YYYY-MM-DD" format
        let storeDateInput = document.getElementById("storeDate");
        let localDate = new Date(selectedDate.getTime() - selectedDate.getTimezoneOffset() * 60000) // Adjust for timezone offset
            .toISOString()
            .split('T')[0]; // Extract only the date part 
        storeDateInput.value = localDate; // Set the value
        console.log("Stored date in hidden input:", storeDateInput.value); // Log stored date
        populateCalendar(currentMonth, currentYear);
        document.getElementById("date-picker").classList.add("hidden");
    });

    // Handle Next Week Button
    document.getElementById("next-week-button").addEventListener("click", function () {
        selectedDate = nextWeek; // Set selected date to next week
        updateButtonText(formatDate(nextWeek)); // Update button text to the exact date of next week
        console.log("Selected date:", selectedDate); // Log selected date
        // Ensure correct local date in "YYYY-MM-DD" format
        let storeDateInput = document.getElementById("storeDate");
        let localDate = new Date(selectedDate.getTime() - selectedDate.getTimezoneOffset() * 60000) // Adjust for timezone offset
            .toISOString()
            .split('T')[0]; // Extract only the date part 
        storeDateInput.value = localDate; // Set the value
        console.log("Stored date in hidden input:", storeDateInput.value); // Log stored date
        populateCalendar(currentMonth, currentYear);
        document.getElementById("date-picker").classList.add("hidden");
    });

    // Handle Today Button
    document.getElementById("today-button").addEventListener("click", function () {
        selectedDate = today; // Set selected date to today
        updateButtonText("Today"); // Update button text to "Today"
        console.log("Selected date:", selectedDate); // Log selected date

        // Ensure correct local date in "YYYY-MM-DD" format
        let storeDateInput = document.getElementById("storeDate");
        let localDate = new Date(selectedDate.getTime() - selectedDate.getTimezoneOffset() * 60000) // Adjust for timezone offset
            .toISOString()
            .split('T')[0]; // Extract only the date part 
        storeDateInput.value = localDate; // Set the value
        console.log("Stored date in hidden input:", storeDateInput.value); // Log stored date
        populateCalendar(currentMonth, currentYear);
        document.getElementById("date-picker").classList.add("hidden");
    });

    // Close the date picker if clicked outside of it
    document.addEventListener("click", function (event) {
        const datePicker = document.getElementById("date-picker");
        const dateButton = document.getElementById("date-button");

        // Close the date picker if the click is outside the date picker or button
        if (!datePicker.contains(event.target) && !dateButton.contains(event.target)) {
            datePicker.classList.add("hidden");
        }
    });

    // Initialize with the current month
    populateCalendar(currentMonth, currentYear);
});


// ----------------------------------- Add Task In Task Container --------------------------------
// document.addEventListener("DOMContentLoaded", function () {
//     const form = document.querySelector("#taskForm form");
//     const taskContainer = document.querySelector("#taskContainer"); // Reference to the existing task container

//     if (!taskContainer) {
//         console.error("Task container (#taskContainer) not found in the HTML.");
//         return;
//     }

//     form.addEventListener("submit", function (e) {
//         e.preventDefault(); // Prevent form from reloading the page

//         // Collecting form data
//         const title = form.querySelector('input[type="text"]').value.trim();
//         const description = form.querySelector("#description").value.trim();
//         const priority = form.querySelector('select[name="priority"] option:checked')?.textContent || "Medium";
//         const member = form.querySelector('select[name="member"] option:checked')?.textContent || "Unassigned";
//         const dateLabel = document.getElementById("date-label")?.textContent || "No Date";

//         // Validate required fields
//         if (!title || !description || !dateLabel) {
//             alert("Please fill in all required fields.");
//             return;
//         }

//         // Define priority styles
//         const priorityStyles = {
//             High: "border-red-600 bg-red-500 bg-opacity-40 text-red-700",
//             Medium: "border-blue-600 bg-blue-500 bg-opacity-40 text-blue-700",
//             Low: "border-green-600 bg-green-500 bg-opacity-40 text-green-700",
//         };
//         const priorityClass = priorityStyles[priority] || priorityStyles.Medium;

//         // Create the new task element
//         const newTask = document.createElement("div");
//         newTask.className = "flex items-center border-b";

//         newTask.innerHTML = `
//             <div class="px-[20px] border flex items-center min-w-[180px] h-[70px]">
//                 <p class="text-[14px]">${dateLabel}</p>
//             </div>
//             <div class="px-[20px] border flex items-start min-w-[500px] flex-col h-[70px] justify-center">
//                 <p class="text-[14px] font-medium">${title}</p>
//                 <p class="truncate text-[14px] w-full">${description}</p>
//             </div>
//             <div class="px-[20px] border flex items-center min-w-[150px] h-[70px]">
//                 <p class="text-[14px] px-[20px] flex items-center justify-center rounded-[5px] h-[35px]
//                     ${priorityClass}">${priority}</p>
//             </div>
//             <div class="px-[20px] border flex items-center min-w-[200px] h-[70px]">
//                 <p class="text-[14px]">${member}</p>
//             </div>
//             <div class="px-[20px] border flex items-center min-w-[150px] h-[70px]">
//                 <button type="button" class="w-full rounded-[6px] h-[35px] poppins text-green-700
//                     bg-green-700 border border-green-700 bg-opacity-40 text-[14px]">Completed</button>
//             </div>
//         `;

//         // Append the new task to the task container
//         taskContainer.appendChild(newTask);

//         // Reset the form after submission
//         form.reset();
//         document.getElementById("date-label").textContent = "Date";
//     });
// });






