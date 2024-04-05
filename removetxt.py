import cv2
import pytesseract
import os

def detect_and_make_text_black(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use Tesseract OCR to detect text regions
    text_data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)
    
    # Iterate over each detected text region
    for i in range(len(text_data['text'])):
        x, y, w, h = text_data['left'][i], text_data['top'][i], text_data['width'][i], text_data['height'][i]
        text = text_data['text'][i]
        conf = int(text_data['conf'][i])

        # If the confidence level is high and the text is not empty
        if conf > 60 and text.strip():
            # Draw a black rectangle over the detected text region
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 0), -1)

    return image

# Function to process all images in a folder
def process_images_in_folder(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
     

    index=1
    # List all files in the input folder
    # for filename in os.listdir(input_folder):
    #     if filename.endswith(('.jpg', '.jpeg', '.png')):  # Filter images
            # Construct input and output paths
            
    input_image_path = os.path.join(input_folder, '191503-img-00002-00033.png')
    output_image_path = os.path.join(output_folder, f"{index}testIMG.png")

            # Process the image
    output_image = detect_and_make_text_black(input_image_path)

            # Save the modified image
    cv2.imwrite(output_image_path, output_image)
    index+=1
# Example usage
input_folder = 'C:/Users/hp/Downloads/final extracted images/final extracted images/191503/Patient-SRINIVAS/Study-2158771-CT-CT- BRAIN PLAIN[20200509]/Series-002'
output_folder = 'D:/capstone codes/testimages'
process_images_in_folder(input_folder, output_folder)
