SELECT
    ride_id,
    COUNT(*) AS total_rides,
    AVG(fare) AS avg_fare,
    MAX(fare) AS max_fare
FROM rides
GROUP BY ride_id