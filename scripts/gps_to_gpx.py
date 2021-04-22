import numpy as np
import gpxpy.gpx
import os
# from lxml import etree as ElementTree

gps = np.load('gps.npz')
lats = gps['latitudes'].tolist()
lons = gps['longitudes'].tolist()
times = gps['times'].tolist()
altitudes = gps['altitudes'].tolist()

last_time = None

if not os.path.isdir('gps_out'):
    os.makedirs('gps_out')

# parser = ElementTree.XMLParser(recover=True)
# gpx_extension_color = ElementTree.fromstring("""<gpxx:TrackExtension xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3">
#     <gpxx:DisplayColor>Black</gpxx:DisplayColor>
#     </gpxx:TrackExtension>
# """, parser)
# print(gpx_extension_color)

gps_num = 0

# Create points:
for lat, lon, altitude, time in zip(lats, lons, altitudes, times):
    if last_time is None or (time - last_time > 0.5 and len(gpx_segment.points) > 0):
        if last_time is not None:
            print('Add new segment')
            with open('gps_out/gps_%05d.gpx' % gps_num, 'w') as f:
                f.write(gpx.to_xml())
            gps_num = gps_num + 1

        gpx = gpxpy.gpx.GPX()
        # gpx.nsmap["gpxtpx"] = "http://www.garmin.com/xmlschemas/GpxExtensions/v3"

        # Create first track in our GPX:
        gpx_track = gpxpy.gpx.GPXTrack()
        gpx.tracks.append(gpx_track)

        # Create first segment in our GPX track:
        gpx_segment = gpxpy.gpx.GPXTrackSegment()
        gpx_track.segments.append(gpx_segment)

        # print('Created GPX:', gpx.to_xml())

    gpx_point = gpxpy.gpx.GPXTrackPoint(lat, lon, altitude)
    gpx_segment.points.append(gpx_point)
    # gpx_point.extensions.append(gpx_extension_color)
    last_time = time

# print('Created GPX:', gpx.to_xml())

if len(gpx_segment.points) > 0:
    with open('gps_out/gps_%05d.gpx' % gps_num, 'w') as f:
        f.write(gpx.to_xml())
