from io import StringIO
import PIL.Image

def encode_img(img_fn):
    with open(img_fn, "rb") as f:
        data = f.read()
        return data.encode("base64")

def decode_img(img_base64):
    decode_str = img_base64.decode("base64")
    file_like = StringIO.StringIO(decode_str)
    img = PIL.Image.open(file_like)
    # rgb_img[c, r] is the pixel values.
    rgb_img = img.convert("RGB")
    return rgb_img

print(encode_img("R (1).png"))

#
#
# import base64
#
#
# def get_base64_encoded_image(image_path):
#     with open(image_path, "rb") as img_file:
#         return base64.encodestring(img_file.read()).decode('utf-8')
# print(get_base64_encoded_image("R (1).png"))
