import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def plot_life_expectancy_france_wide(df: pd.DataFrame):
    """
    Filters the wide-format DataFrame for 'France',
    melts it into long format,
    and plots life expectancy over time.
    """
    if df is None:
        raise AssertionError("Error: DataFrame could not be loaded.")

    if 'country' not in df.columns:
        raise AssertionError("Error: Column 'country' not found.")

    france_data = df[df['country'] == 'France'].copy()

    if france_data.empty:
        raise AssertionError("Warning: No data found for country 'France'.")

    year_cols = [col for col in france_data.columns if col != 'country']

    france_data_long = france_data.melt(
        id_vars=['country'],
        value_vars=year_cols,
        var_name='Year',
        value_name='Life Expectancy'
    )

    try:
        france_data_long['Year'] = pd.to_numeric(
            france_data_long['Year'], errors='coerce'
        ).astype('int64')
        france_data_long['Life Expectancy'] = pd.to_numeric(
            france_data_long['Life Expectancy'], errors='coerce'
        )
    except Exception as e:
        print(f"Data type conversion error: {e}")
        return

    if france_data_long.empty:
        raise AssertionError("Warning: Data for France was found.")

    plt.plot(
        france_data_long['Year'].to_numpy(),
        france_data_long['Life Expectancy'].to_numpy(),
        color='blue',
    )

    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")

    min_year = france_data_long['Year'].min()
    max_year = france_data_long['Year'].max()
    plt.xlim(min_year, max_year)

    plt.show()


def main():
    df_dataset = load("life_expectancy_years.csv")
    plot_life_expectancy_france_wide(df_dataset)


if __name__ == "__main__":
    main()
