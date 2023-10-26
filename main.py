#Code designed for RAW to JPEG you can use any raw file type just have to replace the appropriate extension wherever needed in the code.
#the code supports .cr2 (canon), .nef (nikon), .arw (sony)
#Developed by Debarun Ghosh
import os
import rawpy
from PIL import Image, ImageEnhance
import numpy as np

def convert_raw_to_jpeg(input_folder, output_folder, brightness_factor=1.0, contrast_factor=1.0, saturation_factor=1.0):
    for root, _, files in os.walk(input_folder):
        for file in files:
            # Check if the file is a raw image (you can adjust the file extensions for other raw formats)
            if file.lower().endswith((".cr2", ".nef", ".arw")):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".jpg")
                
                # Read the raw file using the appropriate library (rawpy for CR2, other libraries for other formats)
                # You may need to use different libraries for different raw formats.
                with rawpy.imread(input_path) as raw:
                    rgb = raw.postprocess()
                
                # Convert to a Pillow Image
                image = Image.fromarray(rgb)
                
                # Apply light adjustments to the color image
                enhancer = ImageEnhance.Brightness(image)
                image = enhancer.enhance(brightness_factor)
                
                enhancer = ImageEnhance.Contrast(image)
                image = enhancer.enhance(contrast_factor)
                
                enhancer = ImageEnhance.Color(image)
                image = enhancer.enhance(saturation_factor)
                
                # Convert the image to YCbCr color space
                ycbcr_image = image.convert("YCbCr")
                y, cb, cr = ycbcr_image.split()
                
                # Perform histogram equalization on the Y channel (luminance)
                y = equalize_histogram(y)
                
                # Merge the YCbCr channels back into a color image
                equalized_ycbcr_image = Image.merge("YCbCr", (y, cb, cr))
                
                # Convert back to RGB color space
                equalized_image = equalized_ycbcr_image.convert("RGB")
                
                # Save as JPEG
                equalized_image.save(output_path, "JPEG")

def equalize_histogram(channel):
    np_channel = np.array(channel)
    hist, bins = np.histogram(np_channel, bins=256, range=(0, 256))
    cdf = hist.cumsum()
    cdf = 255 * cdf / cdf[-1]
    equalized_channel = np.interp(np_channel, bins[:-1], cdf)
    return Image.fromarray(equalized_channel.astype(np.uint8))

if __name__ == "__main__":
    input_folder = "path_to_raw_files"
    output_folder = "output_path"
    brightness_factor = 1.2  # Adjust as needed
    contrast_factor = 1.2  # Adjust as needed
    saturation_factor = 1.2  # Adjust as needed

    convert_raw_to_jpeg(input_folder, output_folder, brightness_factor, contrast_factor, saturation_factor)
