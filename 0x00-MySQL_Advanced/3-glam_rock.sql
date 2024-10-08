-- 3-glam_rock
--bands with most fans
SELECT
	band_name,
	CASE
		WHEN split IS NULL THEN 2022 - formed
		ELSE split - formed
	END AS longevity
FROM
	bands
WHERE
	style = 'Glam rock'
ORDER BY
	longevity DESC;
