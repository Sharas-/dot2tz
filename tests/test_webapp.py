from tzcoords import tzcoords
import requests

url = "http://localhost:8080/tz"

def test_tz_lookups():
    for tzc in tzcoords:
        lat, lng, tz_name = tzc
        coord = {"lat": lat, "lng": lng}
        r = requests.get(url, params=coord, timeout=0.5)
        if r.status_code != 200:
            status = f"FAIL REQ: got {r.status_code}, {r.text}"
        else:
            if r.text == tz_name:
                status = "OK" 
            else:
                status = f"FAIL: got {r.text}"
        req_time = r.elapsed.total_seconds();
        print(f"{status} for {tzc} elapsed: {req_time}")
        yield req_time

if __name__ == "__main__":
 times = list(test_tz_lookups())
 mn, mx, av = (min(times), max(times), sum(times)/len(times))
 print(f"requests: {len(times)}, times(sec):\nmin: {mn}\nmax: {mx}\navg: {av}")



