import falcon
import tzlookup
from geocoord import GeoCoord

class TzLookupResource(object):
    key_lat, key_lng = ('lat', 'lng')

    def on_get(self, req, resp):
        coord = (req.params.get(self.key_lat), req.params.get(self.key_lng))
        if not all(coord):
            raise falcon.HTTPBadRequest("lat and lng parameters required for timezone lookup")
        try:
            resp.body = tzlookup.findTZ(GeoCoord(*coord))
        except ValueError as e:
            raise falcon.HTTPBadRequest(str(e))
        resp.status = falcon.HTTP_200

app = falcon.API(media_type="text/plain;charset=UTF-8")
app.add_route("/tz", TzLookupResource())


