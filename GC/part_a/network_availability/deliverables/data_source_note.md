Note on Data Source
====================

The interview specification asked for ERA5 reanalysis cloud cover data.
The CDS (Climate Data Store) API was unavailable on 19 May 2026 due to
scheduled infrastructure maintenance (announced at 
https://forum.ecmwf.int/t/upcoming-essential-maintenance-sessions-on-data-stores-underlying-infrastructure/14954).

As a fallback, the station analysis uses MERRA-2 reanalysis data accessed
via WeatherSpark.com (which blends station data with MERRA-2 reanalysis).
The monthly clear-sky probabilities are derived from the same type of
reanalysis product as ERA5 — just a different reanalysis model.

The methodology (per-station monthly probabilities → spatial correlation
model → network availability) is data-source-agnostic and transfers
directly to ERA5 data when the CDS API is operational.

Station coordinates (used for potential future ERA5 downloads):
  Leh:        34.15°N, 77.58°E
  Jodhpur:    26.24°N, 73.02°E
  Challakere: 14.30°N, 76.50°E
  Sriharikota: 13.72°N, 80.23°E
  Shillong:    25.58°N, 91.88°E
