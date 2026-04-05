from Contractor import Contractor
from RegularHouseBuilder import RegularHouseBuilder
from SmallCastleBuilder import SmallCastleBuilder

if __name__ == "__main__":
    print("Regular house built by a contractor:")
    regular_house_contractor = Contractor()
    regular_house_contractor.set_builder(RegularHouseBuilder())
    print(regular_house_contractor.make_regular_house())

    print("\n")

    print("Small castle built by a contractor:")    
    small_castle_contractor = Contractor()
    small_castle_contractor.set_builder(SmallCastleBuilder())
    print(small_castle_contractor.make_small_castle())

    print("\n")

    print("Regular house built manually:")
    regular_house_builder = RegularHouseBuilder()
    regular_house_builder.build_walls()
    regular_house_builder.build_doors()
    regular_house_builder.build_roof()
    print(regular_house_builder.get_result())

    print("\n")    

    print("Small castle built manually:")
    small_castle_builder = SmallCastleBuilder()
    small_castle_builder.build_walls()
    small_castle_builder.build_doors()
    small_castle_builder.build_roof()
    small_castle_builder.build_windows()
    small_castle_builder.build_garage()
    print(small_castle_builder.get_result())