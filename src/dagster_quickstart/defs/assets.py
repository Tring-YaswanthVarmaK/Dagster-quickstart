import dagster as dg


@dg.asset
def hello():
    print("Hello, Dagster!")

@dg.asset(
    deps=([hello])
)
def world():
    print("World, Dagster!")
    