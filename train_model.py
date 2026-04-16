from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_DIR / "data" / "sample" / "telecom_customers.csv"
OUTPUT_DIR = PROJECT_DIR / "outputs"


def build_pipeline(model):
    numeric_features = [
        "senior_citizen",
        "tenure_months",
        "monthly_charges",
        "total_charges",
        "support_tickets",
        "late_payments",
    ]
    categorical_features = ["gender", "contract_type", "payment_method", "internet_service"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_features),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ]
    )

    return Pipeline(steps=[("preprocessor", preprocessor), ("model", model)])


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    (OUTPUT_DIR / "models").mkdir(exist_ok=True)

    df = pd.read_csv(DATA_PATH)
    X = df.drop(columns=["customer_id", "churn"])
    y = df["churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=42, stratify=y
    )

    candidates = {
        "logistic_regression": LogisticRegression(max_iter=1000, class_weight="balanced"),
        "random_forest": RandomForestClassifier(
            n_estimators=250,
            max_depth=6,
            min_samples_leaf=2,
            random_state=42,
            class_weight="balanced",
        ),
    }

    results = []
    best_name = None
    best_auc = -1
    best_pipeline = None

    for name, model in candidates.items():
        pipeline = build_pipeline(model)
        pipeline.fit(X_train, y_train)
        probabilities = pipeline.predict_proba(X_test)[:, 1]
        predictions = pipeline.predict(X_test)
        auc = roc_auc_score(y_test, probabilities)
        results.append({"model": name, "roc_auc": round(auc, 4)})
        print(f"\n{name} ROC-AUC: {auc:.4f}")
        print(classification_report(y_test, predictions))

        if auc > best_auc:
            best_auc = auc
            best_name = name
            best_pipeline = pipeline

    scored = df.copy()
    scored["churn_probability"] = best_pipeline.predict_proba(X)[:, 1]
    scored["risk_segment"] = pd.cut(
        scored["churn_probability"],
        bins=[0, 0.35, 0.65, 1],
        labels=["Low", "Medium", "High"],
        include_lowest=True,
    )

    pd.DataFrame(results).to_csv(OUTPUT_DIR / "model_comparison.csv", index=False)
    scored.to_csv(OUTPUT_DIR / "customer_churn_scores.csv", index=False)
    joblib.dump(best_pipeline, OUTPUT_DIR / "models" / f"{best_name}_pipeline.joblib")

    print(f"\nBest model: {best_name} with ROC-AUC {best_auc:.4f}")


if __name__ == "__main__":
    main()

