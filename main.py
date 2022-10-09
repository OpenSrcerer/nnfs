import fileinput as fi

from classes.table import Table

print("""
-----------------------------------------------------------------
Hello, this is the beginning of my program! Currently testing table making.
-----------------------------------------------------------------
""")


def load_table():
    with fi.input(files=['./res/partA_input_data.csv']) as f:
        table = Table(f)

    table.sort_by_column(1)
    print(table)


load_table()
