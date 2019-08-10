def get_category(bs, array):
    try:
        tag = bs.find("div", {"class": "g-cell g-cell-10-12 g-cell-md-12-12"}).section
    except Exception:
        category = "None"
    else:
        if tag is not None:
            category = tag.find_all("span")
            if len(category) < 7:
                category = "Other"
            else:
                category = tag.find_all("span")[7]
                category = category.text
        else:
            category = "Other"
    array.append(category)