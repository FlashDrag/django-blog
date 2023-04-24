# I Think Therefore I Blog

## Agile UX
[Agile Project](https://github.com/FlashDrag/agile-project)

### Project Planning
- #### Design Thinking
    - **Empathize**.
    Put yourself in the shoes of the user. What are their needs? What are their pain points? What are their goals?
    - **Questions**.
    Why do you want to build this app? What problem does it solve? What value does it provide? What will make users return to your app?
    - **Examine**.
    What do I want to seee when I visit a blog? What features do I want to see? What features do I not want to see?

### User Stories
- #### GitHub's Kanban board
    _GitHub's Kanban board was used to track user stories_

    [Creating Boards with Github Instructions Sheet](https://docs.google.com/document/d/1VSJtnhh_8djRyncotRzMJG9g_ATfiBHasUVZ1xTwybE/edit#heading=h.hvy9tw74f1o0)

- Create new project board
- Open **Workflows** from the <**...**> menu at the top-right of the board.
- Enable the **Item added to project** workflow by toggling it on. _This enables the automation of moving issues to the **To Do** column when they are added to the project board._
- Link the project board to the repository.
- Create a user stories template:
    - Open the repository's settings.
    - Scroll down to the **Features** section.
    - Click **Set up templates**.
    - Click **Add custom template**:

        | name | about | title | labels | assignees |
        | :------: | :------: | :------: | :------: | :------: |
        | User Story | Issue template for user stories | USER STORY: TITLE | story | @FlashDrag |

        **Description**:

        ```As a **role** I can **capability** so that **received benefit**```

    - Commit the changes (**Propose changes**):
    `Add a new user story template`

- #### User Stories/GitHub Issues
    _Create user stories as GitHub issues using the user stories template and add the issue to the project board._

    - View post list: As a Site User I can view a paginated list of posts so that I can easily select a post to view
    - Open a post: As a Site User I can click on a post so that I can read the full text
    - View likes: As a Site User / Admin I can view the number of likes on each post so that I can see which is the most popular or viral
    - View comments: As a Site User / Admin I can view comments on an individual post so that I can read the conversation
    - Account registration: As a Site User I can register an account so that I can comment and like
    - Comment on a post: As a Site User I can leave comments on a post so that I can be involved in the conversation
    - Like / Unlike: As a Site User I can like or unlike a post so that I can interact with the content
    - Manage posts: As a Site Admin I can create, read, update and delete posts so that I can manage my blog content
    - Create drafts: As a Site Admin I can create draft posts so that I can finish writing the content later
    - Approve comments: As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments

