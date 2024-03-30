import tkinter as tk
from gui.imageSelector import ImageSelectorApp

def main():
    root = tk.Tk()
    root.geometry("800x550")  # Set initial window size
    root.title("PixCraft | Meqdad Darwish")

    ImageSelectorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    ImageSelectorApp.clean_detection_outputs()

