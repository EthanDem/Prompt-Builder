import streamlit as st
import json

# Read in the JSON data
with open('/mount/src/prompt-builder/prompt_builder_templates.json', 'r') as f:
    templates = json.load(f)

# Create mappings from name to prompt for each category

expert_details_map = {item['name']: item['prompt'] for item in templates.get('EXPERTS', [])}
needed_output_map = {item['name']: item['prompt'] for item in templates.get('NEEDED OUTPUT', [])}
writing_style_map = {item['name']: item['prompt'] for item in templates.get('WRITING STYLE', [])}
point_of_view_map = {item['name']: item['prompt'] for item in templates.get('Point of View', [])}
goal_map = {item['name']: item['prompt'] for item in templates.get('Goal', [])}
markup_map = {item['name']: item['prompt'] for item in templates.get('Markup', [])}

st.sidebar.title("Templates")

selected_expert = st.sidebar.selectbox("Expert Details Templates", [""] + list(expert_details_map.keys()), key="expert")
selected_output = st.sidebar.selectbox("Needed Output Templates", [""] + list(needed_output_map.keys()), key="output")
selected_style = st.sidebar.selectbox("Writing Style Templates", [""] + list(writing_style_map.keys()), key="style")
selected_pov = st.sidebar.selectbox("Point Of View Templates", [""] + list(point_of_view_map.keys()), key="pov")
selected_goal = st.sidebar.selectbox("Goal Templates", [""] + list(goal_map.keys()), key="goal")
selected_markup = st.sidebar.selectbox("Markup Templates", [""] + list(markup_map.keys()), key="markup")

st.title("Prompt Builder GUI")
company_name = st.text_input("Company/Person Name")
expert_details = st.text_input("Expert Details", value=expert_details_map.get(selected_expert, ""))
needed_output = st.text_input("Needed Output", value=needed_output_map.get(selected_output, ""))
writing_style = st.text_input("Writing Style", value=writing_style_map.get(selected_style, ""))
point_of_view = st.text_input("Point of View", value=point_of_view_map.get(selected_pov, ""))
goal = st.text_input("Goal", value=goal_map.get(selected_goal, ""))
markup = st.text_input("Markup", value=markup_map.get(selected_markup, ""))

original_text = '''[EXPERT DETAILS] You have been hired by [COMPANY/PERSON NAME] to [NEEDED OUTPUT]
You are to write from the point of view of [POINT OF VIEW]. The overall goal of this output is [GOAL]
In order to provide a perfect and complete output, access any and all information you have access,
which includes: files and content stored in your database, attachments provided if any,
as well as any content provided within this prompt. Your output needs to be complete and final
when you provide the output as this will be sent directly to a user without me reviewing it
so it should always be a completed output. Do not use inert tags or any placeholder text.
If you feel there should be an area that requires a custom input or placeholder text,
please write around the need. This needs to be an output ready for a user to see.
Strictly adhere to the WRITING STYLE provided for tone, overall style of the content
and capture the voice as much as you can.
Please follow the following formatting requirements:
2.) MARKUP - Please use the following Markup and Structure details for the output provided here: [MARKUP]
3.) WRITING STYLE= [WRITING STYLE]

Ok, that is the base instructions, now follow these details and create an output described provided here:
USER PROMPT= '''

if st.button("Generate Prompt"):
    updated_text = original_text.replace("[COMPANY/PERSON NAME]", company_name)
    updated_text = updated_text.replace("[EXPERT DETAILS]", expert_details)  # Use updated_text here
    updated_text = updated_text.replace("[NEEDED OUTPUT]", needed_output)
    updated_text = updated_text.replace("[WRITING STYLE]", writing_style)
    updated_text = updated_text.replace("[POINT OF VIEW]", point_of_view)
    updated_text = updated_text.replace("[GOAL]", goal)
    updated_text = updated_text.replace("[MARKUP]", markup)
    
    st.subheader("Prompt")
    st.write(updated_text)
