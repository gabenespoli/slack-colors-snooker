# Snooker Colors for Slack

This tool is based on [this gist](https://gist.github.com/a7madgamal/c2ce04dde8520f426005e5ed28da8608) for making a dark mode on Slack for macOS. I made a simple python script to replace the color hexes with colors from [my snooker theme](https://github.com/gabenespoli/vim-colors-snooker). The file `black.css` is from the gist, and `snooker.css` is the same with the hexes replaced.

If you want to create your own theme, edit `color_snooker.csv` with your own color hexes.

## Instructions

These instructions are copied from [this gist](https://gist.github.com/a7madgamal/c2ce04dde8520f426005e5ed28da8608), and amended to include the url of the snooker theme in this repo.

1. Close slack

2. Open this file /Applications/Slack.app/Contents/Resources/app.asar.unpacked/src/static/ssb-interop.js

3. Append this to it

```
document.addEventListener('DOMContentLoaded', function() {
 $.ajax({
   url: 'https://raw.githubusercontent.com/gabenespoli/slack-colors-snooker/master/snooker.css',
   success: function(css) {
     $("<style></style>").appendTo('head').html(css);
   }
 });
});
```

4. Open slack and enjoy the darkness!
