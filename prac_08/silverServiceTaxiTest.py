"""
CP1404/CP5632 Practical - Suggested Solution
SilverServiceTaxi class tests
"""

from prac_08.silverServiceTaxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()
