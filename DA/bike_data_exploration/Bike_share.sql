WITH bike_share AS (
    SELECT dteday, season, yr, weekday, hr, rider_type, riders 
    FROM bike_share_yr_0
    UNION ALL
    SELECT dteday, season, yr, weekday, hr, rider_type, riders
    FROM bike_share_yr_1
)
SELECT 
    bs.dteday, 
    bs.season, 
    bs.yr, 
    bs.weekday, 
    bs.hr, 
    bs.rider_type, 
    bs.riders, 
    ct.price, 
    ct.COGS, 
    bs.riders * ct.price AS revenue, 
    (bs.riders * ct.price) - ct.COGS AS profit
FROM bike_share bs
LEFT JOIN cost_table ct
    ON bs.yr = ct.yr;
