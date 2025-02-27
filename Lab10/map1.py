class Map:
    """Implements a map for the game using the Singleton design pattern

    Attributes:
        _instance: Variable of type Map that contains the only instance of this class
        _initialized: Boolean variable that represents whether this class has been initialized already
        _map: A 2D list of characters that represents each tile of the map
        _revealed: A 2D list of bools that represents each tile of the map and if it has been revealed to the player
    """

    _instance = None        # Variable of type Map that contains the only instance of this class
    _initialized = False    # Boolean variable that represents whether this class has been initialized already

    def __new__(cls, *args):
        """Overwrites __new__() to only allow the creation of once instance of this class"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Initializes the class only if it hasn't already been initialized"""
        if not Map._initialized:
            file = open("map_lab10.txt", "r")

            self._map = []
            self._revealed = []

            current_line_map = []
            current_line_revealed = []

            # Reads from file and appends each character to a placeholder list
            for line in file:
                for char in line:
                    # Makes sure no '\n' characters are appended to the list
                    if char == "\n":
                        continue

                    current_line_map.append(char)
                    current_line_revealed.append(False)

                # Appends each placeholder list to their respective class attributes
                self._map.append(current_line_map)
                self._revealed.append(current_line_revealed)

                # Resets placeholder lists
                current_line_map = []
                current_line_revealed = []

            Map._initialized = True


    def __getitem__(self, index):
        """Returns the row of the map at the given index as a list (self._map[index])
           Allows user to call m[i] or m[i][j] where m is of type Map and i, j are integers.
        """
        return self._map[index]


    def __len__(self):
        """Returns the number of rows in the map."""
        return len(self._map)


    def show_map(self, loc):
        """Returns a string with a map that only shows revealed tiles and the player"""
        shown_map = ""

        for i, row in enumerate(self._map):
            for j, char in enumerate(row):
                # Prints plater
                if loc[0] == i and loc[1] == j:
                    shown_map += '*'
                    continue

                # Prints an 'x' over a non-revealed tile
                if not self._revealed[i][j]:
                    shown_map += 'x'
                    continue

                # Prints the correct letter for a revealed tile
                shown_map += char
            shown_map += '\n'
        return shown_map


    def reveal(self, loc):
        """Sets the given location in the revealed map to true.
           This allows show_map() to display the given tile.
        """
        self._revealed[loc[0]][loc[1]] = True
        return


    def remove_at_loc(self, loc):
        """Sets the given location in the map to 'n' (nothing)"""
        self._map[loc[0]][loc[1]] = 'n'
