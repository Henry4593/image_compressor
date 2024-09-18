# Compressio: Effortless image compression for everyone

Compressio is a user-friendly web application that empowers users to compress their images while preserving quality. Built on the robust Flask framework and leveraging the powerful Python Imaging Library (PIL), this application offers a seamless experience for optimizing image files.

## Table of Contents

- [Compressio: Effortless image compression for everyone](#compressio-effortless-image-compression-for-everyone)
  - [Table of Contents](#table-of-contents)
  - [Key Features](#key-features)
    - [Image Compression](#image-compression)
    - [Download Compressed Images](#download-compressed-images)
    - [Intuitive Web Interface](#intuitive-web-interface)
    - [Error Handling:](#error-handling)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation and Setup](#installation-and-setup)
    - [Running the Application](#running-the-application)
  - [Usage](#usage)
    - [Uploading and Compressing Images](#uploading-and-compressing-images)
  - [Docker Integration](#docker-integration)
  - [Contributing](#contributing)
  - [License](#license)
  - [Code Coverage](#code-coverage)

## Key Features

### Image Compression

- Upload your images, and Compressio will handle the compression process, ensuring your files maintain their visual integrity. The application utilizes advanced compression algorithms to reduce file sizes without compromising image quality.

### Download Compressed Images

- Once your images are compressed, you can easily download the optimized versions for further use. This allows you to quickly integrate the compressed images into your projects or share them with others.

### Intuitive Web Interface

- The application's clean and intuitive interface, powered by Flask, provides a smooth and enjoyable user experience. The interface is designed to be user-friendly, making it easy for both novice and experienced users to navigate and use the application.

### Error Handling: 

- Compressio is designed to handle unsupported file formats and compression failures gracefully, providing clear error messages to guide you. This ensures that users can troubleshoot any issues they encounter during the compression process.

## Getting Started

### Prerequisites
To run Compressio, you'll need the following:

- Python 3.6 or higher
- Flask (install via pip install Flask)
- Python Imaging Library (PIL) (install via pip install Pillow)

### Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/Henry4593/image_compressor.git
cd image_compressor
```
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```
### Running the Application

1. Navigate to the project directory:
```bash
cd image_compressor
```
2. Start the Flask application:
```bash
flask run
```
3. Open your web browser and go to http://localhost:7000 to access Compressio.

## Usage

### Uploading and Compressing Images

1. Visit the Compressio web application on your web browser http://localhost:7000.
2. You will be redirected to the landing page. Click "get-started" on the bottom left of the page or in the navigation bar.
3. If you already have an account, input your information on the login form. If you don't have an account, click the hyperlink "signup" to register on the Compressio app.
4. Click the "Cloud" icon to select the image you want to compress or drag and drop the selected images on the "dashed zone".
5. The image(s) will automatically be compressed and made available on the "myfiles" navigation.
6. Navigate to "myfiles" on the navigation bar to preview and download your compressed images to your local machine.

## Docker Integration
Compressio can also be run using Docker and Docker Compose for easier deployment and distribution.
Ensure you have Docker and Docker Compose installed.
1. Build the Docker image:
```bash
docker build -t image_compressor .
```
2. Start the application using Docker Compose:
```bash
docker-compose up -d
```
3. Access the application at http://localhost:7000.

##  Contributing

Contributions to Compressio are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENCE) file for more details.

## Code Coverage

For comprehensive information about the project's code coverage, please refer to the Code Coverage Report.
see the [Code Coverage Report](./CODE_COVERAGE.md)

