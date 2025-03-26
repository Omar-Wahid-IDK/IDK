import os
import shutil

# --------------------------------------------------------------------------------- Folders
VID_FOLDER = r"C:\Users\Omar\Downloads\Video"
SORTED_FOLDERS = {
    "ar12gaming": r"E:\Media Player\Videos\Youtube\AR12", # ------------------------------- Videos
    "mrwhosetheboss": r"E:\Media Player\Videos\Youtube\Mrwhosetheboss",
    "finoggin": r"E:\Media Player\Videos\Youtube\Finoggin",
    "rufus stories": r"E:\Media Player\Videos\Youtube\Rufus Stories",
    "crainer": r"E:\Media Player\Videos\Youtube\Crainer",
    "camodo gaming": r"E:\Media Player\Videos\Youtube\Camodo Gaming",
    "bigtime": r"E:\Media Player\Videos\Youtube\Big Time",
    "slogo": r"E:\Media Player\Videos\Youtube\Slogo",
    "donut": r"E:\Media Player\Videos\Youtube\Donut Media",
    "mrbeast": r"E:\Media Player\Videos\Youtube\Mr Beast",
    "darkviperau": r"E:\Media Player\Videos\Youtube\Dark Viper Au",
    "scrapman": r"E:\Media Player\Videos\Youtube\Scrap Man",
    "kangaming": r"E:\Media Player\Videos\Youtube\Kan Gaming",
    "mat armstrong": r"E:\Media Player\Videos\Youtube\Mat Armstrong",
    "etc": r"E:\Media Player\Videos\Youtube\Etc",
    "solo leveling": r"E:\Media Player\Videos\Anime\Solo Leveling",  # --------------- Anime
    "ao no hako": r"E:\Media Player\Videos\Anime\Blue Box",
    "classroom of the elite": r"E:\Media Player\Videos\Anime\Classroom Of The Elite",
    "more than a married couple, but not lovers": r"E:\Media Player\Videos\Anime\More Than A Married Couple, But Not Lovers",
    "class no daikirai na joshi to kekkon suru koto ni natta": r"E:\Media Player\Videos\Anime\I'm Getting Married to a Girl I Hate in My Class"
}

# --------------------------------------------------------------------------------- Ensure Folders Exist
for key, folder in SORTED_FOLDERS.items():
    folder = folder.strip()  # Remove accidental spaces
    SORTED_FOLDERS[key] = folder  # Update the dictionary with the cleaned path

    # Debugging: Check the exact folder path
    print(f"Checking folder: {repr(folder)}")

    if not os.path.exists(folder):
        print(f"Creating folder: {folder}")  # Debugging print
        os.makedirs(folder, exist_ok=True)

# --------------------------------------------------------------------------------- Sorting Function
def get_channel_folder(filename):
    """Returns the correct folder based on the video filename."""
    lower_name = filename.lower()

    for channel, folder in SORTED_FOLDERS.items():
        if channel.lower() in lower_name:  # Case-insensitive matching
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

        # Ensure the destination folder is not mistakenly nested
        if dest_folder.startswith(VID_FOLDER):
            print(f"⚠️ Skipping {file}: Preventing accidental nesting.")
            continue

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
    print(f"Sorting videos from: {VID_FOLDER}")
    move_videos()
