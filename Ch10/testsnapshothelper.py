import snapshothelper
import unittest
import os

class TestCreateSnapshot(unittest.TestCase):
    
    def setUp(self):
        import os
        os.chdir ('c:\\snapshots')

    def tearDown(self):
        os.system('del *.snp')

    def testpython25snap(self):
        # make a snapshot of the Python25 directory
        snapshothelper.createSnapshot('c:\\python25', 'python25snap.snp')
        assert 'python25snap.snp' in os.listdir(os.curdir), 'Snapshot not created!'

    def testprogramfilesdir(self):
        # make a snapshot of the Python25 directory
        snapshothelper.createSnapshot('c:\\program files', 'programfilessnap.snp')
        assert 'programfilessnap.snp' in os.listdir(os.curdir), 'Snapshot not created!'

if __name__ == '__main__':
    unittest.main()

