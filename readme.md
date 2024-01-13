
## Urls

WebPage: https://some-developer-somewhere-some-streamlit-apps-app-1aye6g.streamlit.app/

Public GitHub repo: https://github.com/Some-Developer-Somewhere/Some-Streamlit-apps

## Setup, etc

### Install Streamlit

> python -m pip install streamlit

### Run from terminal

> streamlit run app.py

### Deploying the app

**Prerequisits**

A preferable pre-requisit is some basic knowledge of how to use GIT. **Maybe a workaround can be found**.

**Deploying**

1. Create a public GitHub repo
2. Clone the GitHub repo down to your machine
    ```
    Cloning a repo. Add ".git":
    
    Example: "https://github.com/your_github_account/your_github_repo" + ".git"

    Clone:
    > git clone https://github.com/your_github_account/your_github_repo.git
    
    ```
3. Develop the app locally to a working version (only 2 lines of code required)
4. Push the changes to the GitHub repo
    - > git add --all
    - > git commit -a -m "This is a description of what I added/committed"
    - > git push
5. Deploying the first time
    - You should have working code in a public GitHub repo
    - Run the app locally and find the deploy button in the running app. Then follow the instructions to let Streamlit point to your GitHub repo
        - > streamlit run app.py

**Deploying new versions**

1. Make changes and test locally
2. push updates using git (Step 4. above)
3. The site/webpage should now be updated (As it is loaded directly from your GitHub repo)


## Using AI to generate streamlit

When asking ChatGPT to make streamlit code, it might give you syntax like the following:
- > st. ..._experimental()
and
- > st. ..._beta()

Just tell GPT something like the following to fix it, or just remove the "_beta" and "_experimental" text:

"I am using a newer verion of streamlit where "the functions are no longer "beta" or "experimental" please remove this from the function names.
