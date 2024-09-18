#!/usr/bin/node

function isValidUsername(username_value) {
    // Regular expression to allow letters, spaces, hyphens, apostrophes, and periods
    const usernamePattern = /^[a-zA-Z]+[0-9a-zA-Z\#\.\-]+$/;
  
    // Test if the element value matches the pattern
    return usernamePattern.test(username_value);
  }

  const username = "John.Demure1234@";
  if (isValidUsername(username)) {
    console.log("Username is valid");
  } else {
    console.log("Username is invalid");
  }