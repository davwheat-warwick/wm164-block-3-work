# WM164 Smart Solutions Development I / Block 3 / Monday

## Version control terminology

| Terminology     | Definition                                                                               |
| --------------- | ---------------------------------------------------------------------------------------- |
| Version control | The process of tracking versions of files through time.                                  |
| Distributed     | Stored in multiple locations.                                                            |
| Check out       | Moving the HEAD to a new location (i.e. new branch).                                     |
| Commit          | Saving a new version of file(s), optionally with a comment                               |
| Repository      | A server which stores all commits, and tracks pointers to these commits (branches, tags) |
| Staging area    | Changes here will be saved upon the next commit.                                         |
| Timeline        | A list of all commits from the HEAD, in reverse chronological order (old to new).        |

## Homework

### What is open source software?

Open source software is software developed with its source code public for anyone to see. This is usually done alongside a version control system, like Git, with a public hosting platform for this (such as GitHub or GitLab).

These are typically (but not always) licensed under 'copyleft' and permissive licenses which allow others to make copies and

### Branches

**What is a branch?**

A branch is a way to develop on top of a specific commit in parallel to other developers.

This allows one developer to work on implementing a feature on a branch named `feature1` while another works on another feature on the `feature2` branch.

Neither tree affects the other, and other commits can still be made to the `main` branch whilst the feature branches are being worked on.

When the code on a branch is ready, it can be merged into another branch. For example, when `feature1` is complete, you can merge it into the `main` branch. This preserves all the commits from within `feature1`, while transferring the changes to the `main` branch.

**How do we get to this history graph?**

![](./git%20tree.svg)

Commands:

```
git commit
git commit
git checkout -b feature1
git commit
git commit
git checkout main
git commit
git commit
git merge feature1
git commit
git checkout feature1
git commit
git commit
```
