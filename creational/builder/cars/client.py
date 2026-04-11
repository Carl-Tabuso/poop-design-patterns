from Director import Director
from CarBuilder import CarBuilder
from CarManualBuilder import CarManualBuilder

if __name__ == '__main__':
    # with director
    director = Director()

    car_builder = CarBuilder()
    director.make_suv(car_builder)
    suv = car_builder.get_result()

    car_builder = CarBuilder()
    director.make_sports_car(car_builder)
    sports_car = car_builder.get_result()

    print(suv)
    print("\n")
    print(sports_car)

    # without director
    car_builder = CarBuilder()
    car = (car_builder.set_seats(4)
            .set_engine('V6')
            .set_trip_computer()
            .set_gps()
            .get_result())
    
    print(car)

    print("\n")

    manual_builder = CarManualBuilder()
    manual = (manual_builder.set_seats(4)
                .set_engine('V8')
                .set_trip_computer()
                .set_gps()
                .get_result()
              )
    
    print(manual)