# PRODIGY_DS_01 — Data Visualization

Prodigy InfoTech Data Science Internship Task 1.

## Objective
Create a bar chart and/or histogram showing the distribution of categorical or continuous variables.

## Dataset
`housing_data.csv` from `IamGroot786/House_Price_Prediction`. The verified source has 1,460 housing records and 81 columns. Copy the CSV into `dataset/housing_data.csv`.

## Visualizations
- `SalePrice`: 30-bin histogram.
- `HouseStyle`: frequency bar chart.

## Verified findings
- SalePrice: min 34,900; max 755,000; mean 180,921.20; median 163,000.
- The SalePrice distribution is right-skewed.
- HouseStyle counts: 1Story 726, 2Story 445, 1.5Fin 154, SLvl 65, SFoyer 37, 1.5Unf 14, 2.5Unf 11, 2.5Fin 8.

## Run
```bash
pip install -r requirements.txt
python task1.py
```

## Structure
```text
PRODIGY_DS_01/
├── dataset/
│   ├── housing_data.csv
│   └── README.md
├── images/
│   ├── sale_price_histogram.png
│   └── house_style_bar_chart.png
├── notebook/
│   └── Task_01.ipynb
├── task1.py
├── README.md
├── requirements.txt
└── .gitignore
```

The included PNGs were checked against exact aggregate values computed directly from the GitHub source CSV.
