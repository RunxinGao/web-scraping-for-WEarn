def get_time(bs, array):
    time_info = ""
    try:
        time = bs.find("time", {"data-automation": "event-details-time"})
        time = time.find_all("p")
    except Exception:
        time_info = "None"
    else:
        for info in time[0:2]:
            time_info += info.get_text()+", "
    array.append(time_info)

