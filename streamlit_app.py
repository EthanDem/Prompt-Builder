import streamlit as st
import json

templates = {
    'EXPERTS': [{'name': 'Expert1', 'prompt': 'Prompt for Expert1'}],
    'NEEDED OUTPUT': [{'name': 'Output1', 'prompt': 'Prompt for Output1'}],
    'WRITING STYLE': [{'name': 'Style1', 'prompt': 'Prompt for Style1'}],
    'Point of View': [{'name': 'POV1', 'prompt': 'Prompt for POV1'}],
    'Goal': [{'name': 'Goal1', 'prompt': 'Prompt for Goal1'}],
    'Markup': [{'name': 'Markup1', 'prompt': 'Prompt for Markup1'}]
}

original_text = '''[EXPERT DETAILS] You have been hired by [COMPANY/PERSON NAME] to [NEEDED OUTPUT]
[POINT OF VIEW] [GOAL]
...'''

expert_details_map = {item['name']: item['prompt'] for item in templates.get('EXPERTS', [])}
needed_output_map = {item['name']: item['prompt'] for item in templates.get('NEEDED OUTPUT', [])}
writing_style_map = {item['name']: item['prompt'] for item in templates.get('WRITING STYLE', [])}
point_of_view_map = {item['name']: item['prompt'] for item in templates.get('Point of View', [])}
goal_map = {item['name']: item['prompt'] for item in templates.get('Goal', [])}
markup_map = {item['name']: item['prompt'] for item in templates.get('Markup', [])}

st.sidebar.title("Templates")

num_instances = st.sidebar.number_input('Number of instances to create', min_value=1, max_value=10, value=1)

selected_expert = st.sidebar.selectbox("Expert Details Templates", [""] + list(expert_details_map.keys()))
selected_output = st.sidebar.selectbox("Needed Output Templates", [""] + list(needed_output_map.keys()))
selected_style = st.sidebar.selectbox("Writing Style Templates", [""] + list(writing_style_map.keys()))
selected_pov = st.sidebar.selectbox("Point Of View Templates", [""] + list(point_of_view_map.keys()))
selected_goal = st.sidebar.selectbox("Goal Templates", [""] + list(goal_map.keys()))
selected_markup = st.sidebar.selectbox("Markup Templates", [""] + list(markup_map.keys()))

st.title("Prompt Builder GUI")

for i in range(num_instances):
    with st.expander(f'Instance {i + 1}', expanded=True):  
        company_name = st.text_input(f"Company/Person Name {i + 1}")
        expert_details = st.text_input(f"Expert Details {i + 1}", value=expert_details_map.get(selected_expert, ""))
        needed_output = st.text_input(f"Needed Output {i + 1}", value=needed_output_map.get(selected_output, ""))
        writing_style = st.text_input(f"Writing Style {i + 1}", value=writing_style_map.get(selected_style, ""))
        point_of_view = st.text_input(f"Point of View {i + 1}", value=point_of_view_map.get(selected_pov, ""))
        goal = st.text_input(f"Goal {i + 1}", value=goal_map.get(selected_goal, ""))
        markup = st.text_input(f"Markup {i + 1}", value=markup_map.get(selected_markup, ""))

if st.button("Generate Prompt"):
    for i in range(num_instances):
        st.subheader(f"Prompt for Instance {i + 1}")
        updated_text = original_text.replace("[COMPANY/PERSON NAME]", company_name)
        updated_text = updated_text.replace("[EXPERT DETAILS]", expert_details)
        updated_text = updated_text.replace("[NEEDED OUTPUT]", needed_output)
        updated_text = updated_text.replace("[WRITING STYLE]", writing_style)
        updated_text = updated_text.replace("[POINT OF VIEW]", point_of_view)
        updated_text = updated_text.replace("[GOAL]", goal)
        updated_text = updated_text.replace("[MARKUP]", markup)
        st.write(updated_text)
