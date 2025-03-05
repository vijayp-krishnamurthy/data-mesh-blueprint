WITH transformed AS (
    SELECT 
        id,
        name,
        price,
        TIMESTAMP_SECONDS(timestamp) AS event_time
    FROM `my_project.cleaned_table`
)
SELECT * FROM transformed;