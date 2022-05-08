# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
from os import path, system
import subprocess

@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(path.expanduser('~', '.config', 'qtile', 'autostart.sh'))])

mod = "mod4"
terminal = guess_terminal()

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # ------------ App Configs ------------

    # Menu
    ([mod], "m", lazy.spawn("rofi -show drun")),

    # Window Nav
    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser
    ([mod], "n", lazy.spawn("google-chrome-stable")),

    #Ranger
    ([mod], "r", lazy.spawn("ranger --show")),

    # File Explorer
    ([mod], "e", lazy.spawn("thunar")),

    # Terminal
    ([mod], "Return", lazy.spawn("tilix")),

    # Visual Studio
    ([mod], "v", lazy.spawn("code")),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 2400")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    ([mod], "s", lazy.spawn("scrot")),
    ([mod, "shift"], "s", lazy.spawn("scrot -s")),

    # ------------ Hardware Configs ------------

    # Volume
    ([mod], "z", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([mod], "x", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([mod], "a", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),
]]

groups = [Group(i) for i in ["爵 WEB",  " DEV", " TERM", " MISC" ]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

layout_conf = {
    'border_focus': '#F07178',
    'border_width': 1,
    'margin': 4
}

layouts = [
    layout.Columns(**layout_conf),
    # layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    layout.TreeTab(**layout_conf),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='UbuntuMono Nerd Font',
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    foreground=[ "#f1ffff", "#f1ffff"] ,
                    background=["#0000003b", "#00000094"],
                    font='UbuntuMono Nerd Font',
                    fontsize=20,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=[ "#f1ffff", "#f1ffff"],
                    inactive= [ "#f1ffff", "#f1ffff"],
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    urgent_border=["#4c566a", "#4c566a"],
                    this_current_screen_border=["#a151d3", "#a151d3"],
                    this_screen_border=["#F07178", "#F07178"],
                    other_current_screen_border=["#0f101a", "#0f101a"],
                    other_screen_border=["#0f101a", "#0f101a"],
                    disable_drag=True ),
                widget.Prompt(),
                widget.WindowName(
                    foreground=[ "#E06C75", "#E06C75"] ,
                    background=["#0f101a", "#0f101a"],
                    font='UbuntuMono Nerd Font Bold',
                    fontsize=20,
                ),
                widget.Systray(),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    background=["#0f101a", "#0f101a"]
                ),
                widget.TextBox(
                    foreground= ["#F07178","#F07178"],
                    background= ["#0f101a", "#0f101a"],
                    text="", # Icon: nf-oct-triangle_left
                    fontsize=40,
                    padding=-3
                ),
                widget.CurrentLayoutIcon(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#F07178", "#F07178"],
                    scale=0.65
                ),
                widget.CurrentLayout(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#F07178", "#F07178"]
                ),#separador de sections.
                widget.TextBox(
                    foreground= ["#a151d3","#a151d3"],
                    background= ["#F07178","#F07178"],
                    text="", # Icon: nf-oct-triangle_left
                    fontsize=37,
                    padding=-3
                ),
                widget.TextBox(
                    padding=5,
                    text=' ',
                    background=["#a151d3", "#a151d3"],
                    foreground=["#0f101a", "#0f101a"],
                ),
                widget.Clock(
                    background=["#a151d3", "#a151d3"],
                    foreground=["#0f101a", "#0f101a"],
                    format='%Y-%m-%d %a %I:%M %p '),
            ],
            25, opacity=0.8
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    foreground=[ "#f1ffff", "#f1ffff"] ,
                    background=["#0f101a", "#0f101a"],
                    font='UbuntuMono Nerd Font',
                    fontsize=19,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=[ "#f1ffff", "#f1ffff"],
                    inactive= [ "#f1ffff", "#f1ffff"],
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    urgent_border=["#4c566a", "#4c566a"],
                    this_current_screen_border=["#a151d3", "#a151d3"],
                    this_screen_border=["#F07178", "#F07178"],
                    other_current_screen_border=["#0f101a", "#0f101a"],
                    other_screen_border=["#0f101a", "#0f101a"],
                    disable_drag=True ),
                widget.Prompt(),
                widget.WindowName(
                    foreground=[ "#E06C75", "#E06C75"] ,
                    background=["#0f101a", "#0f101a"],
                    font='UbuntuMono Nerd Font Bold',
                    fontsize=16,
                ),
                widget.Systray(),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    background=["#0f101a", "#0f101a"]
                ),
                widget.TextBox(
                    foreground= ["#F07178","#F07178"],
                    background= ["#0f101a", "#0f101a"],
                    text="", # Icon: nf-oct-triangle_left
                    fontsize=40,
                    padding=-3
                ),
                widget.CurrentLayoutIcon(
                    padding=5,
                    foreground=["#0f101a", "#0f101a"],
                    background=["#F07178", "#F07178"],
                    scale=0.65
                ),
                widget.CurrentLayout(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#F07178", "#F07178"]
                ),
                widget.TextBox(
                    foreground= ["#a151d3","#a151d3"],
                    background= ["#F07178","#F07178"],
                    text="", # Icon: nf-oct-triangle_left
                    fontsize=37,
                    padding=-3
                ),
                widget.TextBox(
                    padding=5,
                    text=' ',
                    background=["#a151d3", "#a151d3"],
                    foreground=["#0f101a", "#0f101a"],
                ),
                widget.Clock(
                    background=["#a151d3", "#a151d3"],
                    foreground=["#0f101a", "#0f101a"],
                    format='%Y-%m-%d %a %I:%M %p '),
            ],
            25, opacity=0.8
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
], border_focus= "#ffff")
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
