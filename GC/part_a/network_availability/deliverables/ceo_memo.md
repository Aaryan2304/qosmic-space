MEMO TO: CEO, QOSMIC Space Technologies
FROM: Founder's Office
DATE: 19 May 2026
SUBJECT: Recommended Ground Station Locations and Expected Network Availability

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THE ASK
Where should we build our first 5 optical ground stations, and what level of network availability can we expect?

RECOMMENDATION

Place stations at these 5 locations:

1. Leh, Ladakh        — Cold desert, 300 clear days/year
2. Jodhpur, Rajasthan — Thar Desert fringe, 78% annual clear
3. Challakere, Karnataka — Existing QOSMIC site, semi-arid
4. Sriharikota, AP    — ISRO launch site, coastal but operable
5. Shillong, Meghalaya — NE India, different weather system

These five are spread from Ladakh (34°N) to Andhra (14°N) and from Rajasthan (73°E) to Meghalaya (92°E). No two stations share correlated weather patterns — distance between the closest pair (Challakere-SHAR) is 200 km, and most pairs are over 1000 km apart. This diversity is what makes the network work.

NETWORK AVAILABILITY

With 1 station (say Challakere alone, for reference):

    Annual availability: ~46%

    During monsoon (Jun-Sep): Challakere drops to ~8% clear in July.
    That's 4 months of the year where the station is essentially offline.

With all 5 stations:

    Annual availability: >99%

    Even in peak monsoon, at least one station is clear over 95% of the 
    time. When Challakere is under cloud cover, Leh and Jodhpur are 
    typically clear (they're in different climate zones).

THE LEH QUESTION

Leh is our best individual site (74% clear, 3500m elevation, low turbulence), but winter temperatures hit -20°C. This requires cold-rated optics and mount hardware, adding an estimated $15-20K per station. During Jan-Feb, Leh's availability drops to 39% clear (February), so its value is in spring-autumn when it's 80-88% clear.

COST PER STATION

    CapEx: ~$265K per station (telescope, mount, adaptive optics, 
    receiver, site prep, fiber backhaul)

    OpEx: ~$55K per station per year (maintenance, power, site lease, 
    monitoring personnel shared across 3-5 stations)

    Total 5-station deployment: ~$1.3M CapEx, ~$275K/year OpEx

SCHEDULING SIMULATION

A 30-day simulation of LEO passes (500 km altitude, 10 passes/day, 7-minute windows) assigned each pass to the clearest available station:

    Jodhpur:   39% of passes
    Leh:       35%
    Shillong:  18%
    Sriharikota: 7%
    Challakere:  1%

Zero passes went unassigned. Every pass had at least one station with >60% clear probability.

KEY ASSUMPTIONS

1. Monthly climate averages from MERRA-2 reanalysis (NASA) are representative. Actual year-to-year variation exists — expect ±5-10% availability swing.
2. Stations share 1 monitoring engineer per 3-5 stations. Adding dedicated personnel per station would increase OpEx by $20K/station.
3. Leh winter hardware can be sourced within budget. If not feasible, a replacement site in Uttarakhand or Himachal should be evaluated.
4. This analysis uses daily-average cloud data. Hourly ERA5 reanalysis (currently unavailable due to ECMWF infrastructure maintenance) would enable finer-grained scheduling.

NEXT STEPS

1. Run the same analysis with hourly ERA5 data once CDS API is back online (expected 20 May).
2. Commission a Leh winter feasibility study — source cold-rated optics and calculate actual cost premium.
3. Begin site survey for Jodhpur — check fiber backhaul availability and land lease terms.
4. Feed these availability numbers into the business model spreadsheet (Grand Challenge Part B). At 40% utilization and $10/GB, a 5-station network generates approximately $18M/year in potential revenue before cloud losses. With >99% availability, the cloud adjustment factor is negligible.