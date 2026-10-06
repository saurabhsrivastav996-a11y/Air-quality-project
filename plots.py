from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


DATA_FILE = Path(__file__).with_name("air_quality_no2.csv")


def main():
    air_quality = pd.read_csv(DATA_FILE, index_col=0, parse_dates=True)

    # Quick visual check of all station measurements.
    air_quality.plot()

    # Inspect individual stations and compare London with Paris.
    air_quality["station_paris"].plot()
    air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
    air_quality["station_london"].plot()

    # Demonstrate plotting the London column as a one-column DataFrame.
    air_quality[["station_london"]].plot()

    # Summarize each station's distribution once.
    air_quality.plot.box()

    plt.show()


if __name__ == "__main__":
    main()
