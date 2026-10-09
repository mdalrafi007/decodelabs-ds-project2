"""Extract the 12 chart images from an executed Kaggle notebook into ./figures/
Usage: python extract_figures.py Project2_Fraud_Detection.ipynb
Needs only the Python standard library."""
import base64, json, os, sys

NAMES = ["01_class_distribution", "02_amount_by_class", "03_time_of_day", "04_correlation",
         "05_smote_before_after", "06_smote_scatter", "07_tuning_effects", "08_confusion_matrices",
         "09_roc_pr_threshold", "10_model_comparison", "11_feature_importance", "12_business_cost"]

nb = json.load(open(sys.argv[1], encoding="utf-8"))
os.makedirs("figures", exist_ok=True)
n = 0
for cell in nb["cells"]:
    for out in cell.get("outputs", []):
        png = out.get("data", {}).get("image/png")
        if png and n < len(NAMES):
            if isinstance(png, list):
                png = "".join(png)
            with open(f"figures/{NAMES[n]}.png", "wb") as f:
                f.write(base64.b64decode(png))
            n += 1
print(f"Saved {n} figures to ./figures (expected 12)")
