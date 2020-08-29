# Reaktor2020-junior-dev-pre-assignment
My submission for Pre-assignment for junior developer positions @ [Reaktor](https://www.reaktor.com/).

https://mlindholm-reaktor-assignment.herokuapp.com/

## Instructions
https://www.reaktor.com/junior-dev-assignment/

On a Debian and Ubuntu systems, there is a file called /var/lib/dpkg/status that holds information about software packages that the system knows about. Write a small program in a programming language of your choice that exposes some key information about packages in the file via an HTML interface.

- The index page lists installed packages alphabetically with package names as links.
- When following each link, you arrive at a piece of information about a single package. The following information should be included:
  * Name
  * Description
  * The names of the packages the current package depends on (skip version numbers)
  * Reverse dependencies, i.e. the names of the packages that depend on the current package
- The dependencies and reverse dependencies should be clickable and the user can navigate the package structure by clicking from package to package.
- The application must be available publicly on the internet. You can, for example, use Heroku to host it for free. Provide a link to the website in your job application.
- The source code must also be available publicly in GitLab or GitHub, and a link provided in your job application.

## Solution

_Stack: Python + Flask(render_template) + Jinja2 deployed to Heroku._

- I'm using nested global dict to store the parsed info.
- Sorting the data in Jinja with sort / dictsort.
- If the required path does not exist this app uses mock_data provided in the assignment instead.

## Afterthoughts/Improvements

- Perhaps using OOP where each package is a object would have been better solution.
- Creating list for reverse dependencies to avoid nested double for-loops in Jinja.
- The obvious lack of frontend.

## Todo

- [x] fix alphabetical problems
