SELECT schema_metric_table_hourly_4ba9264ca9b14f09.ad_id AS ad_id, schema_metric_table_hourly_4ba9264ca9b14f09.impressions AS impressions 
FROM schema.metric_table_hourly AS schema_metric_table_hourly_4ba9264ca9b14f09 LEFT JOIN schema.entity_table AS schema_entity_table_83a8d33392b3cf56 ON schema_metric_table_hourly_4ba9264ca9b14f09.ad_id = schema_entity_table_83a8d33392b3cf56.ad_id  
WHERE CAST(schema_entity_table_83a8d33392b3cf56.ad_name AS VARCHAR) LIKE '%%abc%%' ESCAPE '/'