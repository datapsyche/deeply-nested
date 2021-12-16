import unittest
import os

from pathlib import Path
from pdb import set_trace as st

from src import NestedObject



current_path = Path(os.path.dirname(os.path.realpath(__file__)))
test_data = f"{current_path}/testdata"

class TestNestedObject(unittest.TestCase):
    def setUp(self):
        self.d = NestedObject()
        self.d.data = f'{test_data}/sample.json'

    def test_datatype(self):        
        self.assertIsInstance(self.d.data, (dict, list))
    
    def test_length(self):
        usernames = self.d.get(key='username')
        assert len(usernames)==10
    
    def test_list(self):
        usernames = self.d.get(key='username')
        username_tuple = usernames[0]
        self.assertIsInstance(username_tuple, tuple)
    
    def test_getkey(self):
        catchphrases = self.d.get(key='catchPhrase')
        catchphrase_1 = catchphrases[0][1]
        self.assertIsInstance(catchphrase_1, str)
    
    def test_paths(self):
        paths = self.d.paths
        self.assertIsInstance(paths, list)
    
    def test_length_of_paths(self):
        paths = self.d.paths
        assert len(paths)==190
    
    def test_length_of_paths(self):
        paths = self.d.paths
        assert len(paths)==190
    
    def test_getkeypath(self):
        name_tuple = self.d.get(keypath="[0]/name")
        self.assertEqual(name_tuple[1], 'Leanne Graham')
    
    def test_getipath(self):
        iobjects = self.d.get(keypath='[i]')
        self.assertIsInstance(iobjects, list)
    
    def test_getikeypath(self):
        name_tuple = self.d.get(keypath='[6]/name')
        self.assertEqual(name_tuple[1], 'Kurtis Weissnat') 

    def test_keys(self):
        keys = self.d.keys()
        self.assertIsInstance(keys, list)  

    def tearDown(self):
        del(self.d) 

if __name__ == "__main__":
    unittest.main()