import json
from urllib.request import urlopen


HACKER_PATH = "https://hacker-news.firebaseio.com/v0/item/"
KIDS = "kids"
TEXT = "text"


def get_json(json_id):
	request = urlopen(f"{HACKER_PATH}{str(json_id)}.json")
	data = json.load(request)
	return data


def get_kids(json_file):
	kids_text = []
	for kid_id in json_file[KIDS]:
		kids_text.append(get_json(kid_id)[TEXT])
	return kids_text


if __name__ == "__main__":
	data = get_json(2921506)
	print(data["kids"])
	print(get_kids(data))
