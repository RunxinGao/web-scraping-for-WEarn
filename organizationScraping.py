def get_organization(bs, array):
    try:
        organization = bs.find("a", {"href": "#listing-organizer"}).get_text()
    except Exception:
        organization = "None"
    else:
        organization = organization.strip().strip("by")
    array.append(organization)