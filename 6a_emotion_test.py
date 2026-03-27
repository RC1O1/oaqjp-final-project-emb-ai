"""
6a_emotion_test.py
Test script for emotion_detection module.
Tests the emotion_detector function with multiple sample inputs, including blank input.
"""

# Add EmotionDetection folder to path if your module is inside a subfolder
import sys
sys.path.insert(0, '.')  # assumes emotion_detection.py is in the same folder

try:
    from emotion_detection import emotion_detector
except ModuleNotFoundError:
    # fallback if emotion_detection.py is inside a folder named EmotionDetection
    sys.path.insert(0, './EmotionDetection')
    from emotion_detection import emotion_detector


def main():
    """Run multiple tests on emotion_detector function."""
    test_cases = [
        "I am so happy and excited today!",
        "This is a sad day.",
        "I feel anxious and nervous about the exam.",
        "",  # blank input test
        "Wow! This is amazing!"  
    ]

    for i, text in enumerate(test_cases, 1):
        result = emotion_detector(text)
        print(f"Test Case {i}: '{text}'")
        print("Result:", result)
        print("-" * 50)


if __name__ == "__main__":
    main()
