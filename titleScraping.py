def get_title(bs, array):
    try:
        title = bs.find("h1", {"data-automation": "listing-title"}).get_text()
    except Exception:
        title = "None"
    else:
        title = title
    array.append(title)