"""
Test suite for PhantomStrikes main module
"""

import unittest
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

class TestPhantomStrikes(unittest.TestCase):
    """Test cases for PhantomStrikes main functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        pass
    
    def tearDown(self):
        """Clean up after tests"""
        pass
    
    def test_import_phantomstrikes(self):
        """Test that phantomstrikes module can be imported"""
        try:
            import phantomstrikes
            self.assertTrue(True, "Module imported successfully")
        except ImportError as e:
            self.fail(f"Failed to import phantomstrikes: {e}")
    
    def test_import_socks(self):
        """Test that socks module can be imported"""
        try:
            import socks
            self.assertTrue(True, "SOCKS module imported successfully")
        except ImportError as e:
            self.fail(f"Failed to import socks: {e}")
    
    def test_import_terminal(self):
        """Test that terminal module can be imported"""
        try:
            import terminal
            self.assertTrue(True, "Terminal module imported successfully")
        except ImportError as e:
            self.fail(f"Failed to import terminal: {e}")
    
    def test_useragents_list(self):
        """Test that useragents list is properly defined"""
        import phantomstrikes
        self.assertIsInstance(phantomstrikes.useragents, list)
        self.assertGreater(len(phantomstrikes.useragents), 0)
    
    def test_httpPost_class_exists(self):
        """Test that httpPost class is defined"""
        import phantomstrikes
        self.assertTrue(hasattr(phantomstrikes, 'httpPost'))
        self.assertTrue(issubclass(phantomstrikes.httpPost, phantomstrikes.Thread))

if __name__ == '__main__':
    unittest.main() 