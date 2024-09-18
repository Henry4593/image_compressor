const loginFormElement = document.getElementById("loginForm")
const username_email = document.getElementById("username");
const password = document.getElementById("password");
const username_msg = document.getElementById("username_msg");
const password_msg = document.getElementById("password_msg");
const submit_button = document.getElementById("login-button");
const passwd_exclamation_icon = document.getElementById("passwd_fail_icon");
const passwd_success_icon = document.getElementById("passwd_success_icon")
const usrnm_exclamation_icon = document.getElementById("usrnm_fail_icon");
const usrnm_success_icon = document.getElementById("usrnm_success_icon");
// const BASE_URL = "http://localhost:7000";

const passwordReveal = document.querySelector(".password-reveal");
passwordReveal.addEventListener("click", (e) => {
  togglePassword();
});

username_email.addEventListener("input", (e) => {
  var username = username_email.value;
  username.replace(/\s/g, "");

  if (!username) {
    username_msg.setAttribute("id", "fail")
    display_msg("Email or username Required!", username_msg);
    usrnm_exclamation_icon.setAttribute("id", "fail_icon");
    usrnm_success_icon.setAttribute("id", "");
  } else if (username.length < 6) {
    username_msg.setAttribute("id", "fail")
    display_msg("Username should be at least 6 characters", username_msg);
    usrnm_exclamation_icon.setAttribute("id", "fail_icon");
    usrnm_success_icon.setAttribute("id", "");

  } else if (username.includes("@") && !isValidEmail(username)){
    username_msg.setAttribute("id", "fail")
    display_msg("Invalid email format", username_msg);
    usrnm_exclamation_icon.setAttribute("id", "fail_icon");
    usrnm_success_icon.setAttribute("id", "");
  }else {
    username_msg.setAttribute("id", "success")
    display_msg("Username or email success!", username_msg);
    usrnm_success_icon.setAttribute("id", "success_icon");
    usrnm_exclamation_icon.setAttribute("id", "");
  }
});

username_email.addEventListener("blur", (e) => {
  display_msg("", username_msg);
  usrnm_success_icon.setAttribute("id", "");
  usrnm_exclamation_icon.setAttribute("id", "");

});

password.addEventListener("input", (e) => {
  const password_val = password.value;

  if (!password_val) {
    password_msg.setAttribute("id", "fail");
    display_msg("Password Required!", password_msg);
    passwd_exclamation_icon.setAttribute("id", "fail_icon");
    passwd_success_icon.setAttribute("id", "");
  } else if (password_val.length < 8) {
    password_msg.setAttribute("id", "fail");
    display_msg("Password should be at least 8 characters", password_msg);
    passwd_exclamation_icon.setAttribute("id", "fail_icon");
    passwd_success_icon.setAttribute("id", "");
  } else if (!isValidPassword(password_val)) {
    password_msg.setAttribute("id", "fail");
    display_msg("Password must contain at least an uppercase and lowercase letter", password_msg);
    passwd_exclamation_icon.setAttribute("id", "fail_icon");
    passwd_success_icon.setAttribute("id", "");
  } else {
    password_msg.setAttribute("id", "success");
    display_msg("Password success!", password_msg);
    passwd_exclamation_icon.setAttribute("id", "");
    passwd_success_icon.setAttribute("id", "success_icon");
  }
});

password.addEventListener("blur", (e) => {
  e.preventDefault();
  display_msg("", password_msg);
  passwd_exclamation_icon.setAttribute("id", "");
  passwd_success_icon.setAttribute("id", "");
});

// loginFormElement.addEventListener("submit", (e) => {
//   e.preventDefault();
//   PostLogin("/api/users/login", loginFormElement);
// });

function togglePassword() {
  const passwordInput = document.getElementById('password');
  if (passwordInput.type === 'password') {
    passwordInput.type = 'text';
  } else {
    passwordInput.type = 'password';
  }
}

function display_msg(text, element) {
  element.textContent = text;
}

function isValidEmail(email) {
  // Regular expression for email validation
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

function isValidPassword(password) {
  // Check for at least one uppercase and one lowercase letter
  return /^(?=.*[a-z])(?=.*[A-Z]).*$/g.test(password);
}

// async function PostLogin(endpoint, form_data) {
//   const API_URL = BASE_URL + endpoint;
//   const form_data_object = new FormData(form_data);

//   try {
//     const response = await fetch(API_URL, {
//       method: "POST",
//       body: form_data_object,
//     });

//     if (!response.ok) {
//       const error = await response.json();
//       password_msg.setAttribute("id", "fail");
//       display_msg(error.message, password_msg);
//       passwd_exclamation_icon.setAttribute("id", "fail_icon");
//       passwd_success_icon.setAttribute("id", "");
      
//       throw new Error(error.message);
//     }

//     const data = await response.json();
//     if (data.message === "true") {
//       window.location.href = "upload.html";
//     }
//   } catch (error) {
//     console.error(error);
//   }
// }