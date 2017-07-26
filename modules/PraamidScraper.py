import json
import urllib.request


class PraamidScraper:
    def get_data(self, date, direction, start_hours, end_hours):
        with urllib.request.urlopen("https://www.praamid.ee/online/events?direction=" + direction + "&departure-date=" + date) as url:
            response = []
            data = json.loads(url.read().decode())
            items = data["items"]

            for item in items:
                free_spaces = int(item["capacities"]["sv"])
                if free_spaces > 0:
                    datestring = item["dtstart"]
                    hour = int(datestring[11:13])
                    if int(start_hours) < hour < int(end_hours):
                        response.append(datestring[11:16] + ": " + str(free_spaces))
            return response

    def parse_datestring_to_readable(self, string):
        return string[0:10] + " " + string[11:16]

