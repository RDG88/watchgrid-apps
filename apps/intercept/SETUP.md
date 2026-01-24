# Setup Instructions

## 1. Create GitHub Repository

Create a new GitHub repository named `watchgrid-apps-intercept` (or your preferred name).

## 2. Initialize Git and Push

From the `/Users/rob/Documents/suitcase/watchgrid-apps/apps/intercept` directory:

```bash
cd /Users/rob/Documents/suitcase/watchgrid-apps/apps/intercept

# Initialize git repository
git init
git add .
git commit -m "Initial commit: iNTERCEPT watchgrid app"

# Add your GitHub repository as remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/watchgrid-apps-intercept.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## 3. Enable GitHub Packages

The GitHub Actions workflow will automatically:
- Build the Docker image on every push to main
- Push it to GitHub Container Registry (ghcr.io)
- Tag it with `latest` and version tags

No additional setup needed - the workflow uses `GITHUB_TOKEN` which is automatically available.

## 4. Update Deployment

After pushing to GitHub, update the image reference in `deployment.yaml`:

Replace `YOUR_GITHUB_USERNAME` with your actual GitHub username:
```yaml
image: ghcr.io/YOUR_GITHUB_USERNAME/watchgrid-apps-intercept:latest
```

## 5. Make Image Public (Optional)

If you want the image to be publicly accessible:

1. Go to your repository on GitHub
2. Click on "Packages" in the right sidebar
3. Click on the package name
4. Click "Package settings"
5. Scroll down to "Danger Zone"
6. Click "Change visibility" and select "Public"

## 6. Using Private Images (If kept private)

If keeping the image private, you'll need to create an image pull secret in Kubernetes:

```bash
kubectl create secret docker-registry ghcr-secret \
  --docker-server=ghcr.io \
  --docker-username=YOUR_GITHUB_USERNAME \
  --docker-password=YOUR_GITHUB_TOKEN \
  --docker-email=YOUR_EMAIL
```

Then add to deployment.yaml:
```yaml
spec:
  imagePullSecrets:
    - name: ghcr-secret
```

## Building the Image

Once you push to GitHub, the workflow will automatically build and push the image. You can monitor the build progress in the "Actions" tab of your GitHub repository.

The image will be available at:
```
ghcr.io/YOUR_GITHUB_USERNAME/watchgrid-apps-intercept:latest
```
