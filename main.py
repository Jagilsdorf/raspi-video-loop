import os, subprocess, glob, logging; from time import sleep as s

EXTENSIONS = ["mp4", "m4v"]
current_user = os.getlogin()
base_path = f"/media/{current_user}"

logging.basicConfig(filename=f'/home/{current_user}/raspi-video-loop/main_py.log', level=logging.DEBUG)
logging.info('Script started')

os.system('amixer cset numid=3 2 && amixer set Master 100%')
os.system(f'sudo chmod 755 {base_path+"/*"}')

def start_screensaver():
    #os.system() waits for screensaver to complete before continuing. Using subprocees instead.
    subprocess.Popen(["python3", f"/home/{current_user}/raspi-video-loop/screensaver.py"])

def start_vlc(path):
    os.system(f"vlc --fullscreen --loop --no-video-title-show {path}")

def remove_old_videos():
    for ext in EXTENSIONS:
        for file_path in glob.glob(f"/home/{current_user}/raspi-video-loop/file.{ext}"):
            os.remove(file_path)

png_found = False

flash_drives = glob.glob(f"{base_path}/*/")

if flash_drives:
    logging.info(f"Detected flash drives: {flash_drives}")
    for root, dirs, files in os.walk(base_path):
        print(f"Checking in directory: {root}")  # This will show which directory is being checked
        for file in files:
            print(f"Checking file: {file}")  # This will show each file being checked
            if file.endswith('.png') and not png_found:
                print("PNG found!")  # This will indicate when a PNG is found
                png_found = True
                os.system(f"cp '{os.path.join(root, file)}' '/home/{current_user}/raspi-video-loop/logo.png'")

            if file.endswith(tuple(EXTENSIONS)):
                video_file = os.path.join(root, file)
                break

    start_screensaver()

    if video_file:
        remove_old_videos()
        new_path = f"/home/{current_user}/raspi-video-loop/file{os.path.splitext(video_file)[1]}"
        os.system(f"cp '{video_file}' '{new_path}'")
        os.system(f'umount {base_path}')
        s(2)
        start_vlc(new_path)
    else:
        # Find the newest video in the directory and play it
        list_of_files = glob.glob('/home/{}/raspi-video-loop/file.*'.format(current_user))
        latest_file = max(list_of_files, key=os.path.getctime)
        start_vlc(latest_file)

else:
    start_screensaver()
    # Find the newest video in the directory and play it
    list_of_files = glob.glob('/home/{}/raspi-video-loop/file.*'.format(current_user))
    latest_file = max(list_of_files, key=os.path.getctime)
    start_vlc(latest_file)
