
# 📈  Basic Data Visualization with Pandas and Matplotlib

## Project Overview

This project serves as a foundational portfolio piece demonstrating core data analysis and visualization skills using Python's **Pandas** and **Matplotlib**. The goal is to load real-world time-series air quality data and generate various plots—including **line plots**, **scatter plots**, and **box plots**—to explore trends, distributions, and relationships between data from different European monitoring stations.


## 📊 Dataset Description

* **File Name:** `air_quality_no2.csv`
* **Description:** The dataset contains hourly measurements of Nitrogen Dioxide concentration collected from various air quality monitoring stations across Europe.
* **Key Columns:**
    * `datetime`: The time index for the measurements.
    * `station_paris`: Nitrogen Dioxide concentration at the Paris station.
    * `station_london`: Nitrogen Dioxide concentration at the London station.
    * `station_antwerp`: Nitrogen Dioxide concentration at the Antwerp station.

## 🛠️ Technologies Used

| Technology | Purpose |
| :--- | :--- |
| **Python** | Primary programming language. |
| **Pandas** | Data loading, manipulation, time-series handling, and high-level plotting interface. |
| **Matplotlib** | Underlying library used by Pandas for rendering the plots. |

---

## 💻 Installation and Execution

Follow these steps to set up and run the visualization script locally.

###  Prerequisites

```bash
python --version  # Python 3.7 or higher required
```

###  Installation (Cloning the Repository)

Clone this repository to your local machine:

```bash
git clone [https://github.com/Tsvietukhina/air-quality-viz.git](https://github.com/Tsvietukhina/air-quality-viz.gitt)
cd air-quality-viz
```

###  Install Dependencies

```bash
# Create and activate a virtual environment
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On Linux/macOS
source venv/bin/activate

# Install the necessary libraries
pip install -r requirements.txt
```

### requirements.txt contents:
```
pandas>=1.3.0
matplotlib>=3.3.0
```

## 📁 Project Structure

### The repository is organized as follows:
```
├── air_quality_no2.csv      # The raw data file
├── plots.py                 # Python script containing visualization code
├── README.md                # Project description and guide
└── requirements.txt         # List of necessary Python libraries
```

### 5. Run the Script
Execute the Python script to generate all the visualizations. A single plot window containing all the graphs will appear.
```bash
python plots.py
```
#### Step 1
![Step 1](https://github.com/Tsvietukhina/air-quality-viz/blob/main/step_1.png)
#### Step 2
![Step 2](https://github.com/Tsvietukhina/air-quality-viz/blob/main/step_2_Paris.png)
#### Step 3
![Step 3](https://github.com/Tsvietukhina/air-quality-viz/blob/main/step_3_Paris-London.png)
#### Step 4
![Step 4](https://github.com/Tsvietukhina/air-quality-viz/blob/main/step_41.png)
#### Step 5
![Step 5](https://github.com/Tsvietukhina/air-quality-viz/blob/main/Step_5.png)

## 🔍 Key Findings (Visualization Insights)
The analysis performed in plots.py generated several key visual insights:

- Time-Series Trends (Line Plots): A quick visual check of the line plots reveals the fluctuating, periodic nature of Nitrogen Dioxide levels, likely corresponding to daily traffic and weather patterns. The London and Paris stations show comparable overall magnitude, though specific peak times may differ.

- Correlation (Scatter Plot): The scatter plot comparing station_london vs. station_paris shows a weak to moderate positive correlation (α=0.5 transparency is used), suggesting that while their Nitrogen Dioxide levels are not strongly linked, higher pollution in one city is generally associated with slightly higher pollution in the other during the measurement period.

### Distribution (Box Plot): The box plots  provide a statistical summary:

- Antwerp generally shows the lowest median Nitrogen Dioxide level (the line inside the box).

- Paris and London have similar medians and interquartile ranges (the box size).

- All stations display outliers (individual dots) indicating isolated periods of very high Nitrogen Dioxide concentration.

## 📊 Code Breakdown

### plots.py

**Key Components:**
The plots.py script focuses on Exploratory Data Analysis (EDA) and visualization of the air quality dataset using Pandas' built-in plotting capabilities, which are powered by Matplotlib.

|Component           |Code Sample                                                      |Description                                                                                                                                                                                        |
|--------------------|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Data Import         |pd.read_csv('air_quality_no2.csv', index_col=0, parse_dates=True)|Reads the CSV file, setting the first column as the DateTime index and automatically parsing it as dates for proper time-series plotting.                                                          |
|Quick Overview      |air_quality.plot()                                               |Generates a simple line plot of all columns in the DataFrame. This is the fastest way to check the raw trend and scale of all data points.                                                         |
|Targeted Series Plot|air_quality["station_paris"].plot()                              |Isolates a single column (time series data for Paris) and plots its values over time.                                                                                                              |
|Relationship Check  |air_quality.plot.scatter(x="station_london", y="station_paris")  |Creates a scatter plot to visually inspect the correlation between air quality values in London and Paris. The alpha=0.5 makes the points semi-transparent to reveal areas of high density.        |
|Statistical Summary |air_quality.plot.box()                                           |Generates box plots (or box-and-whisker plots) for all stations. This provides a quick graphical representation of the median, quartiles, and range of the air quality indices for easy comparison.|
|Display Final Plot  |plt.show()                                                       |Opens all generated Matplotlib figures in a separate window, making them available for viewing and interaction.                                                                                    |

## 👨‍💻 Author

**Your Name**
- GitHub: https://github.com/Tsvietukhina
- LinkedIn: https://www.linkedin.com/in/natalia-tsvietukhina/
- Email: nataliatsvietukhina@gmail.com

## 🙏 Acknowledgments

- European Environment Agency (EEA) / AirBase: For providing the foundational air quality measurement data.
- Open Data Portal of the respective cities (Paris, London, etc.): For curating and publishing the localized Nitrogen Dioxide concentration readings.
- Pandas & Matplotlib Teams: For the powerful Python libraries essential for data manipulation and visualization.
- Open-source community

## 📞 Contact

For questions, suggestions, or feedback:
- Open an issue on GitHub
- Email me directly
- Connect on LinkedIn

## 📚 References

- [Matplotlib](https://matplotlib.org/)
- [Python](https://www.python.org/)
- [Confusion Matrix Guide](https://pandas.pydata.org/docs/user_guide/10min.html)

---

**Project Status**: ✅ Complete and Ready for Use

**Last Updated**: March 2025

**Version**: 1.0.0
