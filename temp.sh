touch .gitignore
echo .DS_Store >> .gitignore
echo *.__pycache__ >> .gitignore
git add .
git commit -m "Updated .gitignore"
git push
