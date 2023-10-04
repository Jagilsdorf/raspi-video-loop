# raspi-video-loop
## Introduction
This project aims to provide a seamless and effortless way to play videos in a loop on a Raspberry Pi, ideal for trade show setups or any scenario where continuous video playback is required. With an emphasis on security, and optimized for speed and reliability, this tool is designed with Sales teams in mind.

## Usage
Once everything is set up:

- Connect a USB flash drive containing your video files (with extensions .mp4 or .m4v) and optionally a logo in .png format, then start the system.
- **On boot**, the system will automatically detect the flash drive, update the screensaver with the logo, and play the most recent video in a loop.
- You can use `Alt + F4` to quit both the screensaver and VLC. This setup makes it so that that raspi can still be used for something else. Hopefully, someone will make a fork of this for setup with a Raspbian LITE and possibly use a RasPi Zero, potentially powering it from te USB port of a TV.

## Recommended Hardware
**Raspberry Pi**: It's highly recommended to use Raspberry Pi 4B or later versions. The increased performance of these newer versions ensures smooth playback and faster load times.
**Case**: Argon One v2 case for the RasPi 4B is recommended. This case offers optimal cooling solutions and adds aesthetic appeal.
**MicroSD Card**: A high-speed MicroSD card with fast read/write capabilities is crucial. For optimal performance, consider using cards such as the ImageMate PRO 32GB, which boasts a speed of 200MB/s read and 90MB/s write. Ensure that your selected card has a good track record of reliability.
## Installation and Setup
1. **Operating System**: Flash **Raspbian 64bit** onto your MicroSD card. As of the current release, this setup isn't compatible with Raspbian LITE.
1. **Connectivity**: It's strongly recommended to **disable WiFi**. Given this project's primary use at trade shows, it's essential to prevent unauthorized access. Always use an Ethernet connection for added security and consistent speed.
1. **Case Installation**: If you're using the Argon One v2 case or any other case that requires software installation to use additional features like fan control or power buttons, ensure that you install the necessary software. For the Argon One v2 case, run:
`curl https://download.argon40.com/argon1.sh | bash`
1. **Raspi Configuration**: Use `sudo raspi-config` to make necessary configurations:
- Adjust the audio output settings to use HDMI, if necessary.
1. **Install This Repository**: To get the project up and running, execute the following command:
`curl https://raw.githubusercontent.com/Jagilsdorf/raspi-video-loop/main/setup.sh | bash`

## Logic Behind Main.py
```
    +----------------------------------+
    |           Start main.py          |
    +----------------------------------+
                    |
                    |
                    v
    +----------------------------------+
    |      Check if flash drive        |__________________________
    |            exists                |                          |
    +------------------+---------------+                          |
        |                                                         |
        | Yes                                                     | No
        v                                                         v
    +------------------+----------------+                         |    
    |    Check for PNG                  |                         |
    |    on flashdrive                  |                         |
    +------------------+----------------+                         |
        |                       |                                 v 
        | Yes, PNG found        | No, PNG                         |
        v                       | not found                       |
    +-------------------+       |                                 |
    |     Copy PNG      |       |                                 |
    |  Rename logo.png  |       |                                 v
    |  Set as wallpaper |       |                                 |
    +---------+---------+       |                                 |
        |                       |                                 |
        |                       |                                 |
        v                       v                                 v
    +------------------+----------------+      +------------------+----------------+
    |       Start screensaver.py        |      |       Start screensaver.py        |
    +------------------+----------------+      +------------------+----------------+
                      |                                           |
                      v                                           v
    +------------------+----------------+                         |
    | Check for video files on          |                         |
    | flashdrive                        |                         |
    +------------------+----------------+                         |
        |                       |                                 v 
        | Yes, video found      | No, video                       |  
        v                       | not found                       | 
    +-------------------+       |                                 |
    |    Copy video     |       |                                 |
    |  Rename file.ext  |       |                                 v
    +---------+---------+       |                                 |
        |                       |                                 |
        |                       |                                 |
        v                       v                                 v
    +---------------------------+----------------+---------------------------+
    |                           Start VLC based on                           |
    |                               Newest file                              |
    +---------------------------+----------------+---------------------------+

```

## Conclusion

This tool simplifies the process of continuously looping videos on a Raspberry Pi. With a focus on security, stability, and ease of use, it's the perfect solution for Sales teams looking to showcase their content at trade shows. Remember to always keep your Raspberry Pi software and this repository updated to ensure you're benefiting from the latest features and security updates. I was bored at work and this was fun, so I hope it helps!
