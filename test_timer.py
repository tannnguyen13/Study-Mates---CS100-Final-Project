from unittest import mock
from mock import patch, MagicMock
import sys
import io
import time
from unittest import TestCase
from timer import *

class TestTimer(TestCase):
    @mock.patch('timer.input', create=True)
    def test_run_timer1(self, mocked_input):
        with patch("time.sleep"):
            supress_text = io.StringIO()
            sys.stdout = supress_text
            
            mocked_input.side_effect = ['1']
            t = Timer()
            t.run_timer()

            result = t.return_total_time()
            self.assertEqual(result, 4)

            sys.stdout = sys.__stdout__

    @mock.patch('timer.input', create=True)
    def test_run_timer0(self, mocked_input):
        with patch("time.sleep"):
            capturedOut = io.StringIO()
            sys.stdout = capturedOut
            
            mocked_input.side_effect = ['0']
            t = Timer()
            t.run_timer()

            sys.stdout = sys.__stdout__
            print('Expected result for 0 minutes: ', capturedOut.getvalue())

    
    @mock.patch('timer.input', create=True)
    def test_run_timer20(self, mocked_input):
        with patch("time.sleep"):
            supress_text = io.StringIO()
            sys.stdout = supress_text
            
            mocked_input.side_effect = ['20']
            t = Timer()
            t.run_timer()

            result = t.return_total_time()
            self.assertEqual(result, 80)

            sys.stdout = sys.__stdout__

    @mock.patch('timer.input', create=True)
    def test_convert_hours20(self, mocked_input):
        with patch("time.sleep"):
            supress_text = io.StringIO()
            sys.stdout = supress_text
            
            mocked_input.side_effect = ['20']
            t = Timer()
            t.run_timer()

            t.return_total_time()
            t.convert_hours()
            hours = t.return_hours()
            minutes = t.return_minutes()
            self.assertEqual(hours, 1)
            self.assertEqual(minutes, 20)

            sys.stdout = sys.__stdout__

    @mock.patch('timer.input', create=True)
    def test_convert_hours30(self, mocked_input):
        with patch("time.sleep"):
            supress_text = io.StringIO()
            sys.stdout = supress_text
            
            mocked_input.side_effect = ['30']
            t = Timer()
            t.run_timer()

            t.return_total_time()
            t.convert_hours()
            hours = t.return_hours()
            minutes = t.return_minutes()
            self.assertEqual(hours, 2)
            self.assertEqual(minutes, 0)

            sys.stdout = sys.__stdout__

    @mock.patch('timer.input', create=True)
    def test_print_hours20(self, mocked_input):
        with patch("time.sleep"):
            
            
            mocked_input.side_effect = ['20']
            t = Timer()

            supress_text = io.StringIO()

            sys.stdout = supress_text
            t.run_timer()
            sys.stdout = sys.__stdout__

            capturedOut = io.StringIO()
            sys.stdout = capturedOut
            t.convert_hours()
            t.print_total_time()

            sys.stdout = sys.__stdout__
            print('Expected result for 20 minutes: ', capturedOut.getvalue())

    @mock.patch('timer.input', create=True)
    def test_print_hours30(self, mocked_input):
        with patch("time.sleep"):
            
            
            mocked_input.side_effect = ['30']
            t = Timer()

            supress_text = io.StringIO()

            sys.stdout = supress_text
            t.run_timer()
            sys.stdout = sys.__stdout__

            capturedOut = io.StringIO()
            sys.stdout = capturedOut
            t.convert_hours()
            t.print_total_time()

            sys.stdout = sys.__stdout__
            print('Expected result for 30 minutes: ', capturedOut.getvalue())


