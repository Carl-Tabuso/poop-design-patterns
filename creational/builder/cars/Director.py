from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Builder import Builder

class Director:
    def make_suv(self, builder: Builder) -> None:
        (builder.reset()
            .set_seats(5)
            .set_engine('V8')
        )

    def make_sports_car(self, builder: Builder) -> None:
        (builder.reset()
            .set_seats(2)
            .set_engine('SportsCarEngine')
            .set_trip_computer()
            .set_gps()
        )
