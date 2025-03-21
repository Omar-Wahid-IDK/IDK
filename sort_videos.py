import os
import shutil

# --------------------------------------------------------------------------------- Folders
VID_FOLDER = r"C:\Users\Omar\Downloads\Video"
SORTED_FOLDERS = {
    "ar12": r"E:\Media Player\Videos\Youtube\AR12",#------------------------------- Videos
    "mrwhosetheboss": r"E:\Media Player\Videos\Youtube\Mrwhosetheboss",
    "scrapman": r"E:\Media Player\Videos\Youtube\Scrap Man",
    "kangaming": r"E:\Media Player\Videos\Youtube\Kan Gaming",
    "matarmstrong": r"E:\Media Player\Videos\Youtube\Mat Armstrong",
    "etc": r"E:\Media Player\Videos\Youtube\Etc",
    "solo leveling": r"E:\Media Player\Videos\Anime\Solo Leveling",#--------------- Anime
    "ao no hako": r"E:\Media Player\Videos\Anime\Blue Box",
    "class no daikirai na joshi to kekkon suru koto ni natta": r"E:\Media Player\Videos\Anime\I'm Getting Married to a Girl I Hate in My Class"
}

# Ensure all folders exist
for folder in SORTED_FOLDERS.values():
    os.makedirs(folder, exist_ok=True)

# --------------------------------------------------------------------------------- Sorting Function
def get_channel_folder(filename):
    """Returns the correct folder based on the video filename."""
    lower_name = filename.lower()
    
    for channel, folder in SORTED_FOLDERS.items():
        if channel in lower_name:
            return folder
    
    return SORTED_FOLDERS["etc"]  # Default to 'etc' if no match

def move_videos():
    """Move videos to their respective folders based on channel names."""
    moved_files = 0  

    for file in os.listdir(VID_FOLDER):
        src = os.path.join(VID_FOLDER, file)
        
        if not os.path.isfile(src):  
            continue  # Skip non-file items

        dest_folder = get_channel_folder(file)
        dest = os.path.join(dest_folder, file)

        try:
            shutil.move(src, dest)
            print(f"✅ Moved: {file} → {dest_folder}")
            moved_files += 1
        except Exception as e:
            print(f"❌ Error moving {file}: {e}")

    if moved_files == 0:
        print("No videos found to move.")

# --------------------------------------------------------------------------------- Run the script
if __name__ == "__main__":
    move_videos()
