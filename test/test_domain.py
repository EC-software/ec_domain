import ecdomain.domain as d
import unittest


class TestDomain(unittest.TestCase):
    """
    Test the add function from the Domain class
    """

    def test_build_empty(self):  # The Empty Domain
        """ The Empty Domain
        Check how functions react in this special case
        """
        # setUp
        dom_empty = d.Domain('testdomain')
        # Run tests
        self.assertEqual(str(dom_empty), '')
        self.assertEqual(dom_empty.get_val('k'), None)
        self.assertEqual(dom_empty.get_key('v'), None)
        # dominise
        self.assertEqual(dom_empty.dominise('kc'), [])
        self.assertEqual(dom_empty.dominise('kc', all_hits=False), [])
        # find
        # tearDown - Nothing to do...

    def test_build_and_fill_manually(self):
        """ The Scandinavian Domain
        Minimalistic Scandinavia, to serve this test... Sorry FI, IS, FO and AX
        The details around SJ are also dodgy, deliberately to allow specific tests, sorry SJ
        """
        # setUp
        dom_scandi = d.Domain('Scandinavia')
        dom_scandi.set_kv('DK', 'Denmark')  # ISO 3166-1 alpha-2, Short English name
        dom_scandi.set_kv('SE', 'Sweden')  # deliberately out of alphabetic order
        dom_scandi.set_kv('NO', 'Norway')
        dom_scandi.set_kv('SJ', 'Norway')
        dom_scandi.set_alias('DK', 'Danmark')  # Local name
        dom_scandi.set_alias('DK', 'The Kingdom of Denmark')  # Long English name
        dom_scandi.set_alias('NO', 'Norge')  # Local name
        dom_scandi.set_alias('NO', 'The Kingdom of Norway')  # Long English name
        dom_scandi.set_alias('SE', 'Sverige')  # Local name
        dom_scandi.set_alias('SE', 'The Kingdom of Sweden')  # Long English name
        dom_scandi.set_alias('SJ', 'Svalbard og Jan Mayen')  # Local name
        dom_scandi.set_alias('SJ', 'Svalbard and Jan Mayen')  # Long English name
        # Run tests
        self.assertEqual(str(dom_scandi), """DK: Denmark
NO: Norway
SE: Sweden
SJ: Norway
rex: DK: ['Danmark', 'The Kingdom of Denmark']
rex: NO: ['Norge', 'The Kingdom of Norway']
rex: SE: ['Sverige', 'The Kingdom of Sweden']
rex: SJ: ['Svalbard og Jan Mayen', 'Svalbard and Jan Mayen']""")
        self.assertEqual(dom_scandi.get_val('NO'), 'Norway')
        self.assertEqual(dom_scandi.get_val('GB'), None)
        self.assertEqual(dom_scandi.get_key('Sweden'), ['SE'])
        self.assertEqual(dom_scandi.get_key('Germany'), None)
        self.assertEqual(dom_scandi.get_key('Norway'), ['NO', 'SJ'])
        # dominise
        self.assertEqual(dom_scandi.dominise('DK'), ['DK'])  # key -> key
        self.assertEqual(dom_scandi.dominise('Denmark'), ['DK'])  # value -> key
        self.assertEqual(dom_scandi.dominise('Danmark'), ['DK'])  # alias -> key
        self.assertEqual(dom_scandi.dominise('DK', all_hits=False), ['DK'])  # key -> key, only first hit
        self.assertEqual(dom_scandi.dominise('Denmark', all_hits=False), ['DK'])  # value -> key, only first hit
        self.assertEqual(dom_scandi.dominise('Danmark', all_hits=False), ['DK'])  # alias -> key, only first hit
        self.assertEqual(dom_scandi.dominise('Norway'), ['NO', 'SJ'])  # implicit all hits
        self.assertEqual(dom_scandi.dominise('Norway', all_hits=True), ['NO', 'SJ'])  # explicit all hits
        self.assertEqual(dom_scandi.dominise('Norway', all_hits=False), ['NO'])  # only first hit
        # find
        # find
        self.assertEqual(dom_scandi.find('SE'), ['SE'])  # in keys
        self.assertEqual(dom_scandi.find('Denmark'), ['DK'])  # in values
        self.assertEqual(dom_scandi.find('Scotland'), [])
        self.assertEqual(dom_scandi.find('Svalbard'), ['SJ'])  # in alias
        self.assertEqual(dom_scandi.find('The Kingdom of'), ['DK', 'NO', 'SE'])  # in alias
        # tearDown - Nothing to do...

    def test_build_and_fill_from_files(self):
        """ The Boolean Domain that comes with the module
        """
        # setUp
        dom_bool = d.Domain('Boolean')
        dom_bool.read_file(r'..\ecdomain\dom_boolean.scsv')
        # Run tests
        self.assertEqual(str(dom_bool), """0: False
1: True""")
        self.assertEqual(dom_bool.get_val('0'), 'False')
        self.assertEqual(dom_bool.get_key('True'), ['1'])
        self.assertEqual(dom_bool.dominise('0'), ['0'])  # key -> key
        self.assertEqual(dom_bool.dominise('True'), ['1'])  # value -> key
        self.assertEqual(dom_bool.dominise('NO'), [])  # alias -> key (rex files not yet imported...)
        # more setUp
        dom_bool.read_file(r'..\ecdomain\dom_boolean_rex.csv', header=False)
        # more Run tests - Repeat the same tests after reading REX-file
        self.assertEqual(str(dom_bool), """0: False
1: True
rex: 0: ['false', 'FALSE', 'No', 'NO', 'no']
rex: 1: ['true', 'TRUE', 'Yes', 'YES', 'yes']""")
        self.assertEqual(dom_bool.get_val('0'), 'False')
        self.assertEqual(dom_bool.get_key('True'), ['1'])
        self.assertEqual(dom_bool.dominise('0'), ['0'])
        self.assertEqual(dom_bool.dominise('True'), ['1'])
        self.assertEqual(dom_bool.dominise('NO'), ['0'])  # alias -> key (rex is now imported...)
        self.assertEqual(dom_bool.dominise('maybe'), [])
        # find
        self.assertEqual(dom_bool.find('0'), ['0'])  # in keys
        self.assertEqual(dom_bool.find('Tru'), ['1'])  # in values
        self.assertEqual(dom_bool.find('maybe'), [])
        self.assertEqual(dom_bool.find('N'), ['0'])  # in alias
        self.assertEqual(dom_bool.find('Y'), ['1'])  # in alias
        self.assertEqual(dom_bool.find('E'), ['0', '1'])  # in alias
        # tearDown - Nothing to do...


if __name__ == '__main__':
    unittest.main()