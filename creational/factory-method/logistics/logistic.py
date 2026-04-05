from RoadLogistics import RoadLogistics
from SeaLogistics import SeaLogistics
from AirLogistics import AirLogistics

if __name__ == "__main__":
    road_logistic = RoadLogistics()
    sea_logistic = SeaLogistics()
    air_logistic = AirLogistics()

    print(road_logistic.plan_delivery())
    print(sea_logistic.plan_delivery())
    print(air_logistic.plan_delivery())