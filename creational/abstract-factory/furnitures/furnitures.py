from typing import Dict, TYPE_CHECKING

from ArtDecoFurnitureFactory import ArtDecoFurnitureFactory
from VictorianFurnitureFactory import VictorianFurnitureFactory
from ModernFurnitureFactory import ModernFurnitureFactory

if TYPE_CHECKING:
    from FurnitureFactory import FurnitureFactory

def create_furnitures(furniture_factory: FurnitureFactory) -> Dict[str, object]:
    return {
        "chair": furniture_factory.create_chair(),
        "sofa": furniture_factory.create_sofa(),
        "coffee_table": furniture_factory.create_coffee_table(),
    }

def display_furnitures(furnitures: dict) -> None:
    for key, value in furnitures.items():
        furniture = str(key).capitalize().replace("_", " ")

        print(f"{furniture}: {value}")

if __name__ == "__main__":
    art_deco_furnitures = create_furnitures(ArtDecoFurnitureFactory())
    victorian_furnitures = create_furnitures(VictorianFurnitureFactory())
    modern_furnitures = create_furnitures(ModernFurnitureFactory())

    print("\n------------------------------------------------------\n")
    print("Art Deco Furnitures:\n")
    display_furnitures(art_deco_furnitures)
    print("\n------------------------------------------------------\n")


    print("Victorian Furnitures:\n")
    display_furnitures(victorian_furnitures)
    print("\n------------------------------------------------------\n")

    print("Modern Furnitures:\n")
    display_furnitures(modern_furnitures)
    print("\n------------------------------------------------------\n")