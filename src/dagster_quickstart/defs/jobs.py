from dagster import define_asset_job

all_assets_job = define_asset_job("all_assets_job")

job_asset_job = define_asset_job("job_asset_job", selection="job_asset")

auto_job_schedule = define_asset_job("auto_job_schedules", selection="auto_job_schedule")