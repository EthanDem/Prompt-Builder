import streamlit as st
import json

with open('/mount/src/prompt-builder/fixed_fully_updated_prompt_builder_templates.json', 'r') as f:
    templates = json.load(f)

specific_instructions_map = {item['Name']: item['Prompt'] for item in templates.get('SPECIFIC INSTRUCTIONS', [])}
writing_style_map = {item['Name']: item['Prompt'] for item in templates.get('WRITING STYLE', [])}
goal_map = {item['Name']: item['Prompt'] for item in templates.get('GOAL', [])}
audience_map = {item['Name']: item['Prompt'] for item in templates.get('AUDIENCE', [])}


st.sidebar.title("Templates")
num_instances = st.sidebar.number_input('Number of instances to create', min_value=1, max_value=10, value=1)
selected_specific_instructions = st.sidebar.selectbox("SPECIFIC INSTRUCTIONS", [""] + list(specific_instructions_map.keys()))
selected_writing_style = st.sidebar.selectbox("WRITING STYLE", [""] + list(writing_style_map.keys()))
selected_goal = st.sidebar.selectbox("GOAL", [""] + list(goal_map.keys()))
selected_audience = st.sidebar.selectbox("AUDIENCE", [""] + list(audience_map.keys()))


st.title("Prompt Builder GUI")

company_names = []
specific_instructions_list = []
writing_styles = []
goals = []
audiences = []
user_prompts = []

for i in range(num_instances):
    with st.expander(f'Instance {i + 1}', expanded=True):
        company_names.append(st.text_input(f"Company/Person Name {i + 1}"))
        specific_instructions_list.append(st.text_input(f"SPECIFIC INSTRUCTIONS {i + 1}", value=specific_instructions_map.get(selected_specific_instructions, "")))
        writing_styles.append(st.text_input(f"WRITING STYLE {i + 1}", value=writing_style_map.get(selected_writing_style, "")))
        goals.append(st.text_input(f"GOAL {i + 1}", value=goal_map.get(selected_goal, "")))
        audiences.append(st.text_input(f"AUDIENCE {i + 1}", value=audience_map.get(selected_audience, "")))
        user_prompts.append(st.text_input(f"User Prompt {i + 1}"))

if st.button("Generate Prompt"):
    for i in range(num_instances):
        original_text = '''
        You are [Company/Person Name]. Your mission is detailed under ‘TASK’. Ensure that your output aligns with the ‘GOAL’ and is tailored for ‘AUDIENCE’. Use any resources provided, including the content of this prompt, attachments or your database. The final output will be sent directly to the user. Avoid placeholders or generic labels. Ensure your response matches the ‘WRITING STYLE’ provided.
\nTASK: [SPECIFIC INSTRUCTIONS]
\nAUDIENCE: [AUDIENCE]
\nWRITING STYLE: [WRITING STYLE]
\nGOAL: [GOAL]
\nUSER PROMPT: [USER PROMPT]'''
        
        updated_text = original_text
        updated_text = updated_text.replace("[Company/Person Name]", company_names[i])
        updated_text = updated_text.replace("[SPECIFIC INSTRUCTIONS]", specific_instructions_list[i])
        updated_text = updated_text.replace("[AUDIENCE]", audiences[i])
        updated_text = updated_text.replace("[WRITING STYLE]", writing_styles[i])
        updated_text = updated_text.replace("[GOAL]", goals[i])
        updated_text = updated_text.replace("[USER PROMPT]", user_prompts[i])
        
        st.subheader(f"Prompt for Instance {i + 1}")
        st.write(updated_text)
