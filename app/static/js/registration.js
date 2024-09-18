
const registrationForm = document.getElementById('registrationForm');
const usernameInput = document.getElementById('username');
const firstNameInput = document.getElementById('firstName');
const lastNameInput = document.getElementById('lastName');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const confirmPasswordInput = document.getElementById('confirmPassword');
const usernameError = document.getElementById('usernameError');
const firstNameError = document.getElementById('firstNameError');
const lastNameError = document.getElementById('lastNameError');
const emailError = document.getElementById('emailError');
const passwordError = document.getElementById('passwordError');
const confirmPasswordError = document.getElementById('confirmPasswordError');
const signup_button = document.getElementById("signup-button");
let BASE_URL = "http://localhost:7000";

  // Validate fields
  usernameInput.addEventListener("input", (e) => {
    e.preventDefault();
    const usernameSuccessIcon = document.getElementById('username_success_icon');
    const usernameFailIcon = document.getElementById('username_fail_icon');

    if (!usernameInput.value) {
        display_msg("Username is required", usernameError);
        usernameError.setAttribute("class", "");
        usernameFailIcon.style.display = "inline";
        usernameSuccessIcon.style.display = "none";

      } else if (!isValidUsername(usernameInput.value)){
        display_msg("only special characters allowed '#' '.' '-' '_'", usernameError);
        usernameError.setAttribute("class", "");
        usernameFailIcon.style.display = "inline";
        usernameSuccessIcon.style.display = "none";

      } else if (usernameInput.value.length < 8) {
        display_msg("Username must have atleast 8 characters", usernameError);
        usernameError.setAttribute("class", "");
        usernameFailIcon.style.display = "inline";
        usernameSuccessIcon.style.display = "none";
      } else {
        display_msg("Username success!", usernameError);
        usernameError.setAttribute("class", "success");
        usernameFailIcon.style.display = "none";
        usernameSuccessIcon.style.display = "inline";
      }

  });


