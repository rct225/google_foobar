Bomb, Baby!

There are two types of bombs: Mach bombs (M) and Facula bombs (F)

The bombs self-replicate via one of 2 ways: For every Mach bomb, a Facula bomb is created; or for every Facula bomb a Mach bomb is created.

E.g. 3 Mach bombs and 2 Facula bombs either produce 3 Mach bombs and 5 Facula bombs, or 5 Mach bombs and 2 Facula bombs. The replication process can be changed each cycle.

You start with 1 Mach and 1 Facula bomb.

Write a function answer(M, F) where M and F are the number of Mach and Facula bombs needed. Return the fewest number of generations (as a string) that need to pass until you reach the required target, or the string "impossible" if this can't be done! M and F will be string representations of positive integers no larger than 10^50.

Examples

Inputs: (string) M = "2" (string) F = "1" Output: (string) "1"

Inputs: (string) M = "4" (string) F = "7" Output: (string) "4"

Inputs: (string) M = "2" (string) F = "4" Output: (string) "impossible"

