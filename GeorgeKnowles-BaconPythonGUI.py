import tkinter as tk
from tkinter import ttk
import PIL
from PIL import Image, ImageTk
from PIL import Image, ImageFilter
root = tk.Tk()
root.title("Frame Demo")
root.config(bg="skyblue")

# Create Frame widget
frame = tk.Frame(root, width=500,height=100)
frame.pack(padx=10, pady=10)
tk.Label(frame, width=30, height=5, text="Welcome to the Image Editor", bg="lightgreen").pack(padx=10, pady=10)

root.title("Image Editor")

# Load the image using PIL (for .jpg support)
original_image = Image.open("cow.jpg")

# Create smaller versions for display
thumbnail_image = ImageTk.PhotoImage(original_image.resize((250, 400)))
display_image = ImageTk.PhotoImage(original_image.resize((300, 200)))

#main view
# Tools frame
tools_frame = tk.Frame(root, width=200, height=400, bg="skyblue")
tools_frame.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.Y)
tk.Label(tools_frame, text="Original Image", bg="skyblue").pack(padx=5, pady=5)
tk.Label(tools_frame, image=thumbnail_image).pack(padx=5, pady=5)

# Tabs for Tools and Filters
notebook = ttk.Notebook(tools_frame)
notebook.pack(expand=True, fill="both")

# Tools tab
tools_tab = tk.Frame(notebook, bg="lightblue")
tools_var = tk.StringVar(value="None")
for tool in ["Resizing", "Rotating"]:
    tk.Radiobutton(tools_tab, text=tool, variable=tools_var, value=tool, bg="lightblue").pack(anchor="w", padx=20, pady=5)
    
# Image operations (tools & filters)
def apply_action():
    edited_image = original_image.copy()

    # Tools
    if tools_var.get() == "Resizing":
        w, h = edited_image.size
        edited_image = edited_image.resize((w // 2, h // 2))
        display_image = ImageTk.PhotoImage(edited_image)
        image_label.config(image=display_image)
        image_label.image = display_image

    elif tools_var.get() == "Rotating":
        edited_image = edited_image.rotate(90, expand=True)

    # Filters
    if filters_var.get() == "Blurring":
        edited_image = edited_image.filter(ImageFilter.BLUR)

    elif filters_var.get() == "Sharpening":
        edited_image = edited_image.filter(ImageFilter.SHARPEN)

    # Update display
    new_display = ImageTk.PhotoImage(edited_image)
    image_label.config(image=new_display)
    image_label.image = new_display  # prevent garbage collection

# Filters tab
filters_tab = tk.Frame(notebook, bg="lightgreen")
filters_var = tk.StringVar(value="None")
for f in ["Blurring", "Sharpening"]:
    tk.Radiobutton(filters_tab, text=f, variable=filters_var, value=f, bg="lightgreen").pack(anchor="w", padx=20, pady=5)
notebook.add(tools_tab, text="Tools")
notebook.add(filters_tab, text="Filters")
# Apply button
tk.Button(tools_frame, text="Apply", command=apply_action).pack(pady=10)

# Image display frame
image_frame = tk.Frame(root, width=400, height=400, bg="grey")
image_frame.pack(padx=5, pady=5, side=tk.RIGHT)
tk.Label(image_frame, text="Edited Image", bg="grey", fg="white").pack(padx=5, pady=5)
image_label = tk.Label(image_frame, image=display_image)
image_label.pack(padx=5, pady=5)

# Keep references to avoid garbage collection
root.thumbnail_image = thumbnail_image
root.display_image = display_image

root.mainloop()

