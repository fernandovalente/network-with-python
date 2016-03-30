from pygeocoder import Geocoder


def lat_lang():
    address = input('Address: ')
    print(Geocoder.geocode(address)[0].coordinates)


if __name__ == '__main__':
    lat_lang()
