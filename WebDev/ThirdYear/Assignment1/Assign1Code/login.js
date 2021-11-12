// Get html elements
const loginForm = document.getElementById("form");
const loginButton = document.getElementById("login_btn");
const loginErrorMsg = document.getElementById("error_message");

// Add an event listener
loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    // Pass the user input value to a variable
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    // Conditional check to see if username matches
    if (username === "corey" && password === "qwerty") {
      //If username matches, relocate to the game page
        window.location.replace("game.html");
    }
    // Otherwise, throw an error
    else {
        loginErrorMsg.style.opacity = 1;
    }
})
