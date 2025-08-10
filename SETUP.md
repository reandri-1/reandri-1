# 🚀 Setup Guide for Your GitHub Profile

## 📋 Prerequisites

1. **GitHub Account**: Make sure you have a GitHub account
2. **Repository**: Create a new repository with the same name as your GitHub username
3. **Secrets**: Set up required secrets in your repository

## 🔧 Installation Steps

### 1. Create Repository
1. Go to [GitHub](https://github.com/new)
2. Create a new repository with the **exact same name** as your GitHub username
3. Make it **public**
4. Initialize with README (optional)

### 2. Upload Files
Upload all the files from this folder to your new repository:
- `README.md`
- `.github/workflows/update-stats.yml`
- `.github/scripts/update-readme.js`
- `package.json`
- `config.json`

### 3. Set Up Secrets
Go to your repository → Settings → Secrets and variables → Actions → New repository secret:

#### Required Secrets:
- `INSTAGRAM_USERNAME`: Your Instagram username
- `INSTAGRAM_PASSWORD`: Your Instagram password (for API access)

#### Optional Secrets:
- `GITHUB_TOKEN`: Automatically provided by GitHub

### 4. Customize Your Profile

#### Update `config.json`:
```json
{
  "social": {
    "instagram": {
      "username": "YOUR_ACTUAL_INSTAGRAM_USERNAME"
    },
    "twitter": {
      "username": "YOUR_TWITTER_USERNAME"
    },
    "linkedin": {
      "username": "YOUR_LINKEDIN_USERNAME"
    }
  }
}
```

#### Update `README.md`:
- Replace `YOUR_USERNAME` with your actual usernames
- Update the gaming stats (AR level, rank, etc.)
- Modify the tech stack badges as needed

### 5. Enable Actions
1. Go to your repository → Actions tab
2. Enable GitHub Actions if prompted
3. The workflow will run automatically every 6 hours

## 🎮 Customization Options

### Gaming Section
Update your gaming stats in README.md:
- **Genshin Impact**: Change AR level, server, characters
- **COD Mobile**: Update your rank and stats
- **Valorant**: Add your current rank and main agents

### Tech Stack
Add or remove badges based on your actual skills:
- Languages you're learning
- Frameworks you use
- Tools you're familiar with

### Colors & Themes
Change the color scheme by modifying:
- Badge colors in README.md
- Stats card themes (change `theme=radical` to other themes)
- Typing animation colors

## 📊 Real-time Stats Setup

### Instagram Followers
The Instagram followers count requires:
1. Instagram Basic Display API access
2. Or use a third-party service like [Social Blade](https://socialblade.com)

### Alternative for Instagram
Replace the Instagram badge with:
```markdown
![Instagram](https://img.shields.io/badge/Instagram-1k%20Followers-E4405F?style=for-the-badge&logo=instagram&logoColor=white)
```

## 🔄 Manual Updates

To manually trigger an update:
1. Go to Actions tab in your repository
2. Select "Update README Stats"
3. Click "Run workflow"

## 🐛 Troubleshooting

### Common Issues:
1. **Stats not updating**: Check if the workflow is running in Actions tab
2. **Instagram not showing**: Instagram has strict API limits, consider using mock values
3. **Badges broken**: Check if the username is correct in all URLs

### Debug Steps:
1. Check Actions logs for errors
2. Verify all secrets are set correctly
3. Ensure repository name matches GitHub username

## 🎨 Available Themes

For GitHub stats cards, you can use these themes:
- `radical` (current)
- `dark`
- `merko`
- `gruvbox`
- `tokyonight`
- `onedark`
- `cobalt`
- `synthwave`
- `highcontrast`

## 📞 Support

If you need help:
1. Check the [GitHub Profile README Guide](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme)
2. Open an issue in your repository
3. Join Discord communities for GitHub profiles

---

**Happy coding! 🚀**
