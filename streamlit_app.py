import streamlit as st
import json

# Load templates from JSON file
with open('/mount/src/prompt-builder/final_updated_prompt_builder_templates.json', 'r') as f:
    templates = json.load(f)

# Create maps for each template category
act_as_map = {item['Name']: item['Prompt'] for item in templates.get('Act as if you are a...', [])}
create_following_map = {item['Name']: item['Prompt'] for item in templates.get('You are creating the following...', [])}
writing_style_map = {item['Name']: item['Prompt'] for item in templates.get('Writing Style', [])}
goal_audience_map = {item['Name']: item['Prompt'] for item in templates.get('The goal for the audience is', [])}
point_of_view_map = {item['Name']: item['Prompt'] for item in templates.get('Point of View', [])}

# Sidebar UI
st.sidebar.title("Templates")
num_instances = st.sidebar.number_input('Number of instances to create', min_value=1, max_value=10, value=1)
selected_act_as = st.sidebar.selectbox("Act as if you are a...", [""] + list(act_as_map.keys()))
selected_create_following = st.sidebar.selectbox("You are creating the following...", [""] + list(create_following_map.keys()))
selected_style = st.sidebar.selectbox("Writing Style", [""] + list(writing_style_map.keys()))
selected_goal_audience = st.sidebar.selectbox("The goal for the audience is", [""] + list(goal_audience_map.keys()))
selected_point_of_view = st.sidebar.selectbox("Point of View", [""] + list(point_of_view_map.keys()))

# Main UI
st.title("Prompt Builder GUI")

# Lists to hold input values
company_names = []
act_as_list = []
create_following_list = []
writing_styles = []
goal_audiences = []
points_of_view = []
user_prompts = []

# Collect inputs for each instance
for i in range(num_instances):
    with st.expander(f'Instance {i + 1}', expanded=True):
        company_names.append(st.text_input(f"Company/Person Name {i + 1}"))
        act_as_list.append(st.text_input(f"Act as if you are a... {i + 1}", value=act_as_map.get(selected_act_as, "")))
        create_following_list.append(st.text_input(f"You are creating the following... {i + 1}", value=create_following_map.get(selected_create_following, "")))
        writing_styles.append(st.text_input(f"Writing Style {i + 1}", value=writing_style_map.get(selected_style, "")))
        goal_audiences.append(st.text_input(f"The goal for the audience is {i + 1}", value=goal_audience_map.get(selected_goal_audience, "")))
        points_of_view.append(st.text_input(f"Point of View {i + 1}", value=point_of_view_map.get(selected_point_of_view, "")))
        user_prompts.append(st.text_input(f"User Prompt {i + 1}"))

# Generate prompt action
if st.button("Generate Prompt"):
    for i in range(num_instances):
        original_text = '''Please analyze and strictly adhere to all of the the instructions in provided in this prompt. You will will follow these instructions and do your best fulfilling the following QUESTION here: [USER PROMPT] .
In order to provide a perfect and complete output, access any and all information you have access, which includes: files and content stored in your database, attachments provided if any, as well as any content provided within this prompt. Output Instructions: 

1. You are to act as if you are the person or representative described here when creating your output: [ACT AS IF YOU ARE A...]

2. You are producing this content on behalf of: [Company/Person Name]

3. You are tasked to create the following: [YOU ARE CREATING THE FOLLOWING...]

4. You should write in the following point of view: [POINT OF VIEW]

5. Your primary goal with this task is:  [THE GOAL FOR THE AUDIENCE IS]

6. Strictly adhere to the following WRITING STYLE: [WRITING STYLE]

Please provide your output for the QUESTION provided above while strictly adhering to the instructions contained within this prompt.'''
        
        updated_text = original_text
        updated_text = updated_text.replace("[Company/Person Name]", company_names[i])
        updated_text = updated_text.replace("[ACT AS IF YOU ARE A...]", act_as_list[i])
        updated_text = updated_text.replace("[YOU ARE CREATING THE FOLLOWING...]", create_following_list[i])
        updated_text = updated_text.replace("[WRITING STYLE]", writing_styles[i])
        updated_text = updated_text.replace("[THE GOAL FOR THE AUDIENCE IS]", goal_audiences[i])
        updated_text = updated_text.replace("[POINT OF VIEW]", points_of_view[i])
        updated_text = updated_text.replace("[USER PROMPT]", user_prompts[i])
        
        st.subheader(f"Prompt for Instance {i + 1}")
        st.write(updated_text)
