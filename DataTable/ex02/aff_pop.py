import pandas as pd
import matplotlib.pyplot as plt

from load_csv import load


def plot_population_france_vs_belgium(df: pd.DataFrame) -> None:
    """
    displays the country information
    of Paris versus Belgique
    """
    if df is None:
        raise AssertionError(
            "Error: DataFrame could not be loaded."
        )

    if "country" not in df.columns:
        raise AssertionError("Error: Column 'country' not found.")

    countries = ["France", "Belgium"]
    data_wide = df[
        df["country"].str.lower().isin(countries)
    ].copy()

    if data_wide.empty:
        raise AssertionError(
            "Warning: No data found for specified countries."
        )

    year_cols = [col for col in data_wide.columns if col != "country"]

    data_long = data_wide.melt(
        id_vars=["country"],
        value_vars=year_cols,
        var_name="Year",
        value_name="Population",
    )

    try:
        data_long["Year"] = pd.to_numeric(data_long["Year"])

        s = data_long["Population"].astype(str).str.lower().str.strip()
        s = s.replace(
            {
                "k": "*1e3",
                "m": "*1e6",
                "b": "*1e9",
            },
            regex=True,
        )
        data_long["Population"] = pd.to_numeric(s.apply(pd.eval))

    except Exception as e:
        print(f"Data type conversion error: {e}")
        return

    data_long = data_long[data_long["Year"] <= 2050].copy()

    if data_long.empty:
        raise AssertionError(
            "Warning: No valid data found after cleaning and filtering."
        )

    color_map = {
        "france": "green",
        "belgium": "blue",
    }

    for country in countries:
        plot_data = data_long[
            data_long["country"].str.strip().str.lower() == country
        ]

        plt.plot(
            plot_data["Year"].to_numpy(),
            (plot_data["Population"] / 1_000_000).to_numpy(),
            color=color_map.get(country),
            label=country.capitalize(),
            linewidth=2,
        )

    min_year = data_long["Year"].min()

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.xlim(min_year, 2050)

    plt.legend(loc="lower right")

    plt.show()


def main() -> None:
    df_dataset = load("population_total.csv")
    plot_population_france_vs_belgium(df_dataset)


if __name__ == "__main__":
    main()
