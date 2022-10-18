class bcolors:
    """
    ANSI escape sequences
    for colorful terminal prints
    from: https://stackoverflow.com/a/287944/13115938
    more info: https://en.wikipedia.org/wiki/ANSI_escape_code
    usage:
    >>> print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
    """

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    def template(msg, code):
        return f"{code}{msg}{bcolors.ENDC}"


def HEADER(msg):
    """
    The HEADER function is a helper function that prints the string passed to it
    in bold, underlined text. It is used by the rest of the functions in this file
    to print out section headings for easier readability of output.

    Parameters
    ----------
        msg
            Print a message to the console

    Returns
    -------

        A string that is formatted to be colored in as a header

    Doc Author
    ----------
        Trelent
    """
    return bcolors.template(msg, bcolors.HEADER)


def OKGREEN(msg):
    """
    The OKGREEN function returns a string formatted with the OKGREEN color code.



    Parameters
    ----------
        msg
            Print the message to the screen

    Returns
    -------

        A string that is printed in green

    Doc Author
    ----------
        Trelent
    """
    return bcolors.template(msg, bcolors.OKGREEN)


def OKBLUE(msg):
    """
    The OKBLUE function is a helper function that prints the given message
    in blue text.


    Parameters
    ----------
        msg
            Display the message to the user

    Returns
    -------

        The string that was passed to it, but with the text wrapped in blue

    Doc Author
    ----------
        Trelent
    """
    return bcolors.template(msg, bcolors.OKBLUE)


def WARNING(msg):
    """
    The WARNING function is a convenience function that prints the given
    message in yellow text.  This is used to indicate a warning or error to the
    user.

    Parameters
    ----------
        msg
            Print a message to the user

    Returns
    -------

        A string that has the word warning in red letters

    Doc Author
    ----------
        Trelent
    """
    return bcolors.template(msg, bcolors.WARNING)


def FAIL(msg):
    """
    The FAIL function is a convenience function that prints the given
    message in red, bold font. It is intended to be used for error messages.

    Parameters
    ----------
        msg
            Print a message to the user

    Returns
    -------

        A string in red

    Doc Author
    ----------
        Trelent
    """
    return bcolors.template(msg, bcolors.FAIL)


def BOLD(msg):
    """
    The BOLD function wraps a string in the ANSI escape sequence for bold.



    Parameters
    ----------
        msg
            Print the message to the console

    Returns
    -------

        The string passed to it with the

    Doc Author
    ----------
        Trelent
    """
    return bcolors.template(msg, bcolors.BOLD)


def UNDERLINE(msg):
    """
    The UNDERLINE function returns a string that is underlined.



    Parameters
    ----------
        msg
            Print the message that is passed to it

    Returns
    -------

        A string that has the inputted

    Doc Author
    ----------
        Trelent
    """
    return bcolors.template(msg, bcolors.UNDERLINE)


def STEP_EXPLANATION(msg, scope=None, end="\n"):
    """
    The STEP_EXPLANATION function prints a warning message in bold font.



    Parameters
    ----------
        msg
            Print out the message to the user
        scope=None
            Add a scope to describe where it is called
        end="\n"
            Set end character

    Returns
    -------

        The message in bold red text

    Doc Author
    ----------
        Trelent
    """
    print(BOLD(WARNING(f" {(scope if scope is not None else '')} --> {msg}")), end=end)
