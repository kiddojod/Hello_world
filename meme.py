import random
import os
from PIL import Image

# Sample moods and quotes
moods = ["Angsty", "Zen", "Chaotic", "Dramatic", "Hyper", "Existential"]
quotes = {
    "Angsty": [
        "I’m not okay, but I smile anyway.",
        "Leave me alone. Or don’t. Whatever."
    ],
    "Zen": [
        "Let that sh*t go.",
        "You are exactly where you need to be."
    ],
    "Chaotic": [
        "Why walk when you can cartwheel?",
        "Rules are optional."
    ],
    "Dramatic": [
        "This is the worst day of my life… again.",
        "I am the main character."
    ],
    "Hyper": [
        "COFFEE! COFFEE! COFFEE!",
        "Everything is AWESOME!!!"
    ],
    "Existential": [
        "Do we even exist?",
        "The universe doesn’t care. And that’s freeing."
    ]
}

# Local folder for meme images
meme_folder = "memes"  # Make sure this folder exists with some images in it

def generate_meme_mood():
    mood = random.choice(moods)
    quote = random.choice(quotes[mood])

    print(f"\n🧠 Mood: {mood}")
    print(f"💬 Quote: \"{quote}\"")

    # Pick a random image from the meme folder
    meme_images = [img for img in os.listdir(meme_folder) if img.endswith((".jpg", ".png", ".jpeg"))]
    if meme_images:
        image_path = os.path.join(meme_folder, random.choice(meme_images))
        img = Image.open(image_path)
        img.show()
    else:
        print("No meme images found in the folder!")

# Run it
if __name__ == "__main__":
    generate_meme_mood()
