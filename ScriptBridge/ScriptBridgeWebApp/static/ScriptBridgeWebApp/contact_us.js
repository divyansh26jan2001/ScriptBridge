// JavaScript to handle form submission and validation
document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Retrieve form data
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();

    // Perform form validation
    if (!validateName(name)) {
        alert('Please enter a valid name with at least two characters.');
        return;
    }

    if (!validateEmail(email)) {
        alert('Please enter a valid email address.');
        return;
    }

    if (!validateMessage(message)) {
        alert('Please enter a message with at least 10 characters.');
        return;
    }

    // If validation is successful, simulate form submission (replace this with actual form handling code)
    alert('Thank you, ' + name + '! Your message has been sent.');

    // Clear the form
    document.getElementById('contact-form').reset();
});

// Validation functions
function validateName(name) {
    return name.length >= 2; // Name should be at least two characters long
}

function validateEmail(email) {
    // Regular expression for email validation
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
}

function validateMessage(message) {
    return message.length >= 10; // Message should be at least 10 characters long
}