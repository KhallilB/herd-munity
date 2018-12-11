import pytest
import io
import sys
import simulation
import math
import random

def test_sim():

    sim = simulation()
    sim._create_population()
    assert len(sim.population) == 10


