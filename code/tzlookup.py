from tzwhere import tzwhere
from geocoord import GeoCoord

tz = tzwhere.tzwhere(forceTZ=True)

def findTZ(gcoord: GeoCoord) -> str:
    """Finds timezone 'under' provided geo coordinate.

    Args:
        geo coordinate

    Returns:
        Timezone name found or 'uninhabited'

    Raises: 
        ValueError if coordinate is invalid 
    """
    try:
        return tz.tzNameAt(latitude=gcoord.lat, longitude=gcoord.lng, forceTZ=True)
    except KeyError:
        raise ValueError("Invalid coordinate") 



