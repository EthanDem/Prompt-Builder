import streamlit as st

original_text = '''You are [EXPERT DETAILS]. You have been hired by [COMPANY/PERSON NAME] to [NEEDED OUTPUT].
You are to write from the point of view of [POINT OF VIEW]. The overall goal of this output is [GOAL].
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
USER PROMPT= [USER PROMPT]
'''

st.title("Text Placeholder Replacer")

expert_details = st.text_input("Expert Details", value="", help="Replace [EXPERT DETAILS]")
company_name = st.text_input("Company/Person Name", value="", help="Replace [COMPANY/PERSON NAME]")
needed_output = st.text_input("Needed Output", value="", help="Replace [NEEDED OUTPUT]")
writing_style = st.text_input("Writing Style", value="", help="Replace [WRITING STYLE]")
point_of_view = st.text_input("Point of View", value="", help="Replace [POINT OF VIEW]")
goal = st.text_input("Goal", value="", help="Replace [GOAL]")
markup = st.text_input("Markup", value="", help="Replace [MARKUP]")
user_prompt = st.text_input("User Prompt", value="", help="Replace [USER PROMPT]")

if st.button("Generate Text"):
    # Replace placeholders with user input
    updated_text = original_text.replace("[EXPERT DETAILS]", expert_details)
    updated_text = updated_text.replace("[COMPANY/PERSON NAME]", company_name)
    updated_text = updated_text.replace("[NEEDED OUTPUT]", needed_output)
    updated_text = updated_text.replace("[WRITING STYLE]", writing_style)
    updated_text = updated_text.replace("[POINT OF VIEW]", point_of_view)
    updated_text = updated_text.replace("[GOAL]", goal)
    updated_text = updated_text.replace("[MARKUP]", markup)
    updated_text = updated_text.replace("[USER PROMPT]", user_prompt)
    
    st.subheader("Updated Text")
    st.write(updated_text)

