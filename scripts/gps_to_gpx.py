import numpy as np
import gpxpy
import gpxpy.gpx

gps = np.load('gps.npz')
lats = gps['latitudes'].tolist()
lons = gps['longitudes'].tolist()

gpx = gpxpy.gpx.GPX()

# Create first track in our GPX:
gpx_track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(gpx_track)

# Create first segment in our GPX track:
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)

# Create points:
for lat, lon in zip(lats, lons):
    gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(lat, lon))

print('Created GPX:', gpx.to_xml())

with open('gps.gpx', 'w') as f:
    f.write(gpx.to_xml())
