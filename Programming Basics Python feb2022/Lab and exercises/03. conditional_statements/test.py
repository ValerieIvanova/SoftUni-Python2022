import phonenumbers

from phonenumbers import geocoder, timezone, carrier

number = '+359895309558'
ch_number = phonenumbers.parse(number)

time_zone = timezone.time_zones_for_number(ch_number)
print(time_zone)

ch_number = phonenumbers.parse(number, 'CH')
print(geocoder.description_for_number(ch_number, 'en'))

ch_number = phonenumbers.parse(number, 'R0')
print(carrier.name_for_number(ch_number, 'en'))