import json

def query_db(page_name):
    with open("content.json") as content:
        content_data=json.load(content)
    print(content_data[page_name]["videos"])
    return content_data.get(page_name)
query_db('page1')