import re

colognePhon_dict = {'aeiouy': 0,
                    ['h']: '-',
                    ['b','p']: 1,
                    ['d','t']: 2,
                    ['f','v','w']: 3,
                    ['ph']: 3,
                    ['g', 'k', 'q']: 4,
                    ['c']: 4,
                    ['x']: 48,
                    }

""""
A, E, I, J, O, U, Y                         --> 0
H                                               -
B                                           --> 1
P                   nicht vor H             --> 1
D, T                nicht vor C, S, Z       --> 2
F, V, W                                     --> 3
P                   vor H                   --> 3
G, K, Q                                     --> 4
C                   im Anlaut vor A, H, K, L, O, Q, R, U, X             --> 4
C                   vor A, H, K, O, Q, U, X ausser S, Z                 --> 4
X                   nicht nach C, K, Q      --> 48
L                                           --> 5
M, N                                        --> 6
R                                           --> 7
S, Z                                        --> 8
C                   im Anlaut ausser vor A, H, K, L, O, Q, R, U, X     --> 8
C                   nicht vor A, H, K, O, Q, U, X ausser S, Z          --> 8
D, T                vor C, S, Z             --> 8
X                   nach C, K, Q            --> 8
"""
