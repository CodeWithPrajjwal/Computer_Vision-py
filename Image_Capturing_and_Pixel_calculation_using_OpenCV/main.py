# import cv2

# def capture_and_save_image():
#     # Open the webcam
#     cap = cv2.VideoCapture(0)
#     if not cap.isOpened():
#         print("Error: Could not access the webcam.")
#         return

#     print("Press 's' to capture the image and save, or 'q' to quit.")

#     while True:
#         # Read frames from the webcam
#         ret, frame = cap.read()
#         if not ret:
#             print("Error: Failed to capture frame.")
#             break
        
#         # Display the frame
#         cv2.imshow("Webcam - Press 's' to capture or 'q' to quit", frame)

#         # Wait for a key press
#         key = cv2.waitKey(1) & 0xFF
        
#         # If 's' is pressed, capture and save the image
#         if key == ord('s'):
#             # Get the dimensions of the image
#             height, width, channels = frame.shape
#             total_pixels = height * width
            
#             print(f"Image captured! Dimensions: {width}x{height}, Total Pixels: {total_pixels}")

#             # Save the image in JPG and PNG formats
#             jpg_filename = "captured_image.jpg"
#             png_filename = "captured_image.png"
#             cv2.imwrite(jpg_filename, frame)
#             cv2.imwrite(png_filename, frame)

#             print(f"Image saved as '{jpg_filename}' and '{png_filename}'.")
#             break
        
#         # If 'q' is pressed, quit the program
#         elif key == ord('q'):
#             print("Exiting without saving.")
#             break

#     # Release the webcam and close all OpenCV windows
#     cap.release()
#     cv2.destroyAllWindows()

# # Run the function
# capture_and_save_image()


import cv2

def capture_and_write_text_on_image():
    # Open the webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return

    print("Press 's' to capture the image with text, or 'q' to quit.")

    while True:
        # Read frames from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Display the frame
        cv2.imshow("Webcam - Press 's' to capture or 'q' to quit", frame)

        # Wait for a key press
        key = cv2.waitKey(1) & 0xFF

        # If 's' is pressed, capture the image and write text
        if key == ord('s'):
            # Get dimensions of the image
            height, width, channels = frame.shape
            total_pixels = height * width
            text = f"Dimensions: {width}x{height}, Total Pixels: {total_pixels}"

            # Add the text to the image
            font = cv2.FONT_HERSHEY_DUPLEX
            position = (10, 50)  # Position of the text (x, y)
            font_scale = 0.7       # Font size
            color = (0, 255, 0)  # Text color (BGR format)
            thickness = 3        # Thickness of the text

            # Write the text on the image
            cv2.putText(frame, text, position, font, font_scale, color, thickness)

            # Save the image
            filename = "captured_image_with_text.jpg"
            cv2.imwrite(filename, frame)

            print(f"Image saved with text as '{filename}'.")
            break

        # If 'q' is pressed, quit the program
        elif key == ord('q'):
            print("Exiting without capturing.")
            break

    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# Run the function
capture_and_write_text_on_image()
