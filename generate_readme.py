from github import Github
import os

token = os.getenv('GITHUB_TOKEN')
g = Github(token)

username = "dagnazty"
user = g.get_user(username)
languages = {}
repos_details = []

for repo in user.get_repos():
    if repo.language:
        if repo.language in languages:
            languages[repo.language] += 1
        else:
            languages[repo.language] = 1

    if not repo.fork:
        repos_details.append((repo.name, repo.html_url, repo.description or "No description provided.", repo.stargazers_count, repo.language or "N/A"))

languages_sorted = {k: v for k, v in sorted(languages.items(), key=lambda item: item[1], reverse=True)}

readme_contents = """
<div>
  <a href="https://github.com/dagnazty"><img align="left" src="https://github-readme-stats.vercel.app/api?username=dagnazty&show_icons=true&theme=radical" /></a>
</div>

| Language   | Repositories |
|------------|--------------|
"""

for language, count in languages_sorted.items():
    readme_contents += f"| {language} | {count} |\n"

readme_contents += """
<br clear="left"/>

## Repositories I've Worked On

| Repository | Description | Stars | Main Language |
|------------|-------------|-------|---------------|
"""

for name, url, description, stars, main_language in repos_details:
    stars_formatted = f"⭐{stars}"
    if main_language: 
         language_badge_url = f"https://img.shields.io/badge/-{main_language.replace(' ', '_')}-informational?style=for-the-badge&logo={main_language.replace(' ', '').lower()}&logoColor=white"
        main_language_badge = f"![{main_language}]({language_badge_url})"
    else:
        main_language_badge = "N/A"
    
    readme_contents += f"| [{name}]({url}) | {description} | {stars_formatted} | {main_language_badge} |\n"


readme_contents += """
## My GitHub Activity

![github activity graph](https://github-readme-activity-graph.vercel.app/graph?username=dagnazty&theme=high-contrast)

<img src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" /> <img src="https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="JavaScript" /> <img src="https://img.shields.io/badge/-PowerShell-5391FE?style=flat-square&logo=powershell&logoColor=white" alt="PowerShell" /> <img src="https://img.shields.io/badge/-C-00599C?style=flat-square&logo=c&logoColor=white" alt="C" /> <img src="https://img.shields.io/badge/-C++-00599C?style=flat-square&logo=c%2B%2B&logoColor=white" alt="C++" /> <img src="https://img.shields.io/badge/-Batch-4D4D4D?style=flat-square&logo=windows&logoColor=white" alt="Batch" /> <img src="https://img.shields.io/badge/-Bash-4EAA25?style=flat-square&logo=gnu-bash&logoColor=white" alt="Bash" /> <img src="https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask" /> <img src="https://img.shields.io/badge/-PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" /> <img src="https://img.shields.io/badge/-HTML-E34F26?style=flat-square&logo=html5&logoColor=white" alt="HTML" />
"""

with open("README.md", "w") as readme_file:
    readme_file.write(readme_contents)
