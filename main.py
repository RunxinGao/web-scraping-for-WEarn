import json
import requests
from bs4 import BeautifulSoup
import categoryScraping
import descriptionScraping
import imageScraping
import locationScraping
import timeScraping
import titleScraping
import organizationScraping
from pandas import DataFrame

event_link = []
event_url = ""

title_list = []
image_list = []
description_list = []
time_list = []
category_list = []
location_list = []
organization_list = []

# get all urls of a single event
for i in range(1, 47):
    if i == 1:
        event_url = "https://www.eventbrite.com/d/wi--madison/all-events/"
    else:
        event_url = "https://www.eventbrite.com/d/wi--madison/all-events/?page=" + str(i)
    i += 1
    Event_html_page = requests.get(event_url)
    soup_page = BeautifulSoup(Event_html_page.text, 'lxml')
    script_page = json.loads(soup_page.find('script', type='application/ld+json').text)
    print(i-1, len(script_page))

    for j in range(len(script_page)):
        event_link.append(script_page[j]['url'])

# single scrapping for all events
for link in event_link:
    html = requests.get(link)
    soup = BeautifulSoup(html.text, 'lxml')

    # get title links
    titleScraping.get_title(soup, title_list)
    # get Image links
    imageScraping.get_image(soup, image_list)
    # get Description links
    descriptionScraping.get_description(soup, description_list)
    # get Time links
    timeScraping.get_time(soup, time_list)
    # get Category links
    categoryScraping.get_category(soup, category_list)
    # get Location List
    locationScraping.get_location(soup, location_list)
    # get Organization List
    organizationScraping.get_organization(soup, organization_list)

print("event_title: " + str(len(title_list)))
print("event_link: " + str(len(event_link)))
print("image_list: " + str(len(image_list)))
print("description_list: " + str(len(description_list)))
print("time_list: " + str(len(time_list)))
print("category_list: " + str(len(category_list)))
print("location_list: " + str(len(location_list)))
print("organization_list: " + str(len(organization_list)))

event_form = {"event_url": event_link, 'event_title': title_list,
              "event_image": image_list,
              "event_description": description_list,
              "event_time": time_list,
              "event_category": category_list,
              "event_location": location_list,
              "event_organization": organization_list}


print(len(event_form.values()))
event_data_frame = DataFrame(event_form)
print(len(event_data_frame))

image_none_index = event_data_frame[event_data_frame.event_image == "None"].index.tolist()
event_data_frame = event_data_frame.drop(index=image_none_index)

description_none_index = event_data_frame[event_data_frame.event_description == "None"].index.tolist()
event_data_frame = event_data_frame.drop(index=description_none_index)

event_csv = event_data_frame.to_csv("event_info.csv", index=None, header=True, encoding='utf-8')
