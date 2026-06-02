from pathlib import Path

from dagster import Definitions, definitions, load_from_defs_folder
# from .jobs import all_assets_job, job_asset_job
# from .defs.assets import hello, world, job_asset


# Needs to import all assets
# defs = Definitions(
#     assets=[hello, world, job_asset],
#     jobs=[all_assets_job, job_asset_job]
# )

# No need to import but need to merge the loaded definitions with the explicit job definitions
# defs = Definitions.merge(
#     load_from_defs_folder(path_within_project=Path(__file__).parent),
#     Definitions(jobs=[all_assets_job, job_asset_job])
# )

# Loads job and assets automatically as long as they are in defs folder
@definitions
def defs():
    return load_from_defs_folder(path_within_project=Path(__file__).parent)
