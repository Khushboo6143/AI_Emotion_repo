# Dictionary mapping emojis to emotions
emoji_to_emotion = {
    "😀": "Happy",
    "😢": "Sad",
    "😡": "Angry",
    "😂": "Laughing",
    "😍": "Loving",
    "😱": "Shocked",
    "😴": "Sleepy",
    "😎": "Cool",
    "🥺": "Pleading",
    "😐": "Neutral",
    "😇": "Blessed",
    "🥳": "Celebrating",
    "😭": "Crying",
    "😤": "Frustrated",
    "🤔": "Thinking",
    "😜": "Playful",
    "😋": "Tasty",
    "🤗": "Hugging",
    "🤩": "Excited",
    "😞": "Disappointed",
    "🤫": "Secretive",
}

def identify_emotion(emoji):
    # Look up the emoji in the dictionary and return the corresponding emotion
    return emoji_to_emotion.get(emoji, "Emotion not found")

# Get user input for the emoji
user_input = input("Enter an emoji: ")

# Identify the emotion
emotion = identify_emotion(user_input)

# Display the result
print(f"The emotion for {user_input} is: {emotion}")