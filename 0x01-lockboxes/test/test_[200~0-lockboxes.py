import unittest

from solution import canUnlockAll

class TestCanUnlockAll(unittest.TestCase):
    
    def test_all_boxes_unlocked(self):
        boxes = [[1], [2], [3], []]
        self.assertTrue(canUnlockAll(boxes))
        
    def test_not_all_boxes_unlocked(self):
        boxes = [[1, 2], [3], [4], []]
        self.assertFalse(canUnlockAll(boxes))
        
    def test_empty_boxes(self):
        boxes = [[], [], []]
        self.assertTrue(canUnlockAll(boxes))
        
    def test_single_box(self):
        boxes = [[]]
        self.assertTrue(canUnlockAll(boxes))
        
    def test_invalid_input(self):
        boxes = None
        with self.assertRaises(TypeError):
            canUnlockAll(boxes)
            
if __name__ == '__main__':
    unittest.main()
