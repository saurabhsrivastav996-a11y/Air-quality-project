# Air Quality Project

A small exploratory data analysis project that uses pandas and Matplotlib to visualize nitrogen dioxide measurements from monitoring stations in Antwerp, London, and Paris.

## Data

The included `air_quality_no2.csv` file contains time-indexed station measurements. The script expects the first CSV column to contain the timestamps and the remaining columns to include `station_antwerp`, `station_london`, and `station_paris`.

## Requirements

- Python 3.9 or newer
- pandas
- Matplotlib

## Setup

Clone this repository and enter its folder:

```bash
git clone https://github.com/saurabhsrivastav996-a11y/Air-quality-project.git
cd Air-quality-project
```

Create and activate a virtual environment, then install the listed packages:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Install dependencies and run the script:

```bash
python -m pip install -r requirements.txt
python plots.py
```

The script opens separate figures for the station time series, the London-versus-Paris scatter plot, and station distributions. Close the figure windows to finish the run.

## Included example figures

- [All stations](step_1.png)
- [Paris station](step_2_Paris.png)
- [London and Paris comparison](step_3_Paris-London.png)
- [London station](step_4_London.png)
- [London DataFrame example](step_41.png)
- [Station distributions](Step_5.png)

## Attribution

This project is based on the air quality visualization project by [Natalia Tsvietukhina](https://github.com/Tsvietukhina/air-quality-viz). The original project does not include a license file, so this repository does not claim a license for the upstream code, data, or figures. Confirm reuse rights before redistributing those materials.

This repository is maintained at [saurabhsrivastav996-a11y/Air-quality-project](https://github.com/saurabhsrivastav996-a11y/Air-quality-project).
