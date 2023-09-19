import streamlit as st
import json

# Load templates from JSON file
with open('/mount/src/prompt-builder/prompt_builder_templates.json', 'r') as f:
    templates = json.load(f)

# Create maps for each template category
expert_details_map = {item['name']: item['prompt'] for item in templates.get('EXPERTS', [])}
needed_output_map = {item['name']: item['prompt'] for item in templates.get('NEEDED OUTPUT', [])}
writing_style_map = {item['name']: item['prompt'] for item in templates.get('WRITING STYLE', [])}
point_of_view_map = {item['name']: item['prompt'] for item in templates.get('Point of View', [])}
goal_map = {item['name']: item['prompt'] for item in templates.get('Goal', [])}
markup_map = {item['name']: item['prompt'] for item in templates.get('Markup', [])}

# Sidebar UI
st.sidebar.title("Templates")
num_instances = st.sidebar.number_input('Number of instances to create', min_value=1, max_value=10, value=1)
selected_expert = st.sidebar.selectbox("Expert Details Templates", [""] + list(expert_details_map.keys()))
selected_output = st.sidebar.selectbox("Needed Output Templates", [""] + list(needed_output_map.keys()))
selected_style = st.sidebar.selectbox("Writing Style Templates", [""] + list(writing_style_map.keys()))
selected_pov = st.sidebar.selectbox("Point Of View Templates", [""] + list(point_of_view_map.keys()))
selected_goal = st.sidebar.selectbox("Goal Templates", [""] + list(goal_map.keys()))
selected_markup = st.sidebar.selectbox("Markup Templates", [""] + list(markup_map.keys()))

# Main UI
st.title("Prompt Builder GUI")

# Original text template
original_text = '''Please analyze and strictly adhere to all of the the instructions in provided in this prompt. You will will follow these instructions and do your best fulfilling the following QUESTION here: [USER PROMPT]
In order to provide a perfect and complete output, access any and all information you have access, which includes: files and content stored in your database, attachments provided if any, as well as any content provided within this prompt. Output Instructions: 

1. You are to act as if you are the person or representitive described here when creating your output: [EXPERT DETAILS] 

2. You should right in the following point gf view:[POINT OF VIEW]

3. Your primary goal with this task is:  [GOAL]

4. Strictly adhere to the following WRITING STYLE: [WRITING STYLE]

5. Your output needs to be complete and final when you provide the output as this will be sent directly to a user without me reviewing it
so it should always be a completed output. Do not use inert tags or any placeholder text. If you feel there should be an area that requires a custom input or placeholder text, please write around the need. This needs to be an output ready for a user to see.

6. Your output should contain the following formatting and Structure details: [MARKUP]

Please provide your output for the QUESTION provided above while strictly adhering to the instructions contained within this prompt. '''

# Lists to hold input values
company_names = []
expert_details_list = []
needed_outputs = []
writing_styles = []
points_of_view = []
goals = []
markups = []
user_prompts = []  # List to hold USER PROMPT values

# Collect inputs for each instance
for i in range(num_instances):
    with st.expander(f'Instance {i + 1}', expanded=True):
        company_names.append(st.text_input(f"Company/Person Name {i + 1}"))
        expert_details_list.append(st.text_input(f"Expert Details {i + 1}", value=expert_details_map.get(selected_expert, "")))
        needed_outputs.append(st.text_input(f"Needed Output {i + 1}", value=needed_output_map.get(selected_output, "")))
        writing_styles.append(st.text_input(f"Writing Style {i + 1}", value=writing_style_map.get(selected_style, "")))
        points_of_view.append(st.text_input(f"Point of View {i + 1}", value=point_of_view_map.get(selected_pov, "")))
        goals.append(st.text_input(f"Goal {i + 1}", value=goal_map.get(selected_goal, "")))
        markups.append(st.text_input(f"Markup {i + 1}", value=markup_map.get(selected_markup, "")))
        user_prompts.append(st.text_input(f"User Prompt {i + 1}"))  # USER PROMPT input box

# Generate prompt action
if st.button("Generate Prompt"):
    for i in range(num_instances):
        updated_text = original_text.replace("[COMPANY/PERSON NAME]", company_names[i])
        updated_text = updated_text.replace("[EXPERT DETAILS]", expert_details_list[i])
        updated_text = updated_text.replace("[NEEDED OUTPUT]", needed_outputs[i])
        updated_text = updated_text.replace("[WRITING STYLE]", writing_styles[i])
        updated_text = updated_text.replace("[POINT OF VIEW]", points_of_view[i])
        updated_text = updated_text.replace("[GOAL]", goals[i])
        updated_text = updated_text.replace("[MARKUP]", markups[i])
        updated_text = updated_text.replace("[USER PROMPT]", f"{user_prompts[i]}")  # Replace USER PROMPT placeholder
        st.subheader(f"Prompt for Instance {i + 1}")
        st.write(updated_text)
