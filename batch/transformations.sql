-- Create aggregated table
CREATE TABLE IF NOT EXISTS ride_summary AS
SELECT
    ride_id,
    AVG(fare) AS avg_fare,
    AVG(distance) AS avg_distance
FROM rides
GROUP BY ride_id;