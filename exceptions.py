class InvalidInputError(Exception):
    """Exception raised if an invalid input is given"""
    def __str__(self) -> str:
        return "Invalid input. Please type 'y' or 'n'"