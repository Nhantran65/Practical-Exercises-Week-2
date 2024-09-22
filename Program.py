from pydriller import Repository
import json
from datetime import datetime

# GitHub API data (directly in the script)
github_data = {
  "id": 123394155,
  "node_id": "MDEwOlJlcG9zaXRvcnkxMjMzOTQxNTU=",
  "name": "scc",
  "full_name": "boyter/scc",
  "private": False,
  "owner": {
    "login": "boyter",
    "id": 612151,
    "node_id": "MDQ6VXNlcjYxMjE1MQ==",
    "avatar_url": "https://avatars.githubusercontent.com/u/612151?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/boyter",
    "html_url": "https://github.com/boyter",
    "followers_url": "https://api.github.com/users/boyter/followers",
    "following_url": "https://api.github.com/users/boyter/following{/other_user}",
    "gists_url": "https://api.github.com/users/boyter/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/boyter/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/boyter/subscriptions",
    "organizations_url": "https://api.github.com/users/boyter/orgs",
    "repos_url": "https://api.github.com/users/boyter/repos",
    "events_url": "https://api.github.com/users/boyter/events{/privacy}",
    "received_events_url": "https://api.github.com/users/boyter/received_events",
    "type": "User",
    "site_admin": False
  },
  "html_url": "https://github.com/boyter/scc",
  "description": "Sloc, Cloc and Code: scc is a very fast accurate code counter with complexity calculations and COCOMO estimates written in pure Go",
  "fork": False,
  "url": "https://api.github.com/repos/boyter/scc",
  "forks_url": "https://api.github.com/repos/boyter/scc/forks",
  "keys_url": "https://api.github.com/repos/boyter/scc/keys{/key_id}",
  "collaborators_url": "https://api.github.com/repos/boyter/scc/collaborators{/collaborator}",
  "teams_url": "https://api.github.com/repos/boyter/scc/teams",
  "hooks_url": "https://api.github.com/repos/boyter/scc/hooks",
  "issue_events_url": "https://api.github.com/repos/boyter/scc/issues/events{/number}",
  "events_url": "https://api.github.com/repos/boyter/scc/events",
  "assignees_url": "https://api.github.com/repos/boyter/scc/assignees{/user}",
  "branches_url": "https://api.github.com/repos/boyter/scc/branches{/branch}",
  "tags_url": "https://api.github.com/repos/boyter/scc/tags",
  "blobs_url": "https://api.github.com/repos/boyter/scc/git/blobs{/sha}",
  "git_tags_url": "https://api.github.com/repos/boyter/scc/git/tags{/sha}",
  "git_refs_url": "https://api.github.com/repos/boyter/scc/git/refs{/sha}",
  "trees_url": "https://api.github.com/repos/boyter/scc/git/trees{/sha}",
  "statuses_url": "https://api.github.com/repos/boyter/scc/statuses/{sha}",
  "languages_url": "https://api.github.com/repos/boyter/scc/languages",
  "stargazers_url": "https://api.github.com/repos/boyter/scc/stargazers",
  "contributors_url": "https://api.github.com/repos/boyter/scc/contributors",
  "subscribers_url": "https://api.github.com/repos/boyter/scc/subscribers",
  "subscription_url": "https://api.github.com/repos/boyter/scc/subscription",
  "commits_url": "https://api.github.com/repos/boyter/scc/commits{/sha}",
  "git_commits_url": "https://api.github.com/repos/boyter/scc/git/commits{/sha}",
  "comments_url": "https://api.github.com/repos/boyter/scc/comments{/number}",
  "issue_comment_url": "https://api.github.com/repos/boyter/scc/issues/comments{/number}",
  "contents_url": "https://api.github.com/repos/boyter/scc/contents/{+path}",
  "compare_url": "https://api.github.com/repos/boyter/scc/compare/{base}...{head}",
  "merges_url": "https://api.github.com/repos/boyter/scc/merges",
  "archive_url": "https://api.github.com/repos/boyter/scc/{archive_format}{/ref}",
  "downloads_url": "https://api.github.com/repos/boyter/scc/downloads",
  "issues_url": "https://api.github.com/repos/boyter/scc/issues{/number}",
  "pulls_url": "https://api.github.com/repos/boyter/scc/pulls{/number}",
  "milestones_url": "https://api.github.com/repos/boyter/scc/milestones{/number}",
  "notifications_url": "https://api.github.com/repos/boyter/scc/notifications{?since,all,participating}",
  "labels_url": "https://api.github.com/repos/boyter/scc/labels{/name}",
  "releases_url": "https://api.github.com/repos/boyter/scc/releases{/id}",
  "deployments_url": "https://api.github.com/repos/boyter/scc/deployments",
  "created_at": "2018-03-01T06:44:25Z",
  "updated_at": "2024-09-21T09:00:09Z",
  "pushed_at": "2024-09-10T22:58:24Z",
  "git_url": "git://github.com/boyter/scc.git",
  "ssh_url": "git@github.com:boyter/scc.git",
  "clone_url": "https://github.com/boyter/scc.git",
  "svn_url": "https://github.com/boyter/scc",
  "homepage": "",
  "size": 12066,
  "stargazers_count": 6533,
  "watchers_count": 6533,
  "language": "Go",
  "has_issues": True,
  "has_projects": True,
  "has_downloads": True,
  "has_wiki": True,
  "has_pages": False,
  "has_discussions": True,
  "forks_count": 255,
  "archived": False,
  "disabled": False,
  "open_issues_count": 46,
  "license": {
    "key": "mit",
    "name": "MIT License",
    "spdx_id": "MIT",
    "url": "https://api.github.com/licenses/mit",
    "node_id": "MDc6TGljZW5zZTEz"
  },
  "allow_forking": True,
  "is_template": False,
  "web_commit_signoff_required": False,
  "topics": [
    "cli",
    "cloc",
    "code",
    "complexity",
    "golang",
    "linux",
    "macos",
    "sloc",
    "sloccount",
    "statistics",
    "tokei",
    "windows"
  ],
  "visibility": "public",
  "forks": 255,
  "open_issues": 46,
  "watchers": 6533,
  "default_branch": "master",
  "network_count": 255,
  "subscribers_count": 40
}

