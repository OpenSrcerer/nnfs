class Column:
    def __str__(self):
        return self._name

    def __repr__(self):
        return self._name

    def __init__(self, name):
        self._cells = []
        self._name = name

    def __len__(self):
        return self._cells.__len__()

    def __getitem__(self, item):
        return self._cells[item]

    def add_cell(self, cell):
        self._cells.append(cell)
