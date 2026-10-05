"""One-command entry point for the complete project."""

from pathlib import Path

from src.train_evaluate import run_project


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    outcome = run_project(root)
    print(f"Prepared {outcome['rows']} monthly observations.")
    print(f"Best test model by MAE: {outcome['best_model']}")
    for row in outcome["metrics"]:
        print(
            f"{row['model']}: MAE={row['mae_m3']:.2f} m3, "
            f"RMSE={row['rmse_m3']:.2f} m3, MAPE={row['mape_percent']:.2f}%"
        )

