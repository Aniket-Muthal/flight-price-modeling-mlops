"""
data_diagnostics.py
-------------------
Data Quality and Summary Utilities
----------------------------------

This module provides helper functions for exploratory data analysis (EDA),
focusing on data quality checks and feature summaries. It includes utilities
to detect duplicates, summarize unique values and datatypes, report missing
values, and generate descriptive statistics for both numerical and categorical
features.

"""

import pandas as pd
from IPython.display import display

# ---------------------------------------------------------------------------#
# ----------------------------DUPLICATE CHECK--------------------------------#
# ---------------------------------------------------------------------------#

def check_duplicates(df, return_count = False):
    """
    Check and report duplicate rows in a DataFrame.

    This function counts fully duplicated rows in the input DataFrame and
    prints a human-readable summary. Optionally, it can return the count
    of duplicate rows for programmatic use.

    PARAMETERS
    ----------
    df : pd.DataFrame
        Input DataFrame to check for duplicate rows

    return_count : bool, default = False
        Whether to return number of duplicate rows

    RETURNS
    -------
    int or None
        Count of duplicate rows if `return_count` flag is True,
        otherwise None
    """
    n_duplicates = df.duplicated().sum()

    if n_duplicates > 0:
        print(f"There are {n_duplicates} duplicate entries in the data.")
    else:
        print("There are no duplicate records in the data.")

    if return_count:
        return n_duplicates
    
# ---------------------------------------------------------------------------#
# ---------------------UNIQUE VALUE & DTYPE SUMMARY--------------------------#
# ---------------------------------------------------------------------------#

def unique_and_dtype_summary(df, return_df = False):
    """
    Displays unique values and datatypes per feature of a DataFrame.
    Optionally returns the summary DataFrame.
    
    PARAMETERS
    ----------
    df : pd.DataFrame
        Input DataFrame to check unique value & dtype summary
    
    return_df : bool, default = False
        Whether to return the summary DataFrame
    
    RETURNS
    -------
    pd.DataFrame or None
        Summary DataFrame (Unique value & dtype per feature) only if
        `return_df` is True, otherwise None
    """
    unique_count_df = (
        df
        .nunique()
        .reset_index()
        .rename(columns = {"index": "feature", 0: "unique_count"})
    )

    data_type_df = (
        df
        .dtypes
        .reset_index()
        .rename(columns = {"index": "feature", 0: "data_type"})
    )

    summary_df = pd.merge(
        left = unique_count_df,
        right = data_type_df,
        on = "feature",
        how = "inner",
    ).sort_values(by = "unique_count", ascending = False, ignore_index = True)

    display(summary_df)

    if return_df:
        return summary_df

# ---------------------------------------------------------------------------#
# -------------------------MISSING VALUES SUMMARY----------------------------#
# ---------------------------------------------------------------------------#

def check_missing_values(df, return_df = False):
    """
    Displays missing value count + percentage per column.
    Optionally returns the summary DataFrame.

    PARAMETERS
    ----------
    df : pd.DataFrame
        Input DataFrame to check missing values

    return_df : bool, default = False
        Whether to return the missing summary DataFrame

    RETURNS
    -------
    pd.DataFrame or None
        Missing summary DataFrame only if `return_df` is True,
        otherwise None    
    """
    n_rows = len(df)

    mv_df = (
        df
        .isnull()
        .sum()
        .to_frame("values")
        .assign(
            percentage = lambda x: (x["values"] * 100 / n_rows).round(2)
        )
        .query("values > 0")
        .sort_values(by = "values", ascending = False)
    )

    if mv_df.empty:
        print("There are no missing values in the data.")
    else:
        print("Missing values detected:")
        display(mv_df)

    if return_df:
        return mv_df

# ---------------------------------------------------------------------------#
# ------------------BASIC SUMMARY (DESCRIPTIVE STATS)------------------------#
# ---------------------------------------------------------------------------#

def basic_summary(df, col):
    """
    Prints descriptive statistics + unique values for a given column.

    PARAMETERS
    ----------
    df : pd.DatFrame
        Input DataFrame to derive descriptive statistics
        and unique values

    col : str
        Input feature for which descriptive statistics
        and unique values are to be derived

    RETURNS
    -------
    None
    """
    print(f"Descriptive Stats for '{col}':\n")
    print(df[col].describe())
    print("\n" + "---" * 30)
    print(f"\nUnique Values:\n")
    print(df[col].unique())
    print("\n" + "---" * 30)
    
    distribution = (
        df[col]
        .value_counts()
        .to_frame()
        .assign(
            percentage = round(df[col].value_counts(normalize = True) * 100, 2)
        )
    )
    print(f"\nDistribution of Categories:\n")
    display(distribution)

# ---------------------------------------------------------------------------#
# -----------------------------Numeric Summary-------------------------------#
# ---------------------------------------------------------------------------#
def numeric_summary(df):
    """
    This function returns summary for numerical features that includes:
        - Descriptive statistics
        - Missing value %
        - Count of unique values

    PARAMETERS
    ----------
    df : pd.DataFrame
        Input DataFrame to derive numerical summary

    RETURNS
    -------
    None
    """
    numeric_cols = df.select_dtypes(include = ["int", "float"]).columns

    summary = df[numeric_cols].describe().T
    summary["missing %"] = df[numeric_cols].isnull().mean() * 100
    summary["unique"] = df[numeric_cols].nunique()

    return summary


# ---------------------------------------------------------------------------#
# ---------------------------Categorical Summary-----------------------------#
# ---------------------------------------------------------------------------#
def categorical_summary(df):
    """
    This function returns summary for categorical features that includes:
        - Count of unique values
        - Most Frequent category
        - Missing value %

    PARAMETERS
    ----------
    df : pd.DataFrame
        Input DataFrame to derive categorical summary

    RETURNS
    -------
    None
    """
    cat_cols = df.select_dtypes(include = ["object", "category"]).columns
    summary = pd.DataFrame(index = cat_cols)

    summary["unique"] = df[cat_cols].nunique()
    summary["most_frequent"] = df[cat_cols].mode().iloc[0]
    summary["missing %"] = df[cat_cols].isnull().mean() * 100

    return summary