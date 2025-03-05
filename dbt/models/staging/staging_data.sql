WITH cleaned_data AS (
    SELECT 
        id,
        name,
        timestamp,
        SAFE_CAST(price AS FLOAT64) AS price
    FROM `my_project.source_data.raw_table`
)
SELECT * FROM cleaned_data;
