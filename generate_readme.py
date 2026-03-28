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
        repos_details.append((
            repo.name,
            repo.html_url,
            repo.description or "",
            repo.stargazers_count,
            repo.language or "",
        ))

# Sort repos by stars descending
repos_details.sort(key=lambda x: x[3], reverse=True)

languages_sorted = sorted(languages.items(), key=lambda item: item[1], reverse=True)


def truncate(text, limit):
    """Truncate text at a word boundary."""
    if len(text) <= limit:
        return text
    truncated = text[:limit]
    last_space = truncated.rfind(" ")
    if last_space > limit // 2:
        truncated = truncated[:last_space]
    return truncated.rstrip(".,;:") + "..."


# --- Build README ---

readme = """\
<h1 align="center">dag</h1>
<p align="center">
  <em>Security researcher & developer building tools for hardware hacking, penetration testing, and embedded systems.</em>
</p>

<p align="center">
  <a href="https://github.com/dagnazty?tab=followers">
    <img src="https://img.shields.io/github/followers/dagnazty?label=Followers&style=social" alt="GitHub Followers" />
  </a>
  <a href="https://github.com/dagnazty?tab=repositories">
    <img src="https://img.shields.io/badge/Repos-{repo_count}-blue?style=flat" alt="Repos" />
  </a>
</p>

---

## About

I build security tools, firmware, and utilities focused on **Flipper Zero**, **M5Stack devices**, **ESP32**, and **WiFi security research**. Most of my work lives at the intersection of hardware hacking, embedded development, and offensive security tooling.

---

## Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=dagnazty&show_icons=true&theme=github_dark&hide_border=true&count_private=true" height="170" />
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=dagnazty&theme=github-dark-blue&hide_border=true" height="170" />
</p>

---

## Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white" alt="C" />
  <img src="https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white" alt="C++" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
  <img src="https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white" alt="PowerShell" />
  <img src="https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML" />
  <img src="https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white" alt="Bash" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Arduino-00979D?style=for-the-badge&logo=arduino&logoColor=white" alt="Arduino" />
</p>

""".format(repo_count=len(repos_details))

# --- Featured Projects (top repos by stars, minimum 5 stars) ---

featured = [r for r in repos_details if r[3] >= 5]
featured_names = {r[0] for r in featured}

if featured:
    readme += """---

## Featured Projects

| Project | Description | Stars |
|---------|-------------|:-----:|
"""
    for name, url, description, stars, lang in featured:
        lang_badge = f" `{lang}`" if lang else ""
        desc = truncate(description, 110) if description else "—"
        readme += f"| **[{name}]({url})**{lang_badge} | {desc} | {stars} |\n"

# --- Other Repositories (exclude featured) ---

other_repos = [r for r in repos_details if r[0] not in featured_names]

if other_repos:
    readme += """
---

## Other Repositories

| Repository | Description | Stars | Language |
|------------|-------------|:-----:|----------|
"""
    for name, url, description, stars, lang in other_repos:
        lang_display = f"`{lang}`" if lang else "—"
        desc = truncate(description, 90) if description else "—"
        readme += f"| [{name}]({url}) | {desc} | {stars} | {lang_display} |\n"

# --- Activity Graph ---

readme += """
---

## Activity

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=dagnazty&theme=github-compact&hide_border=true" alt="Activity Graph" />
</p>

---

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=dagnazty&style=flat-square&color=blue" alt="Profile Views" />
</p>
"""

with open("README.md", "w") as readme_file:
    readme_file.write(readme)
