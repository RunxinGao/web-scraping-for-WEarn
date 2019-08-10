def get_image(bs, array):
    image = bs.find("picture")
    if image is not None:
        image = image.get("content")
    else:
        image = "None"
    array.append(image)