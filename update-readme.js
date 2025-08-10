const fs = require('fs');
const axios = require('axios');

// Function to update Instagram followers
async function updateInstagramFollowers() {
    try {
        // Note: This is a placeholder - you'll need to use Instagram's API or a service
        // For now, we'll use a mock value that you can manually update
        const mockFollowers = 1000; // Replace with actual API call
        
        let readme = fs.readFileSync('README.md', 'utf8');
        
        // Update Instagram followers badge
        const instagramBadge = `![Instagram Followers](https://img.shields.io/badge/Followers-${mockFollowers}-E4405F?style=for-the-badge&logo=instagram&logoColor=white)`;
        
        readme = readme.replace(
            /!\[Instagram Followers\]\(https:\/\/img\.shields\.io\/badge\/Followers-.*?-E4405F.*?logo=instagram.*?\)/g,
            instagramBadge
        );
        
        fs.writeFileSync('README.md', readme);
        console.log('Updated Instagram followers:', mockFollowers);
    } catch (error) {
        console.error('Error updating Instagram followers:', error);
    }
}

// Function to update GitHub stats
async function updateGitHubStats() {
    try {
        const username = process.env.GITHUB_REPOSITORY_OWNER || 'Reandri-1';
        
        // GitHub stats are automatically updated by the shields.io badges
        console.log('GitHub stats are handled by shields.io badges');
        
    } catch (error) {
        console.error('Error updating GitHub stats:', error);
    }
}

// Main function
async function main() {
    console.log('Starting README update...');
    await updateGitHubStats();
    await updateInstagramFollowers();
    console.log('README update completed!');
}

main().catch(console.error);
