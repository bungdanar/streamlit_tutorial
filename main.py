import streamlit as st

# Define the pages
main_page = st.Page("pages/main_page.py", title="Main Page", icon="🎈")
page_2 = st.Page("pages/page_2.py", title="Page 2", icon="❄️")
page_3 = st.Page("pages/page_3.py", title="Page 3", icon="🎉")
uber_page = st.Page('pages/uber_pickups.py')
counter_page = st.Page('pages/counter.py')
forms_page = st.Page('pages/forms.py')

# Set up navigation
pg = st.navigation(
    [main_page, page_2, page_3, uber_page, counter_page, forms_page])

# Run the selected page
pg.run()
