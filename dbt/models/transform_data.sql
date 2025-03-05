WITH raw_data AS (
    SELECT * FROM `my-gcp-project.processed_data.cleaned_table`
)

SELECT
    *,
    CURRENT_TIMESTAMP() AS transformed_at
FROM raw_data
