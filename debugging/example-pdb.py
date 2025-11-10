# algorithm sieve of eratosthenes
"""
DEBUGGING med pdb.

Python har sit eget debugging-bliotek pdb som kan bruges til fejlfinding
eller bare til at forstå hvordan noget kode virker.

I koden indsættes denne linje:

import pdb; pdb.set_trace()

eller bare

breakpoint()

fra Python 3.9.

Eksekveringen vil da blive afbrudt og man får en kommandoprompt til rådighed.

Når breakpointet rammes, har man følgende muligheder i pdb.

Command	Description
p	Print the value of an expression.
pp	Pretty-print the value of an expression.
n	Continue execution until the next line in the current function is reached or it returns.
s	Execute the current line and stop at the first possible occasion (either in a function that is called or in the current function).
c	Continue execution and only stop when a breakpoint is encountered.
unt	Continue execution until the line with a number greater than the current one is reached. With a line number argument, continue execution until a line with a number greater or equal to that is reached.
l	List source code for the current file. Without arguments, list 11 lines around the current line or continue the previous listing.
ll	List the whole source code for the current function or frame.
b	With no arguments, list all breaks. With a line number argument, set a breakpoint at this line in the current file.
w	Print a stack trace, with the most recent frame at the bottom. An arrow indicates the current frame, which determines the context of most commands.
u	Move the current frame count (default one) levels up in the stack trace (to an older frame).
d	Move the current frame count (default one) levels down in the stack trace (to a newer frame).
h	See a list of available commands.
h <topic>	Show help for a command or topic.
h pdb	Show the full pdb documentation.
q	Quit the debugger and exit.
"""



def prime(x:int, y: int) -> list[bool]:
    """ doc block """
    primes = [True] * (y + 1)
    # 0 and 1 are not prime
    primes[0], primes[1] = False, False

    # insert
    for i in range(2, int(y ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, y + 1, i):
                primes[j] = False
    breakpoint()
    res = [i for i in range(x, y + 1) if primes[i]]
    return res

x, y = 2, 7
res = prime(x, y)
print(res if res else "No")
