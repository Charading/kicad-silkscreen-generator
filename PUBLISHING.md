# Publishing to GitHub and KiCad Plugin Manager

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `kicad-silkscreen-generator`
3. Description: "KiCad plugin to duplicate and increment silkscreen labels"
4. Make it **Public** (required for KiCad Plugin Manager)
5. **Don't** initialize with README (we already have one)
6. Click "Create repository"

## Step 2: Push Your Code to GitHub

Run these commands in PowerShell:

```powershell
cd "X:\VS Code\kicad-silkscreen-generator"

# Initialize git repo
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Silkscreen Label Generator v1.0.0"

# Add your GitHub repo as remote (replace 'yourusername' with your GitHub username)
git remote add origin https://github.com/yourusername/kicad-silkscreen-generator.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 3: Update URLs in Files

After creating your GitHub repo, replace `yourusername` in these files:
- `metadata.json`
- `repository.json`

## Step 4: Create a Release Package

1. Create the plugin ZIP file:

```powershell
cd "X:\VS Code\kicad-silkscreen-generator"

# Create a clean ZIP (exclude dev files)
$files = @(
    "__init__.py",
    "silkscreen_generator.py",
    "dialog.py",
    "metadata.json",
    "icon.png",
    "README.md",
    "LICENSE"
)

Compress-Archive -Path $files -DestinationPath "kicad-silkscreen-generator-1.0.0.zip" -Force
```

2. Calculate the SHA256 hash:

```powershell
Get-FileHash "kicad-silkscreen-generator-1.0.0.zip" -Algorithm SHA256 | Select-Object -ExpandProperty Hash
```

3. Get file sizes:

```powershell
$zip = Get-Item "kicad-silkscreen-generator-1.0.0.zip"
Write-Host "Download size: $($zip.Length) bytes"
```

## Step 5: Create GitHub Release

1. Go to your GitHub repo
2. Click "Releases" → "Create a new release"
3. Tag version: `v1.0.0`
4. Release title: `v1.0.0 - Initial Release`
5. Description:
   ```
   Initial release of KiCad Silkscreen Label Generator
   
   Features:
   - Automatic number incrementing for silkscreen labels
   - Custom X/Y offsets for precise positioning
   - Remembers last used settings
   - Perfect for pin headers and connectors
   ```
6. Upload the `kicad-silkscreen-generator-1.0.0.zip` file
7. Click "Publish release"

## Step 6: Update metadata.json with Real Values

After creating the release:

1. Copy the download URL from GitHub release
2. Update `metadata.json` and `repository.json`:
   - Replace `download_url` with the actual release ZIP URL
   - Replace `download_sha256` with the hash from Step 4
   - Replace `download_size` with the actual size in bytes
   - Update `install_size` (usually about 2x the ZIP size)

3. Commit and push the changes:

```powershell
git add metadata.json repository.json
git commit -m "Update metadata with release info"
git push
```

## Step 7: Enable GitHub Pages (for repository.json)

To make your plugin discoverable in KiCad:

1. Go to your repo Settings → Pages
2. Source: "Deploy from a branch"
3. Branch: `main` / `root`
4. Save

5. Update `repository.json` with the GitHub Pages URL and push it to the repo

Your repository URL will be:
```
https://yourusername.github.io/kicad-silkscreen-generator/repository.json
```

## Step 8: Add Repository to KiCad

Users can now add your plugin repository:

1. Open KiCad PCB Editor
2. Tools → Plugin and Content Manager
3. Click "Manage Repositories" (gear icon)
4. Click "+" to add a new repository
5. Name: "Silkscreen Label Generator"
6. URL: `https://yourusername.github.io/kicad-silkscreen-generator/repository.json`
7. Click "Save"
8. Close and refresh
9. Your plugin will appear in the list!

## Alternative: Manual Installation (Current Method)

Users can also install manually:

1. Download the ZIP from releases
2. In KiCad: Tools → Plugin and Content Manager
3. Click "Install from File..."
4. Select the downloaded ZIP

## Updating Your Plugin

When you make changes:

1. Update version number in `metadata.json` and `repository.json`
2. Create new ZIP with new version number
3. Create new GitHub release
4. Update metadata files with new release info
5. Push changes

---

**Note:** Replace `yourusername` with your actual GitHub username everywhere!
