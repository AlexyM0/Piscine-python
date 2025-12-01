import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load


def income_formatter(x, pos):
    if x >= 1_000_000:
        return f"{x / 1_000_000:.0f}M"
    if x >= 1_000:
        return f"{x / 1_000:.0f}k"
    return f"{x:.0f}"


def projection_life_income(
    df_life: pd.DataFrame,
    df_income: pd.DataFrame,
) -> None:
    if df_life is None or df_income is None:
        raise AssertionError(
            "Error: DataFrame could not be loaded."
        )
    df_life.columns = df_life.columns.str.strip()
    df_income.columns = df_income.columns.str.strip()

    year = "1900"
    country_col = "country"

    df_life_1900 = df_life[[country_col, year]].copy()
    df_income_1900 = df_income[[country_col, year]].copy()

    df_life_1900[year] = pd.to_numeric(df_life_1900[year])
    df_income_1900[year] = pd.to_numeric(df_income_1900[year])

    df_life_1900 = df_life_1900.rename(
        columns={year: "Life Expectancy"}
    )
    df_income_1900 = df_income_1900.rename(
        columns={year: "Income"}
    )

    df_merged = (
        pd.merge(
            df_life_1900,
            df_income_1900,
            on=country_col,
        )
        .dropna()
    )

    if df_merged.empty:
        raise AssertionError(
            f"Error: No common data found for countries in {year}."
        )

    ax = plt.gca()

    plt.scatter(
        df_merged["Income"],
        df_merged["Life Expectancy"],
    )

    plt.xscale("log")

    income_ticker_formatter = ticker.FuncFormatter(
        income_formatter
    )
    ax.xaxis.set_major_formatter(income_ticker_formatter)

    plt.title(year)
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")

    plt.show()


def main() -> None:
    df_data_life = load("life_expectancy_years.csv")
    df_data_income = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )
    projection_life_income(df_data_life, df_data_income)


if __name__ == "__main__":
    main()
