import os, glob; from time import sleep as s

def set_audio_to_hdmi():
    # Detect the active HDMI outputs
    hdmi_status = os.popen("tvservice -s").read()
    
    # If HDMI is active, set audio output to HDMI
    if "HDMI" in hdmi_status and "0x120002" not in hdmi_status:
        os.system("amixer cset numid=3 2")  # Set audio output to HDMI
    else:
        os.system("amixer cset numid=3 1")  # Set audio output to Analog

set_audio_to_hdmi()


EXTENSIONS = ["mp4", "m4v"]

def start_screensaver():
    os.system(f"python3 /etc/raspi-video-loop/screensaver.py")

def start_vlc(path):
    os.system(f"vlc --fullscreen --loop --no-video-title-show {path}")

def remove_old_videos():
    for ext in EXTENSIONS:
        for file_path in glob.glob(f"/etc/raspi-video-loop/file.{ext}"):
            os.remove(file_path)

def get_latest_video():
    list_of_files = glob.glob('/etc/raspi-video-loop/file.*')
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file

base_path = f"/media/{os.getlogin()}"

flash_drive_exists = os.path.exists(base_path)

if flash_drive_exists:
    png_found = False
    video_file = ""
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.png') and not png_found:
                png_found = True
                os.system(f"cp '{os.path.join(root, file)}' '/etc/raspi-video-loop/logo.png'")
            if file.endswith(tuple(EXTENSIONS)):
                video_file = os.path.join(root, file)
                break

    start_screensaver()

    if video_file:
        remove_old_videos()
        new_path = f"/etc/raspi-video-loop/file{os.path.splitext(video_file)[1]}"
        os.system(f"cp '{video_file}' '{new_path}'")
        os.system(f'umount {base_path}')
        s(2)
        start_vlc(new_path)
    else:
        start_vlc(get_latest_video())

else:
    start_screensaver()
    start_vlc(get_latest_video())
