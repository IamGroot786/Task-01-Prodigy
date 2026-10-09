from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
df = pd.read_csv(BASE_DIR / "dataset" / "housing_data.csv")
required = {"SalePrice", "HouseStyle"}
missing = required.difference(df.columns)
if missing:
    raise ValueError(f"Missing required columns: {sorted(missing)}")
out = BASE_DIR / "images"
out.mkdir(exist_ok=True)

plt.figure(figsize=(10, 6))
plt.hist(df["SalePrice"].dropna(), bins=30, edgecolor="black")
plt.title("Distribution of House Sale Prices")
plt.xlabel("Sale Price"); plt.ylabel("Frequency")
plt.ticklabel_format(style="plain", axis="x")
plt.tight_layout(); plt.savefig(out / "sale_price_histogram.png", dpi=300); plt.close()

counts = df["HouseStyle"].dropna().value_counts()
plt.figure(figsize=(10, 6))
plt.bar(counts.index, counts.values)
plt.title("Distribution of House Styles")
plt.xlabel("House Style"); plt.ylabel("Number of Houses")
plt.xticks(rotation=30, ha="right")
plt.tight_layout(); plt.savefig(out / "house_style_bar_chart.png", dpi=300); plt.close()

print(f"Rows: {len(df)}")
print(f"SalePrice mean: {df['SalePrice'].mean():.2f}")
print(f"SalePrice median: {df['SalePrice'].median():.2f}")
print(counts.to_string())
