import os
import time
#Scripts
GetChannelName = r"E:\Projects\VidHandler\GetChannelName.py"
VidRenamer = r"E:\Projects\VidHandler\VidRenamer.py"
sort_videosfix = r"E:\Projects\VidHandler\sort_videos(fix).py"
CheckVid = r"E:\Projects\VidHandler\CheckVid.py"
CheckVidOpp = r"E:\Projects\VidHandler\CheckVidOpp.py"

from subprocess import call
def runpyfile():
    call(["python", GetChannelName])
    call(["python", VidRenamer])
    call(["python", CheckVidOpp])
    time.sleep(2)
    call(["python", sort_videosfix])
    time.sleep(2)
    call(["python", CheckVid])

if __name__ == "__main__":
    runpyfile()