import dagster as dg

from dagster import asset


@asset
def hello():
    print("Hello, Dagster!")

@asset(
    deps=([hello])
)
def world():
    print("World, Dagster!")


@asset
def job_asset():
    print("This is a job asset.")
    

@asset
def auto_job_schedule():
    print("This asset is scheduled to run every minute.")