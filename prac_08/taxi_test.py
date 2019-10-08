""""""

from prac_08.taxi import Taxi


def main():
    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print("name={}, current fare={}".format(taxi.name, taxi.current_fare_distance))
    taxi.start_fare()
    taxi.drive(100)
    print("name={}, current fare={}".format(taxi.name, taxi.current_fare_distance))


main()
