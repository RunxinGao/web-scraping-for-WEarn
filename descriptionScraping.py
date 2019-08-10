import description_type_1
import description_type_2
import description_type_3

def get_description(bs,array):
    length = []
    description_info = []

    description_info.append(description_type_1.get_description1(bs))
    description_info.append(description_type_2.get_description2(bs))
    description_info.append(description_type_3.get_description3(bs))

    for info in description_info:
        length.append(len(info))

    content_index = length.index(max(length))

    array.append(description_info[content_index])






