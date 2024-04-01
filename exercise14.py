from datetime import datetime, timedelta


def get_date_list(from_date: str, to_date: str):
    start_date = datetime.fromisoformat(from_date).date()
    end_date = datetime.fromisoformat(to_date).date()
    date_list = []
    if start_date <= end_date:
        step = timedelta(days=1)
        while start_date <= end_date:
            date_list.append(start_date.strftime('%Y-%m-%d'))
            start_date += step
    else:
        step = timedelta(days=-1)
        while start_date >= end_date:
            date_list.append(start_date.strftime('%Y-%m-%d'))
            start_date += step

    return date_list


print(get_date_list("2023-06-04", "2023-06-06"))
# -> ["2023-06-04", "2023-06-05", "2023-06-06"]
print(get_date_list("2023-06-06", "2023-06-06"))
# -> ["2023-06-06"]
print(get_date_list("2023-06-08", "2023-06-06"))
# -> ["2023-06-08", "2023-06-07", "2023-06-06"]
