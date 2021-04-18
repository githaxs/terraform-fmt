# Terraform Format

Fill me out


### Installation
1. Install the [Githaxs Meta Application](https://github.com/apps/githaxs-meta)

2. Create a repo with the name `githaxs_settings`.

3. Add the following to `ghx.yml` within the repo:

```yaml
# githaxs_settings/ghx.yml

terraform-fmt:
  # install on all repos
  org: true
  # install on select repos
  repos:
    - api-microservice
    - websiteservice
  # install on repos with a given topic
  repo_topics:
    - api
    - web
```
### Configuration

|parameter|description|required|
|---|---|---|
|foo|bar| |

### Example Configurations

To configure global settings:

```yaml
# githaxs_settings/ghx.yml

terraform-fmt:
  org: true
  org_settings:
    # Cannot be overriden by repo specific settings
    final:
      foo:
    # Default value if repo specific settings do not exist
    default:
      foo:
   ```

To configure repo specific settings:

```yaml
# <repo name>/ghx.yml

terraform-fmt:
  repo_settings:
    foo:
  ```
