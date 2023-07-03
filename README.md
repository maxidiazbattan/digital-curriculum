![digital-resume-crop.jpg](https://github.com/maxidiazbattan/digital-resume/blob/main/digital-resume-crop.jpg)

# Digital curriculum

This is my resume, made entirely with Streamlit (a Python library to create web apps and pages), in which you'll be able to find my work experience, qualifications, and different projects that I have carried out. It's not an original idea, but I like it. To see it, click on the following badge:

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://maxidiazbattan-digital-curriculum.streamlit.app/)


# Streamlit Share Deployment

## Copy this repo to your own personal one
1. On https://github.com/new, create a new repository  
2. In your terminal, in your home directory, clone the repo
3. `cd` into the repository that is created and you should see all the files now.
4. Then, connect this cloned repo to your new personal repo made in Step 1: `git remote set-url origin https://www.github.com/{your-username}/digital-curriculum.git` (be sure to change your username and remove the curly braces)
5. Run `git push origin main` to push the local repo to remote. You should now see this same code in your personal `categorizer` repo.

## Run Application
1. Run command in terminal `streamlit run app.py` (or your app name)
2. Preview web page in browser '/'

## Deploy to Streamlit
1. Add your app to GitHub. Streamlit Cloud launches apps directly from your GitHub repo, so your app code and dependencies need to be on GitHub before you try to deploy the app.
2. Create a free account on Streamlit Share.
3. Create a `requirements.txt` file with all your non-standard dependencies (based on any libraries you are importing), separated by a newline. In our case, they are `Flask` w/ a capital F. Note that libraries like `os` are standard imports, so they don't need to be included.
4. To deploy an app, click "New app" from the upper right corner of your workspace, then fill in your repo, branch, and file path, and click "Deploy". As a shortcut, you can also click "Paste GitHub URL".
5. Advanced settings for deployment, If you are connecting to a data source or want to select a Python version for your app, you can do that by clicking "Advanced settings" before you deploy the app.
6. Your app is now deploying and you can watch while it launches. Most apps take only a couple of minutes to deploy, but if your app has a lot of dependencies it may take some time to deploy the first time. After the initial deployment, any change that does not touch your dependencies should show up immediately.
8. Once your app URL it's ready, that's it — you're done! Your app now has a permanent URL that you can share with others. Congrats!


# Built With

* [Python](https://docs.python.org/3/) - Programming language
* [Streamlit](https://streamlit.io/) - Web app framework 


# Author

* **Maximiliano Diaz Battan** 
