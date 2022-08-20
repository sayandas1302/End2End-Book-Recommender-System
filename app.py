import streamlit as st
import numpy as np
import pandas as pd
import pickle 

# importing artifacts
#------------------------------
# pivot table is required to find the book name list and also the name of the suggested book from their index value
with open('./artifacts/pivot_table.pkl', 'rb') as file:
    pivot_table = pickle.load(file)

# similarity score is required in the recommend function to find out the books similar to the selected book
with open('./artifacts/similarity_score.pkl', 'rb') as file:
    similarity_score = pickle.load(file)

# book_with_info dataframe required inside of the recommend function to find out the author name and book front page of the suggested books
with open('./artifacts/book_with_info.pkl', 'rb') as file:
    book_with_info = pickle.load(file)

with open('./artifacts/popularity_df.pkl', 'rb') as file:
    popularity_df = pickle.load(file)

# it is given in the books names selectbox
book_names_list = pivot_table.index

# functionality
#------------------------------
def recommend(book_name):
    book_index = np.where(pivot_table.index==book_name)[0][0]
    suggested_book_index = sorted(list(enumerate(similarity_score[book_index])), key=lambda x:x[1], reverse=True)[1:6]
    suggested_book_name = [pivot_table.index[books[0]] for books in suggested_book_index]
    authors = []
    images_url = []
    for book in suggested_book_name:
        authors.append(np.array(book_with_info[book_with_info['Book-Title']==book]['Book-Author'])[0])
        images_url.append(np.array(book_with_info[book_with_info['Book-Title']==book]['Image-URL-M'])[0])
    return suggested_book_name, authors, images_url

# setting up an UI
#------------------------------
# title
st.markdown('''
# Books Recommendation System
''')

# background
st.markdown(f"""
    <style>
        .stApp{{
            background-image: url('https://miro.medium.com/max/1400/0*a_BDQwp3z5P9sUXq'); 
            background-size: cover;
            background-attachment: fixed;
        }}
        .st-c6{{
            background: none;
        }}
    </style>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(['Search Your Books', 'Top 50'])

# collabortive filtering based recommendation front-end (and back-end)
with tab1:
    st.markdown('''
    ### What's your favourite book?
    ''')
    selected_book = st.selectbox('', book_names_list)
    if st.button('Recommend'):
        suggested_books, authors, image_url = recommend(selected_book)

        st.markdown('''
        ### Recommendations for you
        ''')
        
        col0, col1, col2, col3, col4 = st.columns(5)

        with col0:
            st.image(image_url[0])
            st.markdown(f'''
            ***{suggested_books[0]}*** \n
            By ***{authors[0]}***''')

        with col1:
            st.image(image_url[1])
            st.markdown(f'''
            ***{suggested_books[1]}*** \n
            By ***{authors[1]}***''')

        with col2:
            st.image(image_url[2])
            st.markdown(f'''
            ***{suggested_books[2]}*** \n
            By ***{authors[2]}***''')
        
        with col3:
            st.image(image_url[3])
            st.markdown(f'''
            ***{suggested_books[3]}*** \n
            By ***{authors[3]}***''')

        with col4:
            st.image(image_url[4])
            st.markdown(f'''
            ***{suggested_books[4]}*** \n
            By ***{authors[4]}***''')

# popularity based recommendation front-end (and back-end)
with tab2:
    st.markdown('''
    ## Top 50 Books
    ''')

    for index in range(popularity_df.shape[0]):
        book = popularity_df.iloc[index,:]

        col1, col2 = st.columns([1,3])

        with col1:
            st.image(book['Image-URL-M'])

        with col2:
            st.markdown(f'''
            #### {book['Book-Title']} \n
            ##### Book by: {book['Book-Author']}
            ###### Average ratings: ⭐{round(book['avg_rating'], 1)}
            ###### Number of rating: {book['num_rating']}
            ''')