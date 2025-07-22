from model_loader import load_emotion_model

emotion_model = load_emotion_model()

def detect_emotion(text):
    results = emotion_model(text)
    sorted_results = sorted(results[0], key=lambda x: x['score'], reverse=True)
    return sorted_results[0]['label'], sorted_results
