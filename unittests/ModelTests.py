#!/usr/bin/env python
"""
model tests
"""

import os
import sys
import unittest
from prophet_model import model_train, model_predict

class ModelTest(unittest.TestCase):
    """
    test the essential functionality
    """
        
    def test_train_model(self):
        """
        test the train functionality
        """

        ## train the model
        val=model_train()
        self.assertTrue(val)
       
    def test_predict(self):
        """
        test the predict function input
        """
    
        result = model_predict("all","2018","11","11")

        self.assertTrue(result.yhat.values[0] > 5300)

    def test_predict_country(self):
        """
        test the predict function input
        """
    
        result = model_predict("finland","2018","11","11")
        self.assertEqual(result,"Could not find country called finland")

    def test_predict_date(self):
        """
        test the predict function input
        """
    
        result = model_predict("all","2300","11","11")
        self.assertEqual(result,"Date not available")

### Run the tests
if __name__ == '__main__':
    unittest.main()
