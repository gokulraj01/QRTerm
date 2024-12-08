import tkinter as tk
from PIL import ImageTk
from qrcode import QRCode

from . import log

# Cleanup used by button event handler and manually
# `e` is used to take the event from button, but it's never used
def cleanup(e=None):
    log.info("Stopping process. Bye!!")
    root.destroy()

def display_fullscreen_image(code: QRCode):
    global root
    log.info("Starting fullscreen display")
    root = tk.Tk()
    # Create a new window to display the QR code
    root.attributes('-fullscreen', True)

    # Convert the image to PhotoImage
    photo = ImageTk.PhotoImage(code.make_image(fill_color="black", back_color="white"))

    # Create a label to hold the image
    label = tk.Label(root, image=photo, bg="black")
    label.image = photo  # Keep a reference to avoid garbage collection
    label.pack(expand=True, fill=tk.BOTH)

    # Create an exit button
    exit_button = tk.Button(root, text="Exit", command=cleanup, width=root.winfo_vrootwidth())
    exit_button.pack(side=tk.BOTTOM)  # Add some padding for aesthetics

    # Bind the escape key to exit full screen
    root.bind("<Escape>", cleanup)
    root.mainloop()

def on_generate(code: QRCode):
    log.info("Generating QR from GUI")
    # Get the data from the text field
    data = entry.get("1.0", "end")
    if data:
        code.add_data(data)
        cleanup()
    else:
        log.warning("No data recieved from GUI")

def runGUIInput(code: QRCode):
    global entry, root
    log.info("Running in GUI Mode")

    # Create the main application window
    root = tk.Tk()
    root.title("QR Code Generator")

    # Create a text entry field
    entry = tk.Text(root, width=50)
    entry.pack(pady=10)

    # Create a button to generate the QR code
    generate_button = tk.Button(root, text="Generate QR Code", command=lambda:on_generate(code))
    generate_button.pack(pady=5)

    # Start the Tkinter main loop
    root.mainloop()