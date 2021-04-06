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


def find_max(lower=1e7, upper=1e8, found_upper=False):
	if not found_upper:
		if get_json(int(upper)) is None:
			return find_max(lower, upper, True)
		return find_max(lower, upper * 2)
	else:
		if upper - lower > 1:
			new_bound = int((lower + upper) / 2)
			if get_json(new_bound) is None:
				return find_max(lower, new_bound, found_upper=True)
			return find_max(new_bound, upper, found_upper=True)
		return upper


if __name__ == "__main__":
	print(f"found: {find_max()}")
	# data = get_json(99999224)
	# print(data)
	# if data is not None:
	# 	if KIDS in data:
	# 		print(data[KIDS])
	# 		print(get_kids(data))
