def get_location(bs, array):
    try:
        location = bs.find_all("div", {"class": "event-details__data"})
        content = location[len(location) - 1].find_all("p")
        if len(content) < 2:
            content = location[len(location) - 2].find_all("p")
        location_info = ""
    except Exception:
        location_info = "None"
    else:
        for i in range(len(content) - 1):
            location_info += str(content[i].text.strip(" ")) + " , "

    array.append(location_info)