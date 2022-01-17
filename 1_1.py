# seconds_day = 86400
# seconds_hour = 3600
# seconds_minute = 60
# seconds = 1


duration = int(input('Введите количество секунд: '))

day = duration // 86400
duration = duration - (day * 86400)

hour = duration // 3600
duration = duration - (hour * 3600)

minute = duration // 60
duration = duration - (minute * 60)

seconds = duration // 1
duration = duration - (seconds * 1)

print(day, 'дн.', hour, 'час.', minute, 'мин.', seconds, 'сек.')