firstNameInput.addEventListener("input", (e) => {
    e.preventDefault();
    const firstNameSuccessIcon = document.getElementById('first_name_success_icon');
    const firstNameFailIcon = document.getElementById('first_name_fail_icon');

    if (!firstNameInput.value) {
        display_msg("first name is required", firstNameError);
        firstNameError.setAttribute("class", "");
        firstNameFailIcon.style.display = "inline";
        firstNameSuccessIcon.style.display = "none";

      } else if (!isValidName(firstNameInput.value)) {
        display_msg("first name must contain only alphas", firstNameError);
        firstNameError.setAttribute("class", "");
        firstNameFailIcon.style.display = "inline";
        firstNameSuccessIcon.style.display = "none";
      } else {
        display_msg("first name success!", firstNameError);
        firstNameError.setAttribute("class", "success");
        firstNameFailIcon.style.display = "none";
        firstNameSuccessIcon.style.display = "inline";
      }

  });

  lastNameInput.addEventListener("input", (e) => {
    e.preventDefault();
    const lastNameSuccessIcon = document.getElementById('last_name_success_icon');
    const lastNameFailIcon = document.getElementById('last_name_fail_icon');
    if (!lastNameInput.value) {
        display_msg("last name is required", lastNameError);
        lastNameError.setAttribute("class", "");
        lastNameFailIcon.style.display = "inline";
        lastNameSuccessIcon.style.display = "none";

      } else if (!isValidName(lastNameInput.value)) {
        display_msg("last name must contain only alphas", lastNameError);
        lastNameError.setAttribute("class", "");
        lastNameFailIcon.style.display = "inline";
        lastNameSuccessIcon.style.display = "none";
      } else {
        display_msg("last name success!", lastNameError);
        lastNameError.setAttribute("class", "success");
        lastNameFailIcon.style.display = "none";
        lastNameSuccessIcon.style.display = "inline";
      }

  });

  emailInput.addEventListener("input", (e) => {
    e.preventDefault();
    const emailSuccessIcon = document.getElementById('email_success_icon');
    const emailFailIcon = document.getElementById('email_fail_icon');
    if (!emailInput.value){
        display_msg("email is required", emailError);
        emailError.setAttribute("class", "");
        emailFailIcon.style.display = "inline";
        emailSuccessIcon.style.display = "none";
    } else if (!isValidEmail(emailInput.value)) {
    display_msg("Invalid email address", emailError);
    emailError.setAttribute("class", "");
    emailFailIcon.style.display = "inline";
    emailSuccessIcon.style.display = "none";
  } else {
    display_msg("email success!", emailError);
    emailError.setAttribute("class", "success");
    emailFailIcon.style.display = "none";
    emailSuccessIcon.style.display = "inline";
  }
  });


  passwordInput.addEventListener("input", (e) => {
    const passwordVal = passwordInput.value;
    const passwordSuccessIcon = document.getElementById('passwd_success_icon');
    const passwordFailIcon = document.getElementById('passwd_fail_icon');
  
    if (!passwordVal) {
      display_msg('Password is required', passwordError);
      passwordError.classList.remove("success"); // Use classList for efficiency
      passwordFailIcon.style.display = "inline";
      passwordSuccessIcon.style.display = "none";
    } else if (passwordVal.length < 8) {
      display_msg('Password must be at least 8 characters long', passwordError);
      passwordError.classList.remove("success"); // Use classList for efficiency
      passwordFailIcon.style.display = "inline";
      passwordSuccessIcon.style.display = "none";
    } else {
      display_msg("Password success!", passwordError);
      passwordError.classList.add("success");
      passwordFailIcon.style.display = "none";
      passwordSuccessIcon.style.display = "inline";
    }
  });

  confirmPasswordInput.addEventListener("input", (e) => {
    e.preventDefault();
    confirm_success_icon = document.getElementById('confirm_passwd_success_icon');
    confirm_fail_icon = document.getElementById('confirm_passwd_fail_icon');
    
    if (!confirmPasswordInput.value) {
        display_msg('Confirm password is required', confirmPasswordError);
        confirmPasswordError.setAttribute("class", "");
        confirm_fail_icon.style.display = "inline";
        confirm_success_icon.style.display = "none";

      } else if (confirmPasswordInput.value.length < 8) {
        display_msg('Confirm password must be at least 8 characters long', confirmPasswordError);
        confirmPasswordError.setAttribute("class", "");
        confirm_fail_icon.style.display = "inline";
        confirm_success_icon.style.display = "none";

      } else if (isPasswordEqual(passwordInput.value, confirmPasswordInput.value) === false) {
        display_msg("Passwords do not match", confirmPasswordError);
        confirmPasswordError.setAttribute("class", "");
        confirm_fail_icon.style.display = "inline";
        confirm_success_icon.style.display = "none";

      } else {
        display_msg("Confirm password success!", confirmPasswordError);
        confirmPasswordError.setAttribute("class", "success");
        confirm_success_icon.style.display = "inline";
        confirm_fail_icon.style.display = "none";

      }
  });

//   registrationForm.addEventListener("submit", async (e) => {
//     e.preventDefault(); // Prevent default form submission
//     if (isAllInput()) {
//         const responseData = await postData('/api/users/register', registrationForm);
//         if (responseData) {
//             const handle_response = await handleResponse(responseData);
//         }
//     } else {
//         window.alert("Please fill in all required fields before submitting.");
//     }
// });

function isValidEmail(email) {
  // Regular expression for email validation
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}
function isPasswordEqual(password, confirmPassword) {
    if (password === confirmPassword) {
        return true;
    }
    return false;
}
function display_msg(message, element) {
    element.textContent = message;
}

function isValidName(element_value) {
  // Regular expression to allow letters only
  const namePattern = /^[a-zA-Z\s]+$/;

  // Test if the element value matches the pattern
  return namePattern.test(element_value);
}

function isValidUsername(username_value) {
  // Regular expression to allow letters, numbers, hyphens and periods
  const usernamePattern = /^[a-zA-Z]*[0-9a-zA-Z\#\.\-]+$/;

  // Test if the element value matches the pattern
  return usernamePattern.test(username_value);
}

function isAllInput() {
  const allSmallTags = document.querySelectorAll("small");

  for (const smallTag of allSmallTags) {
    if (!smallTag.getAttribute("class")) {
      window.alert("Please fill in all required fields before submitting.");
      return false;
    }
  }

  return true; // All fields are filled
}
function clearInputFields() {
  const AllInputTags = document.querySelectorAll("input");
  for (const inputTag of AllInputTags) {
    inputTag.value = "";
  }
}



