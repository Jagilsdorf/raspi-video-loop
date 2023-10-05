import os
from tkinter import Tk, Canvas
from PIL import Image, ImageTk, ImageDraw

def set_wallpaper_with_logo():
    # Get screen size
    screen_size = (1920, 1080)  # Adjust this if you have a different resolution

    # Open the logo image
    logo_path = f"/home/{os.getlogin()}/raspi-video-loop/logo.png"
    logo = Image.open(logo_path)

    # Calculate position to center the logo
    x_pos = (screen_size[0] - logo.width) // 2
    y_pos = (screen_size[1] - logo.height) // 2

    # Create a white background image
    background = Image.new('RGB', screen_size, color='white')

    # Paste the logo onto the white background
    background.paste(logo, (x_pos, y_pos), logo)

    # Save the new image (temporary file)
    tmp_wallpaper = "/tmp/wallpaper.png"
    background.save(tmp_wallpaper)

    # Set the wallpaper using pcmanfm
    os.system(f'pcmanfm --set-wallpaper {tmp_wallpaper}')

class DVDEmulator:
    def __init__(self, root, image_path):
        self.root = root
        self.canvas = Canvas(self.root, bg="white")
        self.canvas.pack(fill="both", expand=True)

        original_image = Image.open(image_path)
        if original_image.mode != "RGBA": original_image = original_image.convert("RGBA")

        larger_dimension = max(original_image.width, original_image.height)
        scale_factor = 450.0 / larger_dimension

        new_image = original_image.resize((int(original_image.width * scale_factor), int(original_image.height * scale_factor)))
        if new_image.mode != "RGBA": new_image = new_image.convert("RGBA")

        frame_size = (int(new_image.width * 1.01), int(new_image.height * 1.01))
        frame = Image.new("RGBA", frame_size)

        frame.paste(new_image, (int((frame_size[0] - new_image.width) / 2), int((frame_size[1] - new_image.height) / 2)), new_image)

        self.image = ImageTk.PhotoImage(frame)
        self.width = self.canvas.winfo_screenwidth()
        self.height = self.canvas.winfo_screenheight()

        self.image_label = self.canvas.create_image(self.width / 2, self.height / 2, image=self.image)
        self.vx = 1
        self.vy = 1
        self.animate()

        self.root.bind("<Escape>", lambda event: root.quit())

    def animate(self):
        x, y = self.canvas.coords(self.image_label)
        img_width = self.image.width()
        img_height = self.image.height()

        if x + img_width / 2 >= self.width or x - img_width / 2 <= 0:
            self.vx = -self.vx
        if y + img_height / 2 >= self.height or y - img_height / 2 <= 0:
            self.vy = -self.vy

        self.canvas.move(self.image_label, self.vx, self.vy)
        self.root.after(10, self.animate)

if __name__ == "__main__":
    logo_path = f"/home/{os.getlogin()}/raspi-video-loop/logo.png"
    set_wallpaper_with_logo()
    root = Tk()
    root.attributes("-fullscreen", True)
    emulator = DVDEmulator(root, logo_path)
    root.mainloop()