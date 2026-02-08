first_client_time: str = input()
server_time: str = input()
second_client_time: str = input()


def format_to_seconds(str_time: str) -> int:
    hours: int = int(str_time[:2])
    minutes: int = int(str_time[3:5])
    seconds: int = int(str_time[6:9])
    seconds_since_midnight: int = hours * 3600 + minutes * 60 + seconds
    return seconds_since_midnight


def format_to_str(int_time: int) -> str:
    seconds: int = int_time % 60
    minutes: int = (int_time // 60) % 60
    hours: int = int_time // 3600

    def zero_formated_time(timestamp: int) -> str:
        str_timestamp = str(timestamp)
        if len(str_timestamp) == 1:
            str_timestamp = "0" + str_timestamp
        return str_timestamp

    str_time = zero_formated_time(hours) + ":" + zero_formated_time(minutes) + ":" + zero_formated_time(seconds)
    return str_time


int_first_client_time: int = format_to_seconds(first_client_time)
int_second_client_time: int = format_to_seconds(second_client_time)
int_server_time: int = format_to_seconds(server_time)

if int_first_client_time > int_second_client_time:
    int_second_client_time += 24 * 3600

int_time_delay: int = (int_second_client_time - int_first_client_time + 1) // 2

int_current_client_time: int = (int_server_time + int_time_delay) % (24 * 3600)
str_current_client_time: str = format_to_str(int_current_client_time)

print(str_current_client_time)
