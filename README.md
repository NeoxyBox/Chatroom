# Chatroom | A basic "socket" based chatroom

![License: GPL v3](https://img.shields.io/github/license/NeoxyBox/Chatroom)
![Coding](https://img.shields.io/github/languages/top/NeoxyBox/Chatroom)
![Size](https://img.shields.io/github/languages/code-size/NeoxyBox/Chatroom)
![Colorama](https://img.shields.io/pypi/v/colorama)
![Observatory_Grade](https://img.shields.io/mozilla-observatory/grade/github.com?publish)
![commit_acitivity](https://img.shields.io/github/commit-activity/w/NeoxyBox/Chatroom)
![pyapi_format](https://img.shields.io/pypi/format/colorama)

*Forked from [Kerxunos](https://github.com/Kerxunos/Chatroom)*

![Chatroom2](https://user-images.githubusercontent.com/113096235/195297547-76ce4d07-80ef-4705-a112-24c373ced67b.png)

**Reminder:** This tool educational purposes only, the developer does not take any responsibility.

## Installation

```bash
git clone https://github.com/NeoxyBox/Chatroom
```

## Log files

Log files are created in the path of the executable.

## Role System | WIP

### Admin role
1. `Admin` has all permissions.
2. `Admin` can assign roles.
4. `Admin` can not change roles of other admins.
5. Server's role is `Admin` by default.

### Default role
1. `Default` role can only read/write messages.
2. Client's role is `Default` by default.

### Custom roles
1. Custom roles can not assign roles.
2. Custom roles can read/write messages by default.

## Command Set

Commands starts with  `su!` (or your custom prefix.)

- `client_ip <client_id>`
- `kick <client_id>`
- `shutdown -t <miliseconds>`
- `clear`
- `add_command <file_path>`

## Roadmap

- [x] Update the program 
- [x] Add new features 
- [x] Make README.md better
- [ ] Add localization system
- [ ] Debug the program

<3
