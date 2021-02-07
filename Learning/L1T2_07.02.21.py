# По сути - списал, но разобрался. Кто молодец? Я молодец.
# Надо найти разделение строк...
print('Программа-переводчик времени из секунд в 24-х часовой формат.')
sectime = int(input("Введите время в секундах: "))
hour_in_sec = 3600
minute_in_sec = 60
hour = sectime // hour_in_sec
sec_after_hour = sectime % hour_in_sec
minute = sec_after_hour // minute_in_sec
seconds = sec_after_hour % minute_in_sec
print(hour)
print(minute)
print(seconds)
print("%02d" % hour, "%02d" % minute, "%02d" % seconds, sep=":")
