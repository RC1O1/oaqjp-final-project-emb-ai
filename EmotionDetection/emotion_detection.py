# emotion_detection.py

def emotion_detector(text):
    # Step 1: Check for blank input
    if not text.strip():  # text is empty or only spaces
        return {
            "dominant_emotion": None,
            "all_emotions": None,
            "confidence_score": None,
            "status_code": 400
        }
    
    # Step 2: Normal emotion detection code
    # Replace these with your actual AI logic
    dominant_emotion = "happy"  # example placeholder
    all_emotions = {"happy": 0.9, "sad": 0.1}  # example placeholder
    confidence_score = 0.9       # example placeholder
    
    return {
        "dominant_emotion": dominant_emotion,
        "all_emotions": all_emotions,
        "confidence_score": confidence_score,
        "status_code": 200