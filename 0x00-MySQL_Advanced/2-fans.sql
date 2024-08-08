--2-fans
--bands with most fans
SELECT
	origin,
	SUM(nb_fans) AS total
FROM
	bands
GROUP BY
	origin
ORDER BY
	total DESC;
