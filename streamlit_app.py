import streamlit as st

# Templates for the sidebar
expert_details_templates = ["EXAMPLE 1", "EXAMPLE 2", "EXAMPLE 3"]
needed_output_templates = ["EXAMPLE 1", "EXAMPLE 2", "EXAMPLE 3"]
point_of_view_templates = ["EXAMPLE 1", "EXAMPLE 2", "EXAMPLE 3"]
goal_templates = ["EXAMPLE 1", "EXAMPLE 2", "EXAMPLE 3"]
markup_templates = ["EXAMPLE 1", "EXAMPLE 2", "EXAMPLE 3"]
writing_style_templates = ["EXAMPLE 1", "EXAMPLE 2", "EXAMPLE 3"]

# Sidebar with template selection
st.sidebar.title("Templates")

selected_expert = st.sidebar.selectbox("Expert Details Templates", [""] + expert_details_templates, key="expert")
selected_output = st.sidebar.selectbox("Needed Output Templates", [""] + needed_output_templates, key="output")
selected_pov = st.sidebar.selectbox("Point Of View Templates", [""] + point_of_view_templates, key="pov")
selected_goal = st.sidebar.selectbox("Goal Templates", [""] + goal_templates, key="goal")
selected_markup = st.sidebar.selectbox("Markup Templates", [""] + markup_templates, key="markup")
selected_style = st.sidebar.selectbox("Writing Style Templates", [""] + writing_style_templates, key="style")

# Main content
st.title("Prompt Builder GUI")

expert_details = st.text_input("Expert Details", value=selected_expert)
company_name = st.text_input("Company/Person Name", value="")
needed_output = st.text_input("Needed Output", value=selected_output)
writing_style = st.text_input("Writing Style", value=selected_style)
point_of_view = st.text_input("Point of View", value=selected_pov)
goal = st.text_input("Goal", value=selected_goal)
markup = st.text_input("Markup", value=selected_markup)

# Original text with placeholders
original_text = '''You are [EXPERT DETAILS]. You have been hired by [COMPANY/PERSON NAME] to [NEEDED OUTPUT].
You are to write from the point of view of [POINT OF VIEW]. The overall goal of this output is [GOAL].
... (rest of the original text)
'''

# Generate prompt
if st.button("Generate Prompt"):
    updated_text = original_text.replace("[EXPERT DETAILS]", expert_details)
    updated_text = updated_text.replace("[COMPANY/PERSON NAME]", company_name)
    updated_text = updated_text.replace("[NEEDED OUTPUT]", needed_output)
    updated_text = updated_text.replace("[WRITING STYLE]", writing_style)
    updated_text = updated_text.replace("[POINT OF VIEW]", point_of_view)
    updated_text = updated_text.replace("[GOAL]", goal)
    updated_text = updated_text.replace("[MARKUP]", markup)
    
    st.subheader("Prompt")
    st.write(updated_text)
