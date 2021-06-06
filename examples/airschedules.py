import asyncio

from flyline import FlylineClient


async def main():
    async with FlylineClient("test_904c384cb63468da5a6a4b20b4b353e45b142098") as client:
        # aircrafts
        aircrafts = await client.get_aircrafts()
        iata_code = aircrafts.data[0].iata_code
        aircraft = await client.get_aircraft(iata_code=iata_code)
        print("Aircraft".center(100, "="))
        print(aircrafts)
        print(aircraft)

        # airlines
        airlines = await client.get_airlines()
        iata_code = airlines.data[0].iata_code
        airline = await client.get_airline(iata_code=iata_code)
        print("Airline".center(100, "="))
        print(airlines)
        print(airline)

        # airport
        airports = await client.get_airports()
        iata_code = airports.data[0].iata_code
        airport = await client.get_airport(iata_code=iata_code)
        print("Airline".center(100, "="))
        print(airports)
        print(airport)

        # City
        cities = await client.get_cities()
        iata_code = cities.data[0].iata_code
        city = await client.get_city(iata_code=iata_code)
        city_airports = await client.get_airports_by_city(city_iata_code=iata_code)
        print("City".center(100, "="))
        print(cities)
        print(city)
        print(city_airports)

        # SeatTypes
        seat_types = await client.get_seat_types()
        print("seat_types".center(100, "="))
        print(seat_types.data)

        # Seat Layout
        seat_layouts = await client.get_seat_layouts()
        print("seat_layouts".center(100, "="))
        print(seat_layouts.data)

        # Foods
        foods = await client.get_foods()
        print("foods".center(100, "="))
        print(foods)

        # Beverages
        beverages = await client.get_beverages()
        print("beverages".center(100, "="))
        print(beverages)

        # Entertainments
        entertainments = await client.get_entertainments()
        print("entertainments".center(100, "="))
        print(entertainments)

        # wifis
        wifis = await client.get_wifis()
        print("wifis".center(100, "="))
        print(wifis)

        # Powers
        powers = await client.get_powers()
        print("powers".center(100, "="))
        print(powers)

        cabin_class_mapping_list = await client.get_cabin_class_mapping(carrier="AA", cabin_class="economy")
        print(cabin_class_mapping_list)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
