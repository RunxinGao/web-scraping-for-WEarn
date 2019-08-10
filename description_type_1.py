def get_description1(bs):
    description_info = ""
    try:
        description = bs.find("div", {"data-automation": "listing-event-description"})
        for content in description.find_all("p"):
            description_info += content.get_text()
    except Exception:
        description_info = "None"
    else:
        description_info = description_info

    return description_info
