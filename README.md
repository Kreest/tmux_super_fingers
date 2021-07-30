# Tmux Super Fingers [![Tmux Super Fingers](https://github.com/artemave/tmux_super_fingers/actions/workflows/python-app.yml/badge.svg)](https://github.com/artemave/tmux_super_fingers/actions/workflows/python-app.yml)


<img width="300" src="https://78.media.tumblr.com/e1712952f6eb24f418a997a8da6ae831/tumblr_ou1znif6LW1w4t58uo1_500.gif" />

A tmux "mode" that allows you to open file links in an `$EDITOR`, urls in the browser and more.


<details>
  <summary>Demo</summary>

  https://user-images.githubusercontent.com/23721/127636969-6c7785b9-d749-416a-ad5d-275fb38e00e0.mp4
</details>

## Description

Tmux [fingers](https://github.com/morantron/tmux-fingers) plugin introduced the "fingers" mode, where particularly looking chunks of text (e.g. file paths) are highlighted and assigned a "mark". When user hits a mark key, the highlighted text gets copied to clipboard.

Super Fingers extends this idea. Notably:

- it opens files in a terminal `$EDITOR` running elsewhere within the same tmux session* (for gui `$EDITOR`s, it'll simply call OS open)
- only files paths that actually exist are highlighted
- it opens files at line number
- text that isn't a file path, but maps onto one (e.g. `UsersController#show` in rails log or `+++ b/app/models/user.rb` in a diff) is also highlighted
- it opens different types of marks differently: text files are sent to editor, urls and images to OS open, etc.

\* _if no running terminal `$EDITOR` is found in the session, plugin attempts to start one in a new window._

### Secondary action

If you press <kbd>alt</kbd> when choosing a mark, highlighted text is copied into clipboard instead.

## Install

Requires python3.

Use [TPM](https://github.com/tmux-plugins/tpm):

    set -g @plugin 'artemave/tmux_super_fingers'
    
Hit <kbd>prefix</kbd> + <kbd>I</kbd> to fetch and source the plugin.

## Configuration

#### @super-fingers-key

Customize how to enter fingers mode. Always preceded by prefix: `prefix + @super-fingers-key`. Defaults to `f`.

```
set -g @super-fingers-key f
```

## TODO

- [ ] generic, configurable/pluggable way to send highlited text to arbitrary target (not just `vim` and `xdg-open`)
- [ ] search marks
- [ ] secondary action
- [x] configurable `@super-fingers-key`
- [x] create vim window if there are none in the session
- [ ] extract untested code into tested packages
- [ ] python stack traces (line numbers)
