from model_loader import load_local_llm

llm_pipeline = load_local_llm()

def get_ai_reply(prompt):
    outputs = llm_pipeline(prompt)
    generated = outputs[0]['generated_text']
    reply = generated[len(prompt):].strip()  # remove prompt part
    return reply
