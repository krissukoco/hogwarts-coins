# QUESTION:
# In Hogwarts the currency is made up of galleon (G) and Sickle (s), 
# and there are seven coins in general circulation:
# 1s, 5s, 10s, 25s, 50s, G1(100s), and G2(200s)
# It's possible to make G3.5 in the following way:
# 1xG2 +1xG1 + 4x10s +1x5s + 5x1s
# How many different ways can G3.5 be made using any number of coins?

# USING RECURSION METHOD
# For the answer, kindly check main.py

from dataclasses import dataclass
from typing import List
import time

S1: int = 1
S5: int = 5
S10: int = 10
S25: int = 25
S50: int = 50
G1: int = 100
G2: int = 200

@dataclass
class Combination:
    target: int
    G2: int = 0
    G1: int = 0
    S50: int = 0
    S25: int = 0
    S10: int = 0
    S5: int = 0
    S1: int = 0

    def __str__(self):
        return f"{self.G2} x G2 | {self.G1} x G1 | {self.S50} x S50 | {self.S25} x S25" + \
                f" | {self.S10} x S10 | {self.S5} x S5 | {self.S1} x S1"
    
    def value(self):
        return self.G2 * G2 + self.G1 * G1 + self.S50 * S50 + self.S25 * S25 + \
                self.S10 * S10 + self.S5 * S5 + self.S1 * S1
    
    def remaining(self) -> int:
        return self.target - self.value()
    
    def has_remaining(self) -> bool:
        return self.remaining() > 0
    
    def is_fulfilled(self) -> bool:
        return self.target == self.value()    

def get_combinations(target: int) -> List[Combination]:
    if target < 1:
        raise ValueError("target can only be >= 1")
    
    _start = time.time()
    combinations: List[Combination] = []

    for g2 in range(target // G2 + 1):
        print("g2", g2)
        # NOTE on performance and optimization:
        # To improve performance, on the beginning of each loop, create a combination object
        # if combination has no remaining value, then check if it is fulfilled.
        # If it is already fulfilled, then add to combinations list/array.
        # then we can skip the rest of the loop
        # No reason to add more coins, because the combination value is already bigger or equal to the target
        # Case Study: (target = 350)
        # If run without making and checking combination, it will take 170 seconds to run
        # With the optimization, it will take only 5.5 seconds to run
        # -> 30x faster or 96% lower runtime
        comb = Combination(target=target, G2=g2)
        if not comb.has_remaining():
            if comb.is_fulfilled():
                combinations.append(comb)
            continue
        for g1 in range(target // G1 + 1):
            comb = Combination(target=target, G2=g2, G1=g1)
            if not comb.has_remaining():
                if comb.is_fulfilled():
                    combinations.append(comb)
                continue
            for s50 in range(target // S50 + 1):
                comb = Combination(target=target, G2=g2, G1=g1, S50=s50)
                if not comb.has_remaining():
                    if comb.is_fulfilled():
                        combinations.append(comb)
                    continue
                for s25 in range(target // S25 + 1):
                    comb = Combination(target=target, G2=g2, G1=g1, S50=s50, S25=s25)
                    if not comb.has_remaining():
                        if comb.is_fulfilled():
                            combinations.append(comb)
                        continue
                    for s10 in range(target // S10 + 1):
                        comb = Combination(target=target, G2=g2, G1=g1, S50=s50, S25=s25, S10=s10)
                        if not comb.has_remaining():
                            if comb.is_fulfilled():
                                combinations.append(comb)
                            continue
                        for s5 in range(target // S5 + 1):
                            comb = Combination(target=target, G2=g2, G1=g1, S50=s50, S25=s25, S10=s10, S5=s5)
                            if not comb.has_remaining():
                                if comb.is_fulfilled():
                                    combinations.append(comb)
                                continue
                            for s1 in range(target // S1 + 1):
                                comb = Combination(target, g2, g1, s50, s25, s10, s5, s1)
                                if not comb.has_remaining():
                                    if comb.is_fulfilled():
                                        combinations.append(comb)
                                    continue

    print(f"Found {len(combinations)} combinations | Time: {time.time() - _start} seconds")
    return combinations

# Put test case here
TARGET = 350
combinations = get_combinations(TARGET)
print(len(combinations))


# UNOPTIMIZED VERSION
def get_combinations_unoptimized(target: int) -> List[Combination]:
    if target < 1:
        raise ValueError("target can only be >= 1")
    
    _start = time.time()
    combinations: List[Combination] = []

    for g2 in range(target // G2 + 1):
        for g1 in range(target // G1 + 1):
            for s50 in range(target // S50 + 1):
                for s25 in range(target // S25 + 1):
                    for s10 in range(target // S10 + 1):
                        for s5 in range(target // S5 + 1):
                            for s1 in range(target // S1 + 1):
                                comb = Combination(target, g2, g1, s50, s25, s10, s5, s1)
                                if comb.is_fulfilled():
                                    combinations.append(comb)

    print(f"Finished: {time.time() - _start} seconds | Found {len(combinations)} combinations")
    return combinations

# Put test case here
# TARGET = 350
# combinations = get_combinations_unoptimized(TARGET)
# print(len(combinations))