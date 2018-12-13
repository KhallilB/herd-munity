class Virus(object):
    '''Properties and attributes of the virus used in Simulation.'''

    def __init__(self, name, basic_repro_num, mortality_rate):
        self.name = name
        self.basic_repro_num = basic_repro_num
        self.mortality_rate = mortality_rate


def test_virus_instantiation():
    # TODO: Create your own test that models the virus you are working with
    '''Check to make sure that the virus instantiator is working.'''
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.basic_repro_num == 0.8
    assert virus.mortality_rate == 0.3
