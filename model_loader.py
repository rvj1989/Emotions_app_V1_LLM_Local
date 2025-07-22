from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import streamlit as st

@st.cache_resource
def load_emotion_model():
    return pipeline(
        "text-classification",
        model="j-hartmann/emotion-english-distilroberta-base",
        top_k=None
    )

@st.cache_resource
def load_local_llm():
    model_id = "microsoft/phi-2"   # lighter model; change if you have GPU
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)
    llm = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.7
    )
    return llm
