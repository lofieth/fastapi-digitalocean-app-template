from fastapi import Body as body


def Body(default=None):
    # add embed=True to Http Body to interpret
    # single body parameter as a JSON field by default
    return body(default, embed=True)
