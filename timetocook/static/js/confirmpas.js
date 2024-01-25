let password = document.getElementById("password");
let confirm_password = document.getElementById("confirm_password");
let errorMessage = document.getElementById("error-message");

const confirmPassword = () => {
    if (password.value !== confirm_password.value) {
        // If passwords do not match, set a custom validity message
        confirm_password.setCustomValidity("Passwords do not match");
        errorMessage.textContent = "Passwords do not match"; // Set the error message
        errorMessage.style.display = "block"; // Show the error message
    } else {
        // If they do match, clear any custom validity message
        confirm_password.setCustomValidity("");
        errorMessage.style.display = "none"; // Hide the error message
    }
};

password.onchange = confirmPassword;
confirm_password.onkeyup = confirmPassword;

