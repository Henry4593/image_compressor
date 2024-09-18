const dropZone = document.querySelector('.upload-box');
const body = document.querySelector(".container-image-form");
const dropZoneMsg = document.querySelector('#drop-zone h1');
const outsideDropzone = document.querySelector('body');
const fileInput = document.querySelector('#image');
const imageList = document.querySelector('#image-list');
const progressBar = document.querySelector('#progress-bar');
const progress = document.querySelector('#progress');
const uploadStatus = document.createElement("p");

var BASE_URL = "http://localhost:7000";

// Handle file input change
fileInput.addEventListener("change", async (event) => {
  event.preventDefault();
  const files = event.target.files;

  if (files.length === 0) {
    updateUploadStatus("Please select at least one image to upload");
    return;
  }

  try {
    const formData = new FormData();
    for (const file of files) {
      formData.append('image', file);
    }

    updateUploadStatus('Uploading images...');
    const response = await fetch(BASE_URL + "/api/compress", {
      method: 'POST',
      body: formData
    });

    if (response.ok) {
      const data = await response.json()
      alert(data["message"]);
      updateUploadStatus(data["message"]);
    } else {
      updateUploadStatus('failed to upload file');
    }
  } catch (error) {
    console.error('Error uploading images:', error);
    body.innerHTML = "";
    updateUploadStatus('Internal server error 500');
  }
});

// Handle drag over event
dropZone.addEventListener('dragover', (e) => {
  e.preventDefault();
  dropZone.style.borderColor = '#f00'; // Highlight drop zone
});

// Handle drop event
dropZone.addEventListener('drop', async (e) => {
  e.preventDefault();
  dropZone.style.borderColor = '#454545'; // Reset border color
  const files = e.dataTransfer.files;

  if (files.length === 0) {
    updateUploadStatus("Please select at least one image to upload");
    return;
  }

  try {
    handleFiles(files); // Use existing files variable

    const formData = new FormData();
    for (const file of files) {
      formData.append('image', file);
    }

    updateUploadStatus('Uploading images...');
    const response = await fetch(BASE_URL + "/api/compress", {
      method: 'POST',
      body: formData
    });

    if (response.ok) {
      const data = await response.json()
      updateUploadStatus(data["message"]);
      // updateUploadStatus('Images uploaded successfully!');
    } else {
      updateUploadStatus('Error uploading images. Please try again later.');
    }
  } catch (error) {
    console.error('Error uploading images:', error);
    body.innerHTML = "";
    updateUploadStatus('Error uploading images. Please try again later.');
  }
});

// Handle drag leave event
dropZone.addEventListener('dragleave', (e) => {
  e.preventDefault();
  dropZone.style.borderColor = '#454545'; // Reset border color
});

// Prevent default behavior for body drag events
outsideDropzone.addEventListener('dragover', (event) => {
  event.preventDefault();
});

outsideDropzone.addEventListener('dragleave', (event) => {
  event.preventDefault();
});

outsideDropzone.addEventListener('drop', (event) => {
    event.preventDefault();
  });
  
  // Function to handle file uploads
  async function handleFiles(files) {
    if (files.length === 0) {
      alert('No files selected!');
      return;
    }
  
    const fileList = Array.from(files);
  
    clearContent(); // Clear previous content
    fileList.forEach(async (file) => {
      if (file.type.startsWith('image/')) {
        const reader = new FileReader();
  
        reader.onload = function(event) {
          // Create an image element to display
          const img = document.createElement('img');
          const imgDescription = document.createElement('p');
          const imgContainer = document.createElement('div');
          img.src = event.target.result;
          img.alt = file.name;
          img.style.maxWidth = '100px'; // Adjust as needed
          img.style.margin = '10px';
          imgDescription.textContent = file.name;
          imgContainer.classList.add('image-container');
  
          // Append image to the image list
          imageList.appendChild(imgContainer);
          imgContainer.appendChild(img);
          imgContainer.appendChild(imgDescription);
        };
  
        reader.readAsDataURL(file);
      } else {
        alert(`${file.name} is not an image file.`);
      }
    });
  }
  
  // Function to clear content
  function clearContent() {
    imageList.innerHTML = ""; // Clear previous uploads
  }
  
  function updateUploadStatus(text) {
    body.textContent = text;
  }