import check50
import check50.c

@check50.check()
def exists():
    """mystery.c exists"""
    check50.exists("mystery.c")

@check50.check(exists)
def compiles():
    """mystery.c compiles"""
    check50.c.compile("mystery.c", lcs50=True)

@check50.check(compiles)