# Set up the repository
repo_path = "https://github.com/boyter/scc.git"
repo = Repository(repo_path)

try:
    # 1. Get the total count of commits
    commit_count = sum(1 for _ in repo.traverse_commits())
    print(f"Total commits: {commit_count}")

    # 2. Get the total count of developers
    developers = set()
    for commit in repo.traverse_commits():
        developers.add(commit.author.name)
    print(f"Total developers: {len(developers)}")

    # 3. Get the total count of commits in the main branch
    default_branch = github_data["default_branch"]
    main_branch_commits = sum(1 for _ in Repository(repo_path, only_in_branch=default_branch).traverse_commits())
    print(f"Commits in main branch ({default_branch}): {main_branch_commits}")

    # 4. Get the Contributors Experience
    contributor_experience = {}
    for commit in repo.traverse_commits():
        author = commit.author.name
        commit_date = commit.author_date
        if author not in contributor_experience:
            contributor_experience[author] = {
                "first_commit": commit_date,
                "last_commit": commit_date,
                "experience_days": 0
            }
        else:
            contributor_experience[author]["last_commit"] = max(contributor_experience[author]["last_commit"], commit_date)

    for author, data in contributor_experience.items():
        experience = (data["last_commit"] - data["first_commit"]).days
        data["experience_days"] = experience

    # Prepare results
    results = {
        "total_commits": commit_count,
        "total_developers": len(developers),
        "main_branch_commits": main_branch_commits,
        "contributor_experience": contributor_experience,
        "github_api_data": {
            "stargazers_count": github_data["stargazers_count"],
            "forks_count": github_data["forks_count"],
            "open_issues_count": github_data["open_issues_count"],
            "created_at": github_data["created_at"],
            "updated_at": github_data["updated_at"]
        }
    }

    # Save results to a JSON file
    with open("scc_repository_analysis.json", "w") as f:
        json.dump(results, f, indent=2, default=str)

    print("Analysis complete. Results saved to scc_repository_analysis.json")

except Exception as e:
    print(f"An error occurred: {str(e)}")