from typing import Union
from dataclasses import dataclass

TNumber = Union[int, float]
TCoord = Union[str, TNumber] 

@dataclass
class GeoCoord:
    """Value object to represent a valid geo coordinate."""

    @property
    def lng(self) -> float:
        return self._lng

    @property
    def lat(self) -> float:
        return self._lat

    def __init__(self, lat:TCoord, lng:TCoord):
        try:
            lat = float(lat)
            lng = float(lng)
        except (ValueError, TypeError):
            raise ValueError(f"Invalid coordinate representation: {lat} {lng}. Coords should be float numbers.")
        if (lat < -90 or lat > 90) or (lng < -180 or lng > 180):
            raise ValueError(f"Coord value out of range: {lat} {lng}. Valid range lat: [-90, 90] lng: [-180, 180]")

        self._lat = lat
        self._lng = lng




        

