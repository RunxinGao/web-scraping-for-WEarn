def get_description3(bs):
    description_info = ""
    try:
        description = bs.find("div", {"class": "structured-content-rich-text structured-content__module l-align-left l-mar-vert-6 l-sm-mar-vert-4 text-body-medium"})
        for item in description:
            for content in item.find_all("p"):
                description_info += content.get_text()
    except Exception:
        description_info = ""
    else:
        description_info = description_info

    return description_info