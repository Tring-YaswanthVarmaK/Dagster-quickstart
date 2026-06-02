from .assets import job_asset, auto_job_schedule
from .jobs import job_asset_job, auto_job_schedule
from dagster import ScheduleDefinition, DefaultScheduleStatus

job_asset_schedule = ScheduleDefinition(
    name="job_asset_schedule",
    job=job_asset_job,
    # target=[job_asset, auto_job_schedule],
    cron_schedule="* * * * *", 
    default_status= DefaultScheduleStatus.RUNNING
)


auto_job = ScheduleDefinition(
    name="auto_job_schedule",
    job=auto_job_schedule,
    cron_schedule="* * * * *",
    default_status= DefaultScheduleStatus.RUNNING
)

