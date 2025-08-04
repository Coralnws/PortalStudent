# test_portalstudent.py
"""
Tests for PortalStudent module.
"""

import unittest
from portalstudent import PortalStudent

class TestPortalStudent(unittest.TestCase):
    """Test cases for PortalStudent class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PortalStudent()
        self.assertIsInstance(instance, PortalStudent)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PortalStudent()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
