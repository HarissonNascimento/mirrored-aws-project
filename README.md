## Mirror configuration

#### First step
After executing ```terraform apply``` in the [aws-infra](https://github.com/HarissonNascimento/aws-infra) repository.


In this repository, go to **Settings > Secrets and variables > Actions** and check if ```CODECOMMIT_SSH_PRIVATE_KEY``` and ```CODECOMMIT_SSH_PRIVATE_KEY_ID``` secrets are set


<img src="./.github/images/edit-repository-secret.png">


#### Second Step


See the output variable ```codecommit_ssh_url``` and copy the value.


<img src="./.github/images/codecommit-ssh-url-example.png">


If necessary, in the [worflow mirror file](./.github/workflows/mirror.yml) edit the ```target_repo_url``` variable with ```codecommit_ssh_url``` copied value.

Example:

```
...
with:
    target_repo_url: ssh://git-codecommit.sa-east-1.amazonaws.com/v1/repos/mirrored-aws-project
...
```

#### Third step


Check the “Actions” tab of the repository to verify that the workflow was triggered and the workflow run was successful.

<img src="./.github/images/workflow-triggered.png">

---