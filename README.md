# NYC Yellow Taxi Fare Analysis (January 2025) - Dask Edition

This project performs scalable analysis on NYC Yellow Taxi trip data using **Dask**, a parallel computing framework in Python. It demonstrates how to handle and analyze **large-scale real-world datasets** efficiently on a personal computer.

---

## 🚀 Project Objective

Analyze taxi trip data from January 2025 to:

- Join trip data with location metadata
- Clean and filter invalid entries
- Calculate **trip durations**
- Compute **average fare per pickup zone**
- Visualize the **top 10 zones** with the highest average fare

---

## 🛠️ Tech Stack

- **Python 3.12**
- **Dask**
- **Pandas**
- **Matplotlib**
- **Parquet** and **CSV** file formats

---

## 📁 Dataset Used

- `yellow_tripdata_2025-01.parquet`: Contains detailed trip-level data (pickup/dropoff times, distances, fares, etc.)
- `taxi_zone_lookup.csv`: Maps `LocationID` to actual NYC zones and boroughs.

Both datasets can be downloaded from the [NYC TLC official data portal](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page).

---

## 📂 File Structure

---

## 🔧 How to Run the Project

1. **Install dependencies**:
   ```bash
   pip install dask pandas matplotlib
Top 10 Pickup Zones by Average Fare:

Zone                          average_fare
------------------------------------------
JFK Airport                     64.27
LaGuardia Airport               45.16
Upper East Side South           38.24
Times Sq/Theatre District       36.10
...

