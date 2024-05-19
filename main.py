from tkinter import *
from tkinter import filedialog, font, messagebox
from watermark import WatermarkImage

window = Tk()
window.title("Watermark image")
window.minsize(width=500, height=300)
watermark_image = WatermarkImage()
arial_font32 = font.Font(family='Arial', size=32, weight=font.BOLD)
arial_font24 = font.Font(family='Arial', size=24, weight=font.BOLD)

label_image = Label(text="Select image to watermark", font=arial_font32)
label_image.grid(row=0, column=0, columnspan=3, pady=(30, 30))


def upload_image():
    watermark_image.image_path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                            filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    image_path_entry.insert(0, watermark_image.image_path)


def upload_watermark():
    watermark_image.watermark_path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                                filetypes=(
                                                                    ("jpeg files", "*.jpg"), ("all files", "*.*")))
    wtmk_path_entry.insert(0, watermark_image.watermark_path)


def create_new_image():
    if watermark_image.image_path == '':
        new_message = messagebox.Message(type='ok', title='Error', message='Please specify the image', icon='warning')
        new_message.show()
        return

    if watermark_image.watermark_path == '':
        new_message = messagebox.Message(type='ok', title='Error', message='Please specify the watermark', icon='warning')
        new_message.show()
        return

    watermark_image.watermark_image()
    new_message = messagebox.Message(type='ok', title='Created', message='New image created', icon='info')
    new_message.show()


select_image_btn = Button(text="Select image", command=upload_image)
select_image_btn.grid(row=1, column=0, columnspan=1, sticky="ew")

image_path_entry = Entry(width=70)
image_path_entry.grid(row=1, column=1, columnspan=2)

select_wtmk_btn = Button(text="Select watermark", command=upload_watermark)
select_wtmk_btn.grid(row=2, column=0, columnspan=1, sticky="ew")

wtmk_path_entry = Entry(width=70)
wtmk_path_entry.grid(row=2, column=1, columnspan=1)

create_image_btn = Button(text="Create new image", command=create_new_image, font=arial_font24, width=40)
create_image_btn.grid(row=3, column=0, columnspan=3, pady=(30, 10))

window.mainloop()
