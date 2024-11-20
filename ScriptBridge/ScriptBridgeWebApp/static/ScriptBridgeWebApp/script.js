// JavaScript function to toggle the dropdown
function toggleDropdown(questionListId, subjectElement) {
    const questionList = document.getElementById(questionListId);
    const arrow = subjectElement.querySelector('.arrow'); // Select the arrow

    if (questionList.style.display === "none" || questionList.style.display === "") {
        questionList.style.display = "block"; // Show the questions
        arrow.style.transform = "rotate(90deg)"; // Rotate arrow
    } else {
        questionList.style.display = "none"; // Hide the questions
        arrow.style.transform = "rotate(0deg)"; // Reset arrow rotation
    }
}