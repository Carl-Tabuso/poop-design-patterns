class Product:
    def __init__(self, id: str, title: str, description: str, image: str, price: float) -> None:
        self.__id = id
        self.__title = title
        self.__description = description
        self.__image = image
        self.__price = price

    def get_id(self) -> str:
        return self.__id
    
    def get_title(self) -> str:
        return self.__title
    
    def get_description(self) -> str:
        return self.__description
    
    def get_image(self) -> str:
        return self.__image
    
    def get_price(self) -> float:
        return self.__price