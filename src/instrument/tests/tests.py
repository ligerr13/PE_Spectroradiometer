import asyncio
import logging
import unittest
from unittest import IsolatedAsyncioTestCase 
from src.instrument import Instrument as CS2000
from src.commands import Measure, RemoteModeSelect

logging.basicConfig(level=logging.DEBUG)

@CS2000.connection(port='COM4', baudrate=9600)
async def _test_1(protocol):
    """
        Test to perform the measurement.
    """
    await RemoteModeSelect(protocol, operation=1)

    data = await Measure(protocol)

    return data

class Testing(IsolatedAsyncioTestCase):
    async def test_measure(self):
        try:
            result = await _test_1()

            self.assertIsNotNone(result, "Result should not be None")

            self.assertTrue(hasattr(result, 'complete'), "Result should have 'complete' attribute")
            self.assertEqual(result.complete.response, "OK00", f"Measurement did not complete successfully. Received: {result.complete.response}")

            logging.debug("Measurement completed successfully.")
            
        except Exception as e:
            logging.error(f"Test failed due to exception: {e}")
            self.fail(f"Test failed due to exception: {e}")

if __name__ == '__main__':
    unittest.main()
