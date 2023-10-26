# Raw to JPEG Converter with Image Enhancement

This Python script is designed to convert raw image files (e.g., CR2 for Canon, NEF for Nikon, ARW for Sony) to JPEG format while simultaneously enhancing the image quality. It performs a sequence of image processing operations, including brightness, contrast, and saturation adjustments, along with histogram equalization, to create visually appealing and enhanced JPEG images. The end result is a well-balanced and visually pleasing image with improved contrast, all while preserving the original color balance.

## Features

- **Raw to JPEG Conversion**: The script efficiently converts raw files to the widely supported JPEG format, making your raw images more accessible and shareable.

- **Image Enhancement**: The script applies a set of image adjustments to enhance the overall quality of the image. These adjustments include:
  - **Brightness Enhancement**: Adjust the image's brightness level for better visibility.
  - **Contrast Enhancement**: Improve the distinction between different parts of the image.
  - **Saturation Enhancement**: Adjust the color saturation for a more vibrant appearance.
  - **Histogram Equalization**: Reduces noise and enhances overall image quality, resulting in a well-balanced and visually appealing image.

- **Customization**: The script provides flexibility in adjusting enhancement parameters, including brightness, contrast, and saturation. This allows you to fine-tune the output image according to your preferences.

## Requirements

To use this script, you'll need the following prerequisites:

- Python 3.x
- Python libraries: Pillow (PIL), rawpy, numpy

You can install the required libraries using `pip`:

```bash
pip install pillow rawpy numpy
```
## Installation
1. Clone the Repository: Begin by cloning this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/raw-to-jpeg-converter.git
   ```
2. Navigate to the Project Folder: Change your current directory to the project folder:
   ```bash
   cd raw-to-jpeg-converter
   ```
3. Prepare Raw Image Files: Place your raw image files in a directory of your choice. Supported file extensions include .cr2, .nef, .arw, and more. The script can be customized to support additional formats.

## Usage
The script offers customization through the following parameters, which allow you to fine-tune the image enhancement settings:

* Brightness_factor: Adjust the brightness level of the image to enhance visibility.
* Contrast_factor: Modify the image's contrast to improve detail visibility.
* Saturation_factor: Adjust the color saturation to achieve a more vibrant appearance.

Feel free to experiment with these factors to achieve your desired image appearance.

## Contributing
If you wish to contribute to this project or make improvements, follow the standard GitHub contribution process:

1. Fork the project.
2. Create a new branch for your changes.
3. Commit your changes and push them to your fork.
4. Create a pull request with a clear description of your changes.

## Developed by
Debarun Ghosh
