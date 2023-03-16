import git
import os

repo = git.Repo(search_parent_directories=True)

def parse_commit_log(repo, *params):
    commit = {}
    try:
        log = repo.git.log(*params).split("\n")
    except git.GitCommandError:
        return

    for line in log:
        if line.startswith("    "):
            if not 'message' in commit:
                commit['message'] = ""
            else:
                commit['message'] += "\n"
            commit['message'] += line[4:]
        elif line:
            if 'message' in commit:
                yield commit
                commit = {}
            else:
                field, value = line.split(None, 1)
                commit[field.strip(":")] = value
    if commit:
        yield commit
        
commits = list(parse_commit_log(repo, '/home/jovyan/work/new_kedro/kedro-template-tc-06/etl-pipeline/src/tests'))
print(commits)

repo_path = repo.remotes.origin.url.split('.git')[0]
commit_url = os.path.join(repo_path, '-/commit/', commits[0]['commit'])
print(commit_url)

# https://gitlab.com/storemesh/project-template/data-engineer/kedro-template/kedro-example/kedro-tc-06.git
# https://gitlab.com/storemesh/big-project/ditp65/ditp65-data-pipeline/-/commit/b26e43b48557982a7414c95e3d8a3794c2a45006

# repo = git.Repo(search_parent_directories=True)
# branch = repo.active_branch
# branch_name = branch.name
# hexsha = repo.head.object.hexsha