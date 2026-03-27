"""
4b_packaging_test.py
Test script to verify that the emotion_detection module works correctly.
"""

from emotion_detection import emotion_detector

# Test with a sample text
test_text = "I am feeling really happy today!"
result = emotion_detector(test_text)

print("Test Text:", test_text)
print("Detection Result:", result)

# Test blank input
blank_test = ""
blank_result = emotion_detector(blank_test)

print("Blank Input Test:", blank_result)