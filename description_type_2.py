def get_description2(bs):
    description_info = ""

    try:
        description = bs.find("div", {"data-automation": "about-this-event-sc"})
        description = description.find_all("p")
        for content in description:
            description_info += content.get_text()
    except Exception:
        description_info = "None"
    else:
        description_info = description_info

    return description_info