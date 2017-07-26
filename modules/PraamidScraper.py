import urllib.request, json

from modules import DateUtils


class PraamidScraper:
    def get_data(self, date, direction, start_hours, end_hours):
        with urllib.request.urlopen("https://www.praamid.ee/online/events?direction=" + direction + "&departure-date=" + date) as url:
            response = []
            data = json.loads(url.read().decode())
            items = data["items"]

            has_free = False
            for item in items:
                free_spaces = int(item["capacities"]["sv"])
                if free_spaces > 0:
                    datestring = item["dtstart"]
                    hour = int(datestring[11:13])
                    if int(start_hours) < hour < int(end_hours):
                        print(datestring, free_spaces)
                        response.append(DateUtils.get_date_from_string(datestring) + ": " + free_spaces)
                        has_free = True
            print("On vabu kohti: " + str(has_free))
            return response

