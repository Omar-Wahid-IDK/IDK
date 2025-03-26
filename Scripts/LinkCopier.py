import pyperclip
import time
import os

FILE_NAME = r"E:\Projects\VidHandler\youtube_links.txt"  # Set correct path

# Ensure the directory exists
os.makedirs(os.path.dirname(FILE_NAME), exist_ok=True)

# Ensure the file exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        pass

print(f"Saving to: {os.path.abspath(FILE_NAME)}")  # Debugging line

def get_saved_links():
    """Read saved links from the file to avoid duplicates."""
    with open(FILE_NAME, "r") as f:
        return set(f.read().splitlines())

def save_link(link):
    """Save the new YouTube link if not already in the file."""
    saved_links = get_saved_links()
    
    if link not in saved_links:
        with open(FILE_NAME, "a") as f:
            f.write(link + "\n")
        print(f"Added: {link}")  # Debugging message
    else:
        print(f"Already exists: {link}")

def is_youtube_link(text):
    """Check if the copied text is a YouTube link."""
    return "youtube.com/watch?v=" in text or "youtu.be/" in text

def monitor_clipboard():
    """Monitor clipboard for YouTube links and exit after 5 seconds of inactivity."""
    last_clipboard_content = ""
    last_activity_time = time.time()
    
    while True:
        clipboard_content = pyperclip.paste()
        
        if clipboard_content != last_clipboard_content and is_youtube_link(clipboard_content):
            save_link(clipboard_content)
            last_clipboard_content = clipboard_content
            last_activity_time = time.time()  # Reset inactivity timer
        
        if time.time() - last_activity_time > 5:
            print("No activity detected for 5 seconds. Exiting...")
            break
        
        time.sleep(1)  # Check clipboard every second

if __name__ == "__main__":
    print("Monitoring clipboard for YouTube links... (Will exit after 5 seconds of inactivity)")
    try:
        monitor_clipboard()
    except KeyboardInterrupt:
        print("\nStopped.")