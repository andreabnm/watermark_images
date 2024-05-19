from PIL import Image


class WatermarkImage:
    def __init__(self):
        self.image_path = ''
        self.watermark_path = ''

    def watermark_image(self):
        image = Image.open(self.image_path)
        wtmk = Image.open(self.watermark_path)
        wtmk_size = (int(image.width * 0.1), int(image.height * 0.1))
        wtmk.thumbnail(wtmk_size)

        width, height = image.size
        width1, height1 = wtmk.size

        image.paste(wtmk, (width - width1, height - height1))
        image.save('./new_image.jpg')


