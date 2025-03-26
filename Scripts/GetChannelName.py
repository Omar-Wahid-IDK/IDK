import os
import re
import requests
import html  # ✅ Import to decode HTML entities

# 📂 File Paths
VIDEO_LINKS_FILE = r"E:\Projects\VidHandler\youtube_links.txt"
CHANNELS_FILE = r"E:\Projects\VidHandler\youtube_channels.txt"

# 🔹 Function to get video title and channel name using YouTube API
def get_video_details(youtube_url):
    try:
        response = requests.get(youtube_url)
        if response.status_code != 200:
            print(f"❌ Error fetching: {youtube_url}")
            return None, None
        
        # ✅ Extract and clean the video title
        title_match = re.search(r'<title>(.*?)</title>', response.text)
        if not title_match:
            print(f"❌ Could not find title for: {youtube_url}")
            return None, None
        
        title = html.unescape(title_match.group(1))  # ✅ Convert HTML entities to normal text
        title = title.replace(" - YouTube", "").strip()

        # ✅ Extract and clean the channel name
        channel_match = re.search(r'ownerChannelName":"(.*?)"', response.text)
        if not channel_match:
            print(f"❌ Could not find channel name for: {youtube_url}")
            return None, None
        
        channel_name = html.unescape(channel_match.group(1))  # ✅ Convert HTML entities to normal text
        return title, channel_name

    except Exception as e:
        print(f"❌ ERROR: {e}")
        return None, None

# 🔹 Function to process links and save in the correct format
def process_video_links():
    if not os.path.exists(VIDEO_LINKS_FILE):
        print(f"❌ ERROR: {VIDEO_LINKS_FILE} not found!")
        return
    
    with open(VIDEO_LINKS_FILE, "r", encoding="utf-8") as f:
        video_links = [line.strip() for line in f if line.strip()]

    if not video_links:
        print("⚠ No video links found.")
        return
    
    with open(CHANNELS_FILE, "a", encoding="utf-8") as f:
        for link in video_links:
            title, channel = get_video_details(link)
            if title and channel:
                formatted_entry = f"{title} | {channel}"
                f.write(formatted_entry + "\n")
                print(f"✅ Saved: {formatted_entry}")
            else:
                print(f"⚠ Skipping: {link}")

    # Clear the youtube_links.txt file after processing
    open(VIDEO_LINKS_FILE, "w").close()
    print("🧹 Cleaned up youtube_links.txt!")

# 🔹 Run the script
if __name__ == "__main__":
    process_video_links()
