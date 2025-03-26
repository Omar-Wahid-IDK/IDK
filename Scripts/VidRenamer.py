import os
import re

# Paths
VID_FOLDER = r"C:\Users\Omar\Downloads\Video"
CHANNELS_FILE = r"E:\Projects\VidHandler\youtube_channels.txt"

# 🔹 Load YouTube channel names from the file
def get_channel_mapping():
    channel_mapping = {}
    
    try:
        with open(CHANNELS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(" | ")
                if len(parts) == 2:
                    video_title, channel_name = parts
                    channel_mapping[clean_text(video_title)] = channel_name  # Store cleaned title for matching
                else:
                    print(f"⚠ Skipping invalid line: {line.strip()} (wrong format)")
    except FileNotFoundError:
        print(f"❌ ERROR: File {CHANNELS_FILE} not found!")
    
    print(f"✅ Loaded {len(channel_mapping)} entries from {CHANNELS_FILE}")
    return channel_mapping

# 🔹 Function to clean text (remove special characters, numbers, etc.)
def clean_text(text):
    """Convert filename to a standard format for matching."""
    text = text.lower()
    text = text.replace("_", " ")  # Treat underscores as spaces
    text = text.replace(":", " ")  # Treat colons as spaces
    text = re.sub(r"[^\w\s]", "", text)  # Remove special characters except spaces
    text = re.sub(r"\s+", " ", text).strip()  # Normalize multiple spaces
    return text

# 🔹 Rename video files with the correct channel name
def rename_videos():
    channel_mapping = get_channel_mapping()
    
    print(f"🔍 Checking files in: {VID_FOLDER}")
    
    for file in os.listdir(VID_FOLDER):
        file_path = os.path.join(VID_FOLDER, file)
        if not os.path.isfile(file_path):
            continue  # Skip if it's not a file
        
        # 🔹 Clean filename before matching
        file_name, file_ext = os.path.splitext(file)
        clean_name = clean_text(file_name)

        # 🔹 Try to find a match in youtube_channels.txt
        matched_channel = None
        for video_title, channel_name in channel_mapping.items():
            if video_title in clean_name:  # Check if cleaned title is in filename
                matched_channel = channel_name
                break  # Stop searching once we find a match
        
        if matched_channel:
            new_file_name = f"{matched_channel} - {file}"
            new_file_path = os.path.join(VID_FOLDER, new_file_name)
            os.rename(file_path, new_file_path)
            print(f"✅ Renamed: {file} → {new_file_name}")
        else:
            print(f"⚠ No match found for: {file}")
    open(CHANNELS_FILE, "w").close()
    print("🧹 Cleaned up youtube_channels.txt!")        

# Run the script
if __name__ == "__main__":
    rename_videos()
