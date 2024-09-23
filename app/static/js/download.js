const downloadContainer = document.querySelector(".download-container");
const tableWrap = document.querySelector(".table-wrap");
const myFiles = document.getElementById("user-files");
const downloadButtons = document.querySelectorAll(".download-btn")
const BASE_URL = "http://localhost:7000";


document.addEventListener('DOMContentLoaded', (event) => {
    myFiles.addEventListener("click", async (event) => {
        event.preventDefault(); // Prevent default action
    
        try {
            const response = await fetch(`${BASE_URL}/api/images`);
            if (response.ok) {
                const data = await response.json();
                console.log(data); // Log the response data to check its structure
    
                if (Array.isArray(data.images)) {
                    display_msg("Compressed images retrieved successfully", downloadContainer);
                
                    // Clear previous images before displaying new ones
                    downloadContainer.innerHTML = '';

                    // create table wrap
                    const tableWrap = document.createElement("div");
                    tableWrap.classList.add("table-wrap");
                    downloadContainer.appendChild(tableWrap);
                
                    // Create a table and table header
                    const table = document.createElement("table");
                    const headerRow = document.createElement("tr");
                
                    // Define headers
                    const headers = ['Delete', 'Filename', 'Original Size', 'Compressed Size', 'Actions'];
                    headers.forEach(header => {
                        const th = document.createElement("th");
                        th.textContent = header;
                        th.style.color = "#fff";
                        th.style.backgroundColor = "#454545";
                        th.style.textAlign = "left";
                        th.style.padding = "5px 10px";
                        headerRow.appendChild(th);
                    });
                    headerRow.style.color = "#fff";
                    headerRow.style.backgroundColor = "#454545";
                    table.appendChild(headerRow);
                
                    // Populate table with image data
                    data.images.forEach(image => {
                        const row = document.createElement("tr");
                
                        // Create cells for each piece of data
                        const deleteCell = document.createElement("td");
                        deleteCell.innerHTML = '<i class="fa-solid fa-circle-xmark" style="color: #f92424; cursor: pointer;"></i>'; // Use innerHTML for the icon
                
                        const filenameCell = document.createElement("td");
                        filenameCell.textContent = image.filename;
                
                        const originalSizeCell = document.createElement("td");
                        originalSizeCell.textContent = roundToTwoDecimalPlaces(image.original_size / 1024) + " KB";
                
                        const compressedSizeCell = document.createElement("td");
                        compressedSizeCell.textContent = roundToTwoDecimalPlaces(image.compressed_size / 1024) + " KB";
                
                        const actionsCell = document.createElement("td");
                        const previewButton = document.createElement("button");
                        previewButton.className = "preview-btn";
                        previewButton.id = image.image_id;
                        previewButton.textContent = "Preview";
                
                        const downloadButton = document.createElement("button");
                        downloadButton.className = "download-btn";
                        downloadButton.id = image.image_id;
                        downloadButton.textContent = "Download";
                
                        actionsCell.appendChild(previewButton);
                        actionsCell.appendChild(downloadButton);
                
                        // Append cells to the row
                        row.appendChild(deleteCell); // Append the deleteCell to the row
                        row.appendChild(filenameCell);
                        row.appendChild(originalSizeCell);
                        row.appendChild(compressedSizeCell);
                        row.appendChild(actionsCell);
                
                        // Append the row to the table
                        table.appendChild(row);
                    });
                
                    // Append the table to the table wrap
                    downloadContainer.appendChild(tableWrap);
                    tableWrap.appendChild(table);
                
                } else {
                    throw new Error("Invalid data format: 'images' is not an array");
                }
            } else {
                throw new Error("Failed to retrieve images: " + response.statusText);
            }
        } catch (error) {
            console.error(error);
            display_msg("Error retrieving images: " + error.message, downloadContainer);
        }
    });
    
    downloadContainer.addEventListener('click', (event) => {
        if (event.target.classList.contains('download-btn')) {
            const imageId = event.target.id;
            const link = document.createElement('a');
            link.href = `${BASE_URL}/api/images/${imageId}`;
            link.download = '';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }
    });
});

function display_msg(text, element) {
    element.textContent = text;
  }

  function roundToTwoDecimalPlaces(number) {
    return Math.round(number * 100) / 100;
  }





