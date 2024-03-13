from PIL import Image, ImageDraw, ImageFont
import textwrap

# Load the images
img1_path = 'D:\\PROJETS\\seed\\bouche_ouverte.png'
img2_path = 'D:\\PROJETS\\seed\\bouche_fermee.png'
img3_path = 'D:\\PROJETS\\seed\\heureux.png'  # Load image3

img1 = Image.open(img1_path)
img2 = Image.open(img2_path)
img3 = Image.open(img3_path)

# Define a function to add text progressively with wrapping
def add_text_to_speech_bubble(image, text, position, font_size=100, max_width=800):
    """
    Add text to an image progressively, word by word, with text wrapping.
    
    :param image: PIL Image object
    :param text: Text to add
    :param position: Tuple (x, y) where to start adding the text
    :param font_size: Size of the font
    :param max_width: Maximum width of the text before wrapping
    :return: List of PIL Image objects with text added progressively
    """
    # Load a font
    font = ImageFont.truetype("arial.ttf", font_size)
    
    # Wrap the text
    wrapped_text = textwrap.fill(text, width=30)  # Adjust width as needed
    
    # List to store images
    images_with_text = []
    
    # Split the wrapped text into words
    words = wrapped_text.split()
    
    # Add words to the image one by one
    for i in range(len(words)+1):
        # Copy the image so we don't draw over it
        img_with_text = image.copy()
        draw = ImageDraw.Draw(img_with_text)
        
        # Current text is the first i words
        current_text = ' '.join(words[:i])
        
        # Re-wrap the current text to maintain the structure
        current_wrapped_text = textwrap.fill(current_text, width=25)  # Adjust width as needed
        
        # Add the text to the image
        draw.multiline_text(position, current_wrapped_text, font=font, fill="black")
        
        # Append the image with the current text to the list
        images_with_text.append(img_with_text)
    
    return images_with_text

# French text to add to the image
french_text = "Tu as très bien réussi !​ L'extrados permet de faire voler les avions"

# Position of the text in the speech bubble, assuming the speech bubble is in a similar position in both images
text_position = (800, 100)  # Adjust as needed for your images

# Add text to both images progressively
frames_with_text_1 = add_text_to_speech_bubble(img1, french_text, text_position)
frames_with_text_2 = add_text_to_speech_bubble(img2, french_text, text_position)
# Add text to the final image (image3)
final_frame_with_text = add_text_to_speech_bubble(img3, french_text, text_position)[-1]

# Combine the frames with alternating mouth images, text added progressively, and the final image with text
frames = [frame for pair in zip(frames_with_text_1, frames_with_text_2) for frame in pair] + [final_frame_with_text]

# Set the duration for displaying each frame
duration_per_frame = 200  # 200 ms per frame for 0.2 seconds as specified
final_frame_duration = 5000  # This will keep the final image for 5 seconds

# Save the combined frames as a GIF without looping and with the final image staying longer
gif_path = 'D:\\PROJETS\\seed\\speaking_animation_with_french_text.gif'
frames[0].save(
    gif_path,
    format='GIF',
    append_images=frames[1:],
    save_all=True,
    duration=[duration_per_frame]*(len(frames)-1) + [final_frame_duration],  # Set duration for each frame except the last
    loop=1  # Set loop to 1 so it does not loop
)

print(gif_path)
