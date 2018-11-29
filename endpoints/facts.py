from io import BytesIO

from PIL import Image, ImageDraw
from flask import send_file

from utils.endpoint import Endpoint
from utils.textutils import wrap


class Facts(Endpoint):
    params = ['text']

    def generate(self, avatars, text, usernames):
        base = Image.open(self.assets.get('assets/facts/facts.bmp'))
        # We need to create an image layer here for the rotation
        text_layer = Image.new('RGBA', base.size)
        font = self.assets.get_font('assets/fonts/verdana.ttf', size=25)
        canv = ImageDraw.Draw(text_layer)

        text = wrap(font, text, 400)
        canv.text((90, 600), text, font=font, fill='Black')
        text_layer = text_layer.rotate(-13, resample=Image.BICUBIC)
        base.paste(text_layer, (0, 0), text_layer)

        b = BytesIO()
        base.save(b, format='jpeg')
        b.seek(0)
        return send_file(b, mimetype='image/jpeg')


def setup(cache):
    return Facts(cache)
