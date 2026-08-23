# GitHub Sync

This project is connected to the existing GitHub repository:

```bash
https://github.com/cys9689/AI-ML-Interview-Preparation.git
```

Local branch tracking:

```bash
main -> origin/main
```

Daily update workflow:

```bash
git status
git add .
git commit -m "Add practice notes for YYYY-MM-DD"
git push
```

If `git push` reports `Invalid username or token`, authenticate GitHub first.
Recommended options:

```bash
# Option 1: install GitHub CLI, then login
brew install gh
gh auth login
```

```bash
# Option 2: keep HTTPS and use a GitHub personal access token when prompted
git push
```

```bash
# Option 3: configure an SSH key in GitHub, then switch the remote
git remote set-url origin git@github.com:cys9689/AI-ML-Interview-Preparation.git
git push
```
