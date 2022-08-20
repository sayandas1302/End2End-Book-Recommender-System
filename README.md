# End2End-Book-Recommender-System
This recommender system uses the popularity based recommender and collaborative filtering based recommender to recommend books for its users.

### Getting Started
1. first download the entire folder and create an virtual environment inside the folder using the commandline '<base interpreter path> -m venv <env name>'
2. once the virtual environment is created, activate it.
3. then in the cmd run the command 'pip install -r requirements.txt' keeping the virtual environment activated. this will install all the required packages in the environment
4. once this is done run 'streamlit run app.py' in the cmd under the environment to run the app.
5. this will create a UI to select your favourite books. once the favourite book is selected click on the button to to get recommendations. also in the top 50 tab you can get the top 50 trending books. 
6. enjoy the app!

### Datasets
Now before you analyse the .ipynb file, you need to extract the .rar file in the dataset folder that contains 3 datasets namely 'Books.csv', 'Users.csv', 'Ratings.csv'. keep the extracted files in the dataset folder to avoid FileNotFoundError in the .ipynb file. you can always change the location of those 3 .csv file but in that case you have to make sure that the file paths that are used in the .ipynb file is consisted=nt.
